import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

# Function to add tasks to the list
def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

# Function to update the list
def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

# Function to delete a task from the list
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_to_delete = task_listbox.get(selected_index)
        tasks.remove(task_to_delete)
        the_cursor.execute('delete from tasks where title = ?', (task_to_delete,))
        list_update()
    except IndexError:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

# Function to edit a task
def edit_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_to_edit = task_listbox.get(selected_index)
        new_task = task_field.get()
        if len(new_task) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            tasks[selected_index] = new_task
            the_cursor.execute('update tasks set title = ? where title = ?', (new_task, task_to_edit))
            list_update()
            task_field.delete(0, 'end')
    except IndexError:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Edit.')

# Function to delete all tasks from the list
def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        while len(tasks) != 0:
            tasks.pop()
        the_cursor.execute('delete from tasks')
        list_update()

# Function to clear the list
def clear_list():
    task_listbox.delete(0, 'end')

# Function to close the application
def close():
    guiWindow.destroy()

# Function to retrieve data from the database
def retrieve_database():
    while len(tasks) != 0:
        tasks.pop()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

# Main function
if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#BFEFFF")  # Pale Turquoise background color

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="#BFEFFF")  # Pale Turquoise header background color
    functions_frame = tk.Frame(guiWindow, bg="#BFEFFF")  # Pale Turquoise functions background color
    listbox_frame = tk.Frame(guiWindow, bg="#BFEFFF")  # Pale Turquoise listbox background color

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="Vedeep's To-Do List",
        font=("Brush Script MT", 30),
        background="#BFEFFF",  # Pale Turquoise header background color
        foreground="#000080"  # Navy Blue header text color
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Consolas", 11, "bold"),
        background="#BFEFFF",  # Pale Turquoise functions background color
        foreground="#000080"  # Navy Blue functions text color
    )
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(
        functions_frame,
        font=("Consolas", 12),
        width=18,
        background="white",  # White entry field background color
        foreground="#000080"  # Navy Blue entry field text color
    )
    task_field.place(x=30, y=80)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task
    )
    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task
    )
    edit_button = ttk.Button(
        functions_frame,
        text="Edit Task",
        width=24,
        command=edit_task
    )
    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        command=delete_all_tasks
    )
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=close
    )
    add_button.place(x=30, y=120)
    del_button.place(x=30, y=160)
    edit_button.place(x=30, y=200)
    del_all_button.place(x=30, y=240)
    exit_button.place(x=30, y=280)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode='SINGLE',
        background="white",  # White listbox background color
        foreground="#000080",  # Navy Blue listbox text color
        selectbackground="#000080",  # Navy Blue listbox selected item background color
        selectforeground="white"  # White listbox selected item text color
    )
    task_listbox.place(x=10, y=20)

    retrieve_database()
    list_update()

    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()
