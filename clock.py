import time
import tkinter as tk

def clock():
    format_hour = time.strftime("%H:%M:%S")
    watch.config(text=format_hour)
    watch.after(1000, clock)

app = tk.Tk()
app.title("Clock")

watch = tk.Label(app, text="", font=("Roboto", 48))
watch.pack()

clock()
app.mainloop()