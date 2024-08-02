#Generate QR Code
import qrcode

def generate_qr_code():
    print("Welcome to the QR Code Generator Script!")
    data = input("Enter the data to encode in the QR code: ")
    output_file = input("Enter the output file name (e.g., 'qrcode.png'): ")

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR code saved as {output_file}")

if __name__ == "__main__":
    generate_qr_code()
