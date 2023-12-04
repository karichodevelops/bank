def home():
    display = """
    1. Safaricom\n
    2. M-PESA\n
    """
    return display

def call():
    disp = """
    1.SEND MONEY
    2.WITHDRAW CASH
    3.BUY AIRTIME
    4.LOANS AND SAVINGS
    5.LIPA NA MPESA
    6.MY ACCOUNT
    """
    return disp

def inputs(key):
    dicty = {    "1" : "phone no",     "2" : "amount",    "3" : "enter pin",    "4" : "till no",    "5" : "paybill no", "6" : "agent no", "7" : "store no" }
    value = ""
    value = dicty[key]
    return value



# resp = inputs("2")
# print(resp)
    


