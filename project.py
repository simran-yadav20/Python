import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Create GUI components
        self.task_entry = tk.Entry(root, width=35)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.mark_complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_complete)
        self.mark_complete_button.pack(pady=5)

         # Create Menu Bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # Add File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save", command=self.save_tasks)
        self.file_menu.add_command(label="Load", command=self.load_tasks)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Clear All", command=self.clear_all_tasks)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Add Help Menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index] += " (Completed)"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
