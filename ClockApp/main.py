import time
import math
import os
import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital & Analog Clock")
        self.root.geometry("500x600")
        self.root.configure(bg="black")

        # Digital Clock Label
        self.digital_label = tk.Label(root, font=("Arial", 24, "bold"), bg="black", fg="cyan")
        self.digital_label.pack(pady=10)

        # Create Analog Clock Canvas
        self.canvas = Canvas(root, width=300, height=300, bg="black", highlightthickness=0)
        self.canvas.pack(pady=20)

        # Load Clock Background Image
        self.load_clock_face()

        # Create Clock Hands
        self.hour_hand = self.canvas.create_line(150, 150, 150, 100, width=6, fill="white")
        self.minute_hand = self.canvas.create_line(150, 150, 150, 70, width=4, fill="red")
        self.second_hand = self.canvas.create_line(150, 150, 150, 50, width=2, fill="cyan")

        # Start Clock Update
        self.update_clock()

    def load_clock_face(self):
        """Loads clock face image if available, otherwise sets a plain background."""
        try:
            image_path = os.path.join(os.path.dirname(__file__), "clock_face.png")
            self.clock_img = Image.open(image_path)
            self.clock_img = self.clock_img.resize((300, 300), Image.LANCZOS)
            self.clock_photo = ImageTk.PhotoImage(self.clock_img)
            self.canvas.create_image(150, 150, image=self.clock_photo)
        except FileNotFoundError:
            print("⚠️ Clock face image not found. Using a plain background.")

    def update_clock(self):
        """Updates the digital and analog clock every second."""
        # Digital Clock
        current_time = time.strftime("%H:%M:%S")
        self.digital_label.config(text=current_time)

        # Get Current Time
        h, m, s = map(int, current_time.split(":"))

        # Convert Time to Angles
        hour_angle = (h % 12) * 30 + (m / 60) * 30
        minute_angle = m * 6
        second_angle = s * 6

        # Move Clock Hands
        self.update_hand(self.hour_hand, hour_angle, 50)
        self.update_hand(self.minute_hand, minute_angle, 70)
        self.update_hand(self.second_hand, second_angle, 90)

        # Repeat every second
        self.root.after(1000, self.update_clock)

    def update_hand(self, hand, angle, length):
        """Updates clock hands based on time angles."""
        x = 150 + length * math.sin(math.radians(angle))
        y = 150 - length * math.cos(math.radians(angle))
        self.canvas.coords(hand, 150, 150, x, y)

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
