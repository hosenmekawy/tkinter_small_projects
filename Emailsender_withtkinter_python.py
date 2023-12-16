import smtplib
import ssl
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    sender_email = 'your email'
    receiver_email = email.get()
    password = 'your api email password'
    subject = "Your Subject Here"
    body = "Hello, this is an automated email from our system."

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # The body and the attachments for the mail
    message.attach(MIMEText(body, "plain"))
    
    # Open file in bynary
    binary = open(filename, "rb")

    payload = MIMEBase('application', 'octate-stream', Name=filename)
    # To change the payload into encoded form
    payload.set_payload((binary).read())
    
    # enconding the binary into base64
    encoders.encode_base64(payload)
    
    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=filename)
    message.attach(payload)
    
    try:
        #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)
        
        #enable security
        session.starttls()
        
        #login with mail_id and password
        session.login(sender_email, password)
        text = message.as_string()
        session.sendmail(sender_email, receiver_email, text)
        session.quit()
        messagebox.showinfo("Success", "Email sent successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_image():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select an Image",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    label_img = Label(image=photo)
    label_img.image = photo  # keep a reference!
    label_img.pack()

root = Tk()

Label(root, text="Receiver Email:").pack()
email = Entry(root)
email.pack()

Button(root, text="Send Email", command=send_email).pack()
Button(root, text="Browse Image", command=browse_image).pack()

root.mainloop()
