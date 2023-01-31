import pywhatkit as kit
import datetime
'program opens whatsapp web and sends message'
i = 0
'your current system time'
now = datetime.datetime.now()

while i == 0:
    PersonalOrGroup = input("is this a personal message or a group message? (P/G):")
    if PersonalOrGroup == "P":
        PhoneNumber = input("please Enter the number you want to send a message to (ex:+90**********):")
        Message = input("please enter your message:")
        SpecificTime = input("if you want to send the message now, enter Y, or enter the N to specify the time")

        if SpecificTime == "Y":
            hour = now.hour
            'sends messages after 1 minutes of your current time'
            minute = now.minute + 1
            try:
                kit.sendwhatmsg(PhoneNumber, Message, hour, minute)
                print("message has been delivered")
                Continue = input("do you want to continue (Y/N):")
                if Continue == "Y":
                    i = 0
                elif Continue == "N":
                    i = 1
            except:
                print("error")

        elif SpecificTime == "N":
            hour = input("which hour you want to send message (0 - 23):")
            minute = input("which minute you want to send message (0 - 59):")
            try:
                kit.sendwhatmsg(PhoneNumber, Message, hour, minute)
                print("message has been delivered")
                if Continue == "Y":
                    i = 0
                elif Continue == "N":
                    i = 1
            except:
                print("error")

        else:
            print("please try again")

    if PersonalOrGroup == "G":
        'this is random key(it must be a string) of the link after the last /   (ex:FESXxsQA6D58LU6kc2964J)'
        GroupId = input("please enter the group id you want to send message:")
        Message = input("please enter your message:")
        SpecificTime = input("if you want to send the message now, enter Y, or enter the N to specify the time")

        if SpecificTime == "Y":
            hour = now.hour
            'sends messages after 1 minutes of your current time'
            minute = now.minute + 1
            try:
                kit.sendwhatmsg_to_group(GroupId, Message, hour, minute)
                print("message has been delivered")
                if Continue == "Y":
                    i = 0
                elif Continue == "N":
                    i = 1
            except:
                print("error")

        elif SpecificTime == "N":
            hour = input("which hour you want to send message (0 - 23):")
            minute = input("which minute you want to send message (0 - 59):")
            try:
                kit.sendwhatmsg_to_group(GroupId, Message, hour, minute)
                print("message has been delivered")
                if Continue == "Y":
                    i = 0
                elif Continue == "N":
                    i = 1
            except:
                print("error")

        else:
            print("please try again")

    else:
        print("please try again")
        i = 0

    if i == 1:
        break

'neganwashere'

