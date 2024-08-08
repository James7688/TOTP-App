import pyotp
import qrcode
from tkinter import Tk, Label, Entry, Button, StringVar, filedialog, messagebox
from PIL import ImageTk, Image

class TOTPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TOTP App")

        # StringVars for dynamic content
        self.secret_var = StringVar()
        self.otp_var = StringVar()

        # UI Elements
        Label(root, text="TOTP Secret Key:").grid(row=0, column=0, padx=10, pady=10)
        self.secret_entry = Entry(root, textvariable=self.secret_var, width=40)
        self.secret_entry.grid(row=0, column=1, padx=10, pady=10)

        Button(root, text="Generate New Secret", command=self.generate_secret).grid(row=1, column=0, padx=10, pady=10)
        Button(root, text="Generate OTP", command=self.generate_otp).grid(row=2, column=0, padx=10, pady=10)
        Entry(root, textvariable=self.otp_var, width=20).grid(row=2, column=1, padx=10, pady=10)

        Label(root, text="Verify OTP:").grid(row=3, column=0, padx=10, pady=10)
        self.otp_entry = Entry(root, width=20)
        self.otp_entry.grid(row=3, column=1, padx=10, pady=10)
        Button(root, text="Verify", command=self.verify_otp).grid(row=4, column=0, padx=10, pady=10)

        Button(root, text="Generate QR Code", command=self.generate_qr_code).grid(row=5, column=0, padx=10, pady=10)
        Button(root, text="Save QR Code", command=self.save_qr_code).grid(row=5, column=1, padx=10, pady=10)

        # Image placeholder for QR code
        self.qr_image_label = Label(root)
        self.qr_image_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def generate_secret(self):
        secret = pyotp.random_base32()
        self.secret_var.set(secret)

    def generate_otp(self):
        secret = self.secret_var.get()
        if not secret:
            messagebox.showerror("Error", "Please enter or generate a TOTP secret key.")
            return

        self.totp = pyotp.TOTP(secret)
        otp = self.totp.now()
        self.otp_var.set(otp)

    def verify_otp(self):
        secret = self.secret_var.get()
        if not secret:
            messagebox.showerror("Error", "Please enter or generate a TOTP secret key.")
            return

        user_otp = self.otp_entry.get()
        self.totp = pyotp.TOTP(secret)

        if self.totp.verify(user_otp):
            messagebox.showinfo("Result", "The OTP is valid!")
        else:
            messagebox.showerror("Result", "The OTP is invalid!")

    def generate_qr_code(self):
        secret = self.secret_var.get()
        if not secret:
            messagebox.showerror("Error", "Please enter or generate a TOTP secret key.")
            return

        uri = pyotp.TOTP(secret).provisioning_uri(name="YourAppName", issuer_name="YourCompanyName")
        qr = qrcode.make(uri)
        qr_image = ImageTk.PhotoImage(qr)
        self.qr_image_label.configure(image=qr_image)
        self.qr_image_label.image = qr_image

    def save_qr_code(self):
        secret = self.secret_var.get()
        if not secret:
            messagebox.showerror("Error", "Please enter or generate a TOTP secret key.")
            return

        uri = pyotp.TOTP(secret).provisioning_uri(name="YourAppName", issuer_name="YourCompanyName")
        qr = qrcode.make(uri)
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            qr.save(file_path)
            messagebox.showinfo("Success", f"QR code saved as {file_path}")

if __name__ == "__main__":
    root = Tk()
    app = TOTPApp(root)
    root.mainloop()