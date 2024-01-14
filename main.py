import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Читатель Мыслей')
root.geometry('300x200')
root.resizable(False, False)
root.iconbitmap('img/logo.ico')
root['bg'] = '#ffeea8'

def hide_progress_bar():
    progress_bar.stop()
    number = input_field.get()
    label.config(text=f'Вы загадали число '+ str(number))
    new_window.after(10000, new_window.destroy)

def update_text():
    label.config(text="Я думаю, читаю твои мысли...", font=40, bg='#ffeea8')

def open_new_window():
    global new_window, progress_bar, label
    new_window = tk.Toplevel(root)
    new_window.title("Читатель мыслей")
    new_window['bg'] = '#ffeea8'
    new_window.iconbitmap('img/logo.ico')

    label = tk.Label(new_window, text="New Window")
    label.pack(pady=10)
    
    progress_bar = ttk.Progressbar(new_window, orient="horizontal", mode="indeterminate", length=300)
    progress_bar.pack(pady=10)

    new_window.after(6000, hide_progress_bar)
    new_window.after(0, update_text)

    progress_bar.start()
    
title = tk.Label(root, text='Загадайте число от 1 до 10:', font=40, bg='#ffeea8', pady=35)
title.pack()

input_field = tk.Entry(root, bg='#acbf69')
input_field.pack()

btn = tk.Button(root, text='Прочитать мои мысли...', bg='#acbf69', border=0, command=open_new_window)
btn.pack(padx=10, pady=30)

root.mainloop()