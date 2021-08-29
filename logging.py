import datetime
curdate = datetime.datetime.now().strftime("%Y-%m-%d %I-%M-%S")
ext = ".txt"

while(True):
    name = input("Enter the name            : ")
    if name == 'quit':
        break
    phone_num = input("Enter the phone number    : ")
    place = input("Enter the place           : ")
    temp = input("Enter the body temperature: ")

    myfile = open(curdate+ext,'a')
    myfile.write("Name        : "+name)
    myfile.write("\nPhone Number: "+phone_num)
    myfile.write("\nPlace       : "+place)
    myfile.write("\nTemperature : "+temp+"\r\n")
print("Data saved to the file..")
myfile.close()

