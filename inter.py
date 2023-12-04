from method import home, call

STEPS = 5
current = 1
response = ""

while(current != STEPS):
    if(current == 1):
        print(home())
        response = int(input("Enter option:"))
    elif(current == 2):
        if response == 1:
            print("under development")
        else:
            

            print(call())
            response = int(input("Enter service:"))
    





    current = current + 1
