#Deploy website internet service

#Welcome massage
print("Hello in Net Application")

#Variables & input

name = input("PLase enter your name: ")

#A date start from customer
date_start = input("Plase enter your first_day of net: ")

#End date
date_end = input("Plase enter your end_date of net: ")

#Phone number of customer
phone_number = input("PLease enter your phone number: ")

#Variable
service_day =1

while service_day < 30 :
    print(service_day)
    service_day +=1

else:
    print("Hello MR. " + name)
    print("Your Net service is end today: " + str(date_end) + "that start in : " + str(date_start))
    print("your phone number is : " + str(phone_number))


#THanks customer
print("thank you for use our service .")