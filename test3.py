import os
from telethon.sync import TelegramClient
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

class TelegramSender:
    def __init__(self, root, api_id, api_hash, phone):
        self.client = TelegramClient('session_name', api_id, api_hash)
        self.client.start()

        self._create_widgets(root)

    def _create_widgets(self, root):
        self._create_label_entry(root, "Receiver Username:")
        self._create_label_entry(root, "Message:")
        self._create_label_entry(root, "Image:")

        Button(root, text="Browse Image", command=self.browse_image).pack()
        Button(root, text="Send Telegram Message", command=self.send_telegram_message).pack()

    def _create_label_entry(self, root, text):
        Label(root, text=text).pack()
        entry = Entry(root)
        entry.pack()
        setattr(self, text.lower().replace(":", "").replace(" ", "_") + "_entry", entry)

    def browse_image(self):
        filename = filedialog.askopenfilename(filetypes=[('Image Files', '*.png *.jpg *.jpeg *.gif')])
        self.image_entry.delete(0, 'end')
        self.image_entry.insert(0, filename)

    def send_telegram_message(self):
        receiver = self.receiver_username_entry.get()
        message = self.message_entry.get()
        image_path = self.image_entry.get()
        if os.path.isfile(image_path):
            try:
                self.client.send_file(receiver, image_path, caption=message)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Invalid image path")

root = Tk()
root.geometry('300x200')  # Set the window size

api_id = 'Replace with your API ID'  # Replace with your API ID
api_hash = 'Replace with your API hash'  # Replace with your API hash
phone = 'your phone'  # Replace with your phone number

app = TelegramSender(root, api_id, api_hash, phone)

root.mainloop()
