from tkinter import messagebox
import tkinter as tk
import cv2
import time
import threading
from datetime import datetime
from telegram import Bot
import torch
import numpy as np

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Object Detection App")

        # Initialize Telegram bot
        self.bot = Bot(token="enter your token here")

        self.create_widgets()

    def create_widgets(self):
        # Label to display date and time
        self.datetime_label = tk.Label(self.root, text="")
        self.datetime_label.pack()

        # Button to run Fall Detection
        fall_detection_button = tk.Button(self.root, text="Run Fall Detection", command=self.run_fall_detection)
        fall_detection_button.pack()

        # Button to run Object Detection
        object_detection_button = tk.Button(self.root, text="Run Object Detection", command=self.run_object_detection)
        object_detection_button.pack()

        # Quit button
        quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        quit_button.pack()

        # Update date and time
        self.update_datetime()

    def run_fall_detection(self):
        try:
            # Write your fall detection code here

            # Notify user when finished
            self.show_notification("Fall Detection finished.")
        except Exception as e:
            self.show_notification(f"Error in Fall Detection: {str(e)}")

    def run_object_detection(self):
        try:
            # Write your object detection code here

            # Notify user when finished
            self.show_notification("Object Detection finished.")
        except Exception as e:
            self.show_notification(f"Error in Object Detection: {str(e)}")

    def show_notification(self, message):
        tk.messagebox.showinfo("Notification", message)

    def update_datetime(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.datetime_label.config(text=current_time)
        self.root.after(1000, self.update_datetime)

def run_app():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Run the Tkinter app in a separate thread to avoid blocking the main thread
    app_thread = threading.Thread(target=run_app)
    app_thread.start()
