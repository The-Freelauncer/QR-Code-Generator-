import qrcode 

url = input("Enter a Test or URL : ")

img = qrcode.make(url)

n = int(input("Do you want a Default Filename or a Custom one \n Press 1 for Default Filename \n Press 2 for Custom Filename \n Enter your Choice : "))

if (n == 1):
    img.save("QRcode.png")
    print("QR code Generated Successfully")
    print("You will find the QRcode attached in the same folder")

elif (n == 2):
    img.save((input("Enter a custom filename without giving any extension : ") + ".png"))
    print("QR code Generated Successfully")
    print("You will find the QRcode attached in the same folder")

else :
    print("Invalid Input , Please Try Again !!! ")
