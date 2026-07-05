import qrcode #Install it first by pip install qrcode    

#Taking UPI ID as a input..
upi_id = input("Enter your UPI ID: ")

#upi://pay?pa=UPI_ID%apn=NAME&am=Amount&cu=Currency&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
navi_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)
navi_qr = qrcode.make(navi_url)

#Save the QR Code to image file (optional)
phonepe_qr.save('phonepe-qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
navi_qr.save('navi_qr.png')

#Display the QR Code (you maky need to install PIL/Pillow Library)
choice = input("Which QR code do you want to view? (phonepe/paytm/googlepay/navi): ").lower()
qr_map = {
    'phonepe': phonepe_qr,
    'paytm': paytm_qr,
    'googlepay': google_pay_qr,
    'navi': navi_qr   
}

if choice in qr_map:
    qr_map[choice].show()
else:
    print("Invalid choice.")   


