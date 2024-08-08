# TOTP App

A Python application for generating and verifying Time-based One-Time Passwords (TOTP) as part of a two-step verification process. This app also allows you to generate a QR code for easy setup with authenticator apps like Google Authenticator.

## Features

- **Generate TOTP Secret Key**: Create a new secret key for setting up two-step verification.
- **Input Existing Secret**: Use an existing secret key to generate and verify OTP codes.
- **Generate OTP**: Generate a one-time password based on the provided secret key.
- **Verify OTP**: Verify if the provided OTP is correct.
- **Generate QR Code**: Generate a QR code for the TOTP, which can be scanned by an authenticator app.
- **Save QR Code**: Save the generated QR code as a PNG file.

## Requirements

The following Python modules are required to run the app:

- `pyotp`: For generating and verifying OTPs.
- `qrcode[pil]`: For generating QR codes.
- `Pillow`: For handling and displaying images.
- `tkinter`: For creating the graphical user interface (built-in with Python).

You can install the required modules using `pip`:

```bash
pip install pyotp qrcode[pil] pillow
```

## Installation:
Clone the repository using `git`:
```bash
git clone https://github.com/James7688/TOTP-App.git
```
Navigate into the project directory:

```bash
cd TOTP-App
```

**You can install the .exe file here:**
[Download it here.](https://github.com/James7688/TOTP-App/blob/main/TOTP%20Application.exe)

## CREDIT:
Quy Anh Nguyen - Developer
