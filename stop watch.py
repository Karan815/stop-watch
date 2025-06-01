import tkinter as tk
from datetime import datetime
import time
import threading

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch & Clock")
        self.root.geometry("350x250")
        self.root.configure(bg="#f0f0f0")

        # Clock Label
        self.clock_label = tk.Label(root, text="", font=("Arial", 16), fg="blue", bg="#f0f0f0")
        self.clock_label.pack(pady=10)

        # Stopwatch Label
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 32), bg="#f0f0f0")
        self.stopwatch_label.pack(pady=10)

        # Stopwatch Buttons
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Start", width=10, command=self.start)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(self.button_frame, text="Stop", width=10, command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(self.button_frame, text="Reset", width=10, command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=5)

        # Stopwatch variables
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Start updating the clock
        self.update_clock()

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text="Current Time: " + now)
        self.root.after(1000, self.update_clock)

    def update_stopwatch(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            formatted_time = self.format_time(self.elapsed_time)
            self.stopwatch_label.config(text=formatted_time)
            self.root.after(100, self.update_stopwatch)

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_stopwatch()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

    @staticmethod
    def format_time(seconds):
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        return f"{h:02}:{m:02}:{s:02}"

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchClockApp(root)
    root.mainloop()
