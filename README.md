# RFID-Smart-Cashier-with-Recommendation-System
The study used Radio Frequency Identification (RFID) to get data of each item that will be purchased. 
Based on data analytic technique, this research focus on the use of association rules. 
The collected data from RFID then compared with the rules, and the system will be able to recommend the items that customers might interest respected to the association rules. All transactions will be kept in record and be able to utilize in terms of increasing more samples in dataset to improve the association rules, and in terms of business intelligences, such as warehouse management, reducing cost and time, faster process, better resource allocation.   Keywords—Radio Frequency Identification, Association Rule, Business Intelligence
################################################

# A.	System Design
- The smart cashier cabinet is embed with an Arduino UNO which is connected with RFID module PN532 and touch switch. RFID PN532 module will read data from RFID tag, in this paper we introduce 15 sample tags and 1 sample credit card. Touch switch will be pressed when the item scanning is done. It will require the valid payment by scanning the  specific card, if scanning fail over 5 times, it will reject the current transaction and ready for the new transaction. 
- In terms of data analytic, we used dataset “Instacart Market Basket Analysis” from www.kaggle.com to find association rule in this scenario. All 45,150 rules were stored in rules.csv, each has its own id, name, aisle number, and department etc. We upload this dataset into Colab and implement Python to find association rule, sorting from the highest Lift value. Then, we map RFID tag with item code, in this scenario we introduce 15 items.

# B.	System Components
- Hardware components consist of Physical cabinet, RFID module, RFID tags, Arduino UNO, touch switch, and LCD display.
- Software components consist of Arduino IDE for controlling Arduino UNO, RFID module and touch switch. Colab for association rule data analysis. Python 3.6.3 for recommendation system and report generating.
