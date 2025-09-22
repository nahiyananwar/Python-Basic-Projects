'''
Write a program to generate a QR code based on user input, such as text or a
URL. The QR code should be saved as an image file that can be scanned with a
smartphone.

->Add options for the user to choose the color of the QR code. This will allow
users to generate QR codes that match their style or branding. 

->Implement a feature that lets the user generate multiple QR codes at once by
providing a list of URLs or texts. Each QR code should be saved with a unique
filename. 

'''

import qrcode

user_input = input("Enter a text or URL for QR Code:\n> ").strip()
file_name = input(
    "\nEnter the name of the generated QRcode image:\n> ").strip()

qr = qrcode.QRCode(box_size=10, border=4)

qr.add_data(user_input)

f_color = input("\nEnter the color of the qrcode:\n> ").lower()
b_color = input("\nEnter the Background color of the qrcode:\n> ").lower()

image = qr.make_image(fill_color=f_color, back_color=b_color)

image.save(file_name)

print(f"QR code generated. It's saved as {file_name}.")
