import qrcode

user_input = input("Enter a text or URL for QR Code:\n> ")
file_name = input("Enter the name of the generated QRcode image:\n> ")

qr = qrcode.QRCode(box_size=10, border=4)

qr.add_data(user_input)

image = qr.make_image(fill_color='black', back_color='white')

image.save(file_name)

print(f"QR code generated. It's saved as {file_name}.")
