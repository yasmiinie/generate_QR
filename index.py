import pandas as pd
import qrcode

# Function to generate QR code for a given ID
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qrcodes/{data}.png")  # Save the QR code with the ID as the filename
    return f"qrcodes/{data}.png"

# Read CSV file
df = pd.read_csv("QR.csv")

# Add a new column with the QR code links
df['QRCodeLink'] = df['ID'].apply(generate_qr_code)

# Save the updated DataFrame to a new CSV file
df.to_csv("output_file.csv", index=False)
