import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_frame = tk.Frame(frame_tasks)
        task_label = tk.Label(task_frame, text=task, width=40)
        task_label.pack(side=tk.LEFT)
        edit_button = tk.Button(task_frame, text="Edit", command=lambda: edit_task(task_frame))
        delete_button = tk.Button(task_frame, text="Delete", command=lambda: remove_task(task_frame))
        edit_button.pack(side=tk.LEFT, padx=5)
        delete_button.pack(side=tk.LEFT, padx=5)
        task_frame.pack(pady=5)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task(frame):
    frame.destroy()

def edit_task(frame):
    task_text = frame.winfo_children()[0].cget("text")
    entry.delete(0, tk.END)
    entry.insert(0, task_text)
    frame.destroy()

root = tk.Tk()
root.title("To-Do List")

# Add heading
heading = tk.Label(root, text="To-Do List", font=("Helvetica", 16, "bold"))
heading.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(root, width=35)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

frame_tasks = tk.Frame(root)
frame_tasks.pack()

root.mainloop()
