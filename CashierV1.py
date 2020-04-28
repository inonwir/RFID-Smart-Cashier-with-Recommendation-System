import serial #for Serial communication
import time   #for delay functions
from genprofile import update_profile
import pandas as pd
import winsound as ws
 
arduino = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print (arduino.readline()) #read the serial data and print it as line

rfidset = set()
counter_customer = 1
store_df = pd.read_csv('store.csv')
rules_df = pd.read_csv('rules.csv')
product_df = pd.read_csv('products.csv')

print("Please scan your items:")



while 1:      #Do this in loop
    line = arduino.readline().decode('utf-8')
    if(line.find('UID Value:') != -1):
        #print(line)
        ws.PlaySound('beep-07.wav',1)
        rfid = line[12:-2]
        print("RFID Value : ", rfid)
        rfidset.add(rfid)
        #print(rfidset)
    elif(line.find('Exit') != -1):
        ws.PlaySound('beep-02.wav',1)
        #print(rfidset)
        #f = open('customer_orders.txt','w');
        #for i in rfidset:
        #    f.write(str(i) + '\n')
        #f.close()
        rfidlist = list(rfidset)
        rfidset.clear()
        

        # Generate Report
        items = store_df[store_df['rfid'].isin(rfidlist)]
        productid_list = items['product_id'].to_list()
        productname_list = items['product_name'].to_list()
        price_list = items['price'].to_list()
        info_recipt = 'GG SHOP Co(071095)\nTAX#123456789513 (VAT Included)\n===============================================\nReceipt\n===============================================\n'
        print('Order')
        for i in range(len(productid_list)):
            info_recipt += "%4d\t%40s\t%4d\n"%(i, productname_list[i], price_list[i])
            print("%4d\t%50s\t%4d"%(productid_list[i], productname_list[i], price_list[i]))
        info_recipt += 'Total : %d Baht\n'%sum(price_list)
        print('Total : %d Baht'%sum(price_list))

        info_recipt += '===============================================\n'

        info_recipt += 'Products that you might interested\n'
        print('Products that you might interested')
        for id in productid_list:
            try:
                product_b = rules_df.loc[rules_df.Product_A == id].loc[rules_df.Lift > 10]
                b_id   = product_b.Product_B.to_list()[0]
                b_name = product_b.product_B_name.to_list()[0]
                aisleid = product_df.loc[product_df.product_id == b_id]['aisle_id'].to_list()[0]
                info_recipt += '%6d\t%50s\t\tcheck it out at aisle no. %4d\n'%(b_id, b_name,aisleid) 
                print('%6d\t%70s\t\tcheck it out at aisle no. %4d'%(b_id, b_name,aisleid))
    
    
                product_a = rules_df.loc[rules_df.Product_B == id].loc[rules_df.Lift > 10]
                a_id   = product_a.Product_A.to_list()[0]
                a_name = product_a.product_A_name.to_list()[0]
                aisleid = product_df.loc[product_df.product_id == a_id]['aisle_id'].to_list()[0]
                info_recipt += '%6d\t%50s\t\tcheck it out at aisle no. %4d\n'%(a_id, a_name, aisleid)
                print('%6d\t%70s\t\tcheck it out at aisle no. %4d'%(a_id, a_name, aisleid))
            except:
                pass
        info_recipt += '-----------------------------------------------\nTHANK YOU\n** CUSTOMER COPY **\n** NO REFUND **\n'

        print('Total : %d Baht\nPresent your credit card : '%sum(price_list))
        error_count = 0
        while error_count < 5:
            line = arduino.readline().decode('utf-8')
            if(line.find('UID Value:') != -1):
                ws.PlaySound('beep-07.wav',1)
                rfid = line[12:-2]
                if rfid == '0x73 0x97 0xD5 0x1B':
                    print('purchase success!!')
                    f = open('Receipt_%d.txt'%(counter_customer),'w');
                    f.write(info_recipt)
                    f.close()
                    update_profile(productid_list, counter_customer)
                    counter_customer += 1
                    break
                else:
                    print('Invalid Card. Try again.')
                    print('%d attempts'%(4-error_count))
                    error_count += 1
        if error_count == 5:
            print('Cancel Invoice!!!')

        ws.PlaySound('beep-06.wav',1)
        print("Please scan your items:")
        
