import pandas as pd

#order_df = pd.read_csv('order_profile.csv')
#store_df = pd.read_csv('store.csv')

def update_profile(productid_list, transaction_id):
    #time product_id transaction_id
    current_time  =  pd.datetime.now().timestamp()
    N_items = len(productid_list)
    profile = list(zip([current_time]*N_items, productid_list, [transaction_id]*N_items))
    profile_df = pd.DataFrame(profile, columns = ['time', 'product_id', 'transaction_id'])
    #print(profile_df)
    profile_df.to_csv('order_profile.csv', mode = 'a', index = False, header = False)
    #with open('order_profile.csv', 'a') as f:
    #    profile_df.to_csv(f, index = False, header = False)
    #    f.close()

if __name__ == '__main__':
    update_profile([11,22,33],4)
