import tkinter as tk
from tkinter import font

class FancyCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Fancy Counter ✨")
        self.root.geometry("400x300")
        self.root.config(bg="#1e1e2f")

        self.count = 0

        
        self.title_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.count_font = font.Font(family="Courier", size=50, weight="bold")
        self.btn_font = font.Font(family="Helvetica", size=14)

        tk.Label(root, text="Fancy Counter", font=self.title_font, bg="#1e1e2f", fg="#ffffff").pack(pady=10)

        self.counter_label = tk.Label(root, text=str(self.count), font=self.count_font, fg="#00ffd5", bg="#1e1e2f")
        self.counter_label.pack(pady=20)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#1e1e2f")
        btn_frame.pack()

        # Decrement Button
        self.decrement_btn = tk.Button(btn_frame, text="-", font=self.btn_font, width=5, bg="#ff4d4d", fg="white",
                                       activebackground="#ff1a1a", command=self.decrement)
        self.decrement_btn.pack(side="left", padx=20)
        self.add_hover_effect(self.decrement_btn, "#ff4d4d", "#ff1a1a")

        # Increment Button
        self.increment_btn = tk.Button(btn_frame, text="+", font=self.btn_font, width=5, bg="#33cc33", fg="white",
                                       activebackground="#2eb82e", command=self.increment)
        self.increment_btn.pack(side="right", padx=20)
        self.add_hover_effect(self.increment_btn, "#33cc33", "#2eb82e")

    def increment(self):
        self.count += 1
        self.update_display()

    def decrement(self):
        self.count -= 1
        self.update_display()

    def update_display(self):
        self.counter_label.config(text=str(self.count))

    def add_hover_effect(self, widget, normal_bg, hover_bg):
        widget.bind("<Enter>", lambda e: widget.config(bg=hover_bg))
        widget.bind("<Leave>", lambda e: widget.config(bg=normal_bg))

if __name__ == "__main__":
    root = tk.Tk()
    app = FancyCounter(root)
    root.mainloop()
