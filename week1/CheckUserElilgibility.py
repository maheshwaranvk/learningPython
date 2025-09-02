# Assignment : https://drive.google.com/open?id=1UACPjjcV_VbDvOEDJjFGSzoPdhcRTfpQ&usp=drive_fs

correctPassword = "openAI123"
count=0
for i in range(3):
    userPassword = input("Enter your password: ")
    if (userPassword == correctPassword):
        print("Login Successful")
        break
    else:
        count= count+1
if (count==3):
    print("Account Locked")