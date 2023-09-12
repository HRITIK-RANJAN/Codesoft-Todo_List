import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import ttk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for task in tasks:
            task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

app = tk.Tk()
app.title("To-Do List")

# Styling
font_style = font.Font(family="Helvetica", size=12)
task_listbox_style = ttk.Style()
task_listbox_style.configure("TaskListbox.TListbox", font=font_style)

# Create and configure GUI elements
task_entry = tk.Entry(app, font=font_style, width=40)
task_entry.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

add_button = tk.Button(app, text="Add Task", font=font_style, command=add_task)
add_button.grid(row=0, column=2, padx=10, pady=20)

remove_button = tk.Button(app, text="Remove Task", font=font_style, command=remove_task)
remove_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

clear_button = tk.Button(app, text="Clear All", font=font_style, command=clear_tasks)
clear_button.grid(row=1, column=1, padx=10, pady=10)

save_button = tk.Button(app, text="Save Tasks", font=font_style, command=save_tasks)
save_button.grid(row=1, column=2, padx=20, pady=10, sticky="e")

task_listbox = tk.Listbox(app, font=font_style, selectbackground="sky blue", height=10, width=50)
task_listbox.grid(row=2, column=0, padx=20, pady=20, columnspan=3)

# Load tasks from a file (if any)
load_tasks()

app.mainloop()
