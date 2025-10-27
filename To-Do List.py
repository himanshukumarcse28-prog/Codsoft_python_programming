# To-Do List application

import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List ")
root.geometry("400x450")
root.config(bg="#f4f4f4")

tasks = []

# --- Functions ---

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = task_entry.get().strip()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        tasks.remove(task)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?"):
        tasks.clear()
        update_listbox()

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        if not task.startswith("✔️ "):
            tasks[selected] = "✔️ " + task
            update_listbox()
        else:
            messagebox.showinfo("Info", "Task already marked as done.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark done.")

# --- UI Layout ---

title_label = tk.Label(root, text="To-Do List", font=("Arial", 20, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=25, font=("Arial", 14))
task_entry.grid(row=0, column=0, padx=10)

add_btn = tk.Button(frame, text="Add", width=10, bg="#4CAF50", fg="white", command=add_task)
add_btn.grid(row=0, column=1)

listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12), selectmode=tk.SINGLE)
listbox.pack(pady=10)

btn_frame = tk.Frame(root, bg="#f4f4f4")
btn_frame.pack(pady=10)

done_btn = tk.Button(btn_frame, text="Mark Done", width=12, bg="#2196F3", fg="white", command=mark_done)
done_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete", width=12, bg="#f44336", fg="white", command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear All", width=12, bg="#9E9E9E", fg="white", command=clear_all)
clear_btn.grid(row=0, column=2, padx=5)

# Run main window loop
root.mainloop()
