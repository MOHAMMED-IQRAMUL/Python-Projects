import time
import threading
import customtkinter as ctk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("400x350")
        ctk.set_appearance_mode("dark")  # Dark Mode
        ctk.set_default_color_theme("blue")

        self.time_left = 0
        self.running = False

        # Title Label
        self.label = ctk.CTkLabel(root, text="Select Time", font=("Arial", 16))
        self.label.pack(pady=10)

        # Time Picker (Dropdowns for HH, MM, SS)
        self.hours = ctk.CTkComboBox(root, values=[f"{i:02}" for i in range(24)], width=80)
        self.minutes = ctk.CTkComboBox(root, values=[f"{i:02}" for i in range(60)], width=80)
        self.seconds = ctk.CTkComboBox(root, values=[f"{i:02}" for i in range(60)], width=80)

        self.hours.pack(side="left", padx=5, pady=5)
        self.minutes.pack(side="left", padx=5, pady=5)
        self.seconds.pack(side="left", padx=5, pady=5)

        # Time Display
        self.timer_display = ctk.CTkLabel(root, text="00:00:00", font=("Arial", 30))
        self.timer_display.pack(pady=10)

        # Buttons
        self.start_button = ctk.CTkButton(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.pause_button = ctk.CTkButton(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(pady=5)

        self.reset_button = ctk.CTkButton(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=5)

    def start_timer(self):
        if not self.running:
            try:
                h = int(self.hours.get())
                m = int(self.minutes.get())
                s = int(self.seconds.get())
                self.time_left = h * 3600 + m * 60 + s
                self.running = True
                self.update_timer()
            except:
                messagebox.showerror("Error", "Select a valid time!")

    def update_timer(self):
        if self.running and self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            hours, mins = divmod(mins, 60)
            self.timer_display.configure(text=f"{hours:02}:{mins:02}:{secs:02}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0 and self.running:
            self.running = False
            messagebox.showinfo("Time's Up!", "Countdown Finished!")

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.timer_display.configure(text="00:00:00")

# Run App
if __name__ == "__main__":
    root = ctk.CTk()
    app = CountdownTimer(root)
    root.mainloop()
