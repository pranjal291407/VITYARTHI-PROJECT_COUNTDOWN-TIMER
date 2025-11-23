import tkinter as tk
from tkinter import messagebox
import time
import threading

def start_timer():
    
    try:
        total_seconds = int(time_entry.get()) * 60
        if total_seconds <= 0:
            messagebox.showerror( "Please enter a positive number of minutes.")
            return
    except ValueError:
        messagebox.showerror( "That's not a valid number. Try again!")
        return

    
    task_name = task_entry.get()
    start_button.config(state="disabled")

   
    def countdown():
        remaining = total_seconds
        while remaining >= 0:
            minutes = remaining // 60
            seconds = remaining % 60
            timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            root.update() 
            time.sleep(1)
            remaining -= 1
        
       
        messagebox.showinfo("All Done!", f"Great job on completing '{task_name}'!")
        start_button.config(state="normal")

   
    threading.Thread(target=countdown).start()


root = tk.Tk()
root.title("Simple Countdown Timer")
root.geometry("300x300")


tk.Label(root, text="Enter your task", font=("Arial", 12)).pack(pady=5)
task_entry = tk.Entry(root, font=("Arial", 12))
task_entry.pack()


tk.Label(root, text="How many minutes?", font=("Arial", 12)).pack(pady=5)
time_entry = tk.Entry(root, font=("Arial", 12))
time_entry.pack()


start_button = tk.Button(root, text="Start Timer", font=("Arial", 12), command=start_timer)
start_button.pack(pady=10)


timer_label = tk.Label(root, text="00:00", font=("Arial", 30), fg="blue")
timer_label.pack(pady=20, expand=True)


root.mainloop()
