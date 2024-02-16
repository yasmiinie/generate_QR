import pandas as pd
import qrcode
import os

# Function to generate QR code for a given ID and name
def generate_qr_code(row):
    data = f"{row['Name']}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Ensure the "qrcodes" folder exists
    os.makedirs("qrcodes", exist_ok=True)

    file_name = f"qrcodes/{data}.png"
    img.save(file_name)
    return file_name

# Read CSV file
df = pd.read_csv("QR.csv")

# Add a new column with the QR code links
df['QRCodeLink'] = df.apply(generate_qr_code, axis=1)

# Save the updated DataFrame to a new CSV file
df.to_csv("output_file.csv", index=False)
