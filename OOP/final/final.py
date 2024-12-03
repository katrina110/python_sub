import datetime
import csv
import tkinter as tk
from tkinter import messagebox, filedialog


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if len(self.contacts) >= 100:
            messagebox.showinfo("Info", "Address book is full. Cannot add more contacts.")
        else:
            self.contacts.append(contact)

    def edit_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower():
                results.append(contact)
        return results

    def save_to_csv(self, file_name):
        try:
            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Phone', 'Email'])
                for contact in self.contacts:
                    writer.writerow([contact.name, contact.phone, contact.email])
            messagebox.showinfo("Success", "Address book saved successfully.")
        except IOError:
            messagebox.showerror("Error", "An error occurred while saving the address book.")

    def load_from_csv(self, file_name):
        try:
            with open(file_name, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    name, phone, email = row
                    contact = Contact(name, phone, email)
                    self.contacts.append(contact)
            messagebox.showinfo("Success", "Address book loaded successfully.")
        except IOError:
            messagebox.showerror("Error", "An error occurred while loading the address book.")


class AddressBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Address Book")
        self.root.geometry("600x600")
        self.root.configure(bg="#d9b99b")

        self.address_book = AddressBook()
        self.night_mode = False

        self.create_widgets()

        self.contact_count_label = tk.Label(self.root, text="Contacts saved: 0", bg="#d9b99b")
        self.contact_count_label.pack(side=tk.BOTTOM, anchor=tk.SE)

    def create_widgets(self):
        self.root.config(bg="#d9b99b")

        content_frame = tk.Frame(self.root, bg="#d9b99b")
        content_frame.pack(expand=True)

        title_label = tk.Label(content_frame, text="Address Book", font=("Arial", 16), bg="#a67a5b", fg="white")
        title_label.grid(row=0, column=0, columnspan=3, pady=20, sticky=tk.W + tk.E)  # Center horizontally

        menu_label = tk.Label(content_frame, text="What would you like to do?", font=("Arial", 12), bg="#a67a5b",
                              fg="white")
        menu_label.grid(row=1, column=0, columnspan=3, pady=20, sticky=tk.W + tk.E)  # Center horizontally

        options = ["Add Contact", "Edit Contact", "Delete Contact", "View Contacts", "Search Address Book", "Exit"]

        for i, option in enumerate(options):
            btn = tk.Button(content_frame, text=option, width=50, bg="#614e55", fg="white",
                            command=lambda idx=i: self.handle_option(idx))
            btn.grid(row=i + 2, column=1, padx=20, pady=10, sticky=tk.W + tk.E)  # Center horizontally

        self.time_label = tk.Label(content_frame, text="", font=("Arial", 12), bg="#d9b99b", fg="black")
        self.time_label.grid(row=len(options) + 4, column=0, columnspan=6, pady=20, sticky=tk.NE)


        self.save_btn = tk.Button(content_frame, text="Save", width=10, command=self.save_address_book,
                                  bg="#757575", fg="white")
        self.save_btn.grid(row=len(options) + 2,column=0, columnspan=6, padx=10, pady=(0, 0))

        self.load_btn = tk.Button(content_frame, text="Load", width=10, command=self.load_address_book,
                                  bg="#757575", fg="white")
        self.load_btn.grid(row=len(options) + 3, column=0, columnspan=6, padx=0, pady=(10, 10))

        self.night_mode_btn = tk.Button(content_frame, text="Night Mode", width=10, command=self.toggle_night_mode,
                                        bg="#BB86FC", fg="white")
        self.night_mode_btn.grid(row=len(options) + 4, column=0, columnspan=6, padx=0, pady=(10, 0))

        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        content_frame.configure(width=window_width, height=window_height)

        def resize_content(event):
            width = event.width
            height = event.height
            content_frame.configure(width=width, height=height)

        self.root.bind("<Configure>", resize_content)

        self.update_time()

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

    def handle_option(self, option):
        if option == 0:
            self.add_contact()
        elif option == 1:
            self.edit_contact()
        elif option == 2:
            self.delete_contact()
        elif option == 3:
            self.view_contacts()
        elif option == 4:
            self.search_contacts()
        elif option == 5:
            self.root.destroy()

    def add_contact(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Contact")
        add_window.geometry("300x200")
        add_window.config(bg="#e5e5e5")

        def validate_numeric_input(new_value):
            if new_value.isdigit() or new_value == "":
                return True
            return False

        def validate_contact():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            address = address_entry.get()
            contact_number = contact_number_entry.get()

            if not first_name or not last_name or not address or not contact_number:
                messagebox.showerror("Error", "Please fill in all fields.")
            elif not contact_number.isdigit():
                messagebox.showerror("Error", "Contact number should only contain digits.")
            else:
                full_name = f"{first_name} {last_name}"
                contact = Contact(full_name, contact_number, address)
                self.address_book.add_contact(contact)
                messagebox.showinfo("Success", "Contact added successfully.")
                add_window.destroy()
                self.update_contact_count()

        first_name_label = tk.Label(add_window, text="First Name:", bg="#e5e5e5")
        first_name_label.pack()
        first_name_entry = tk.Entry(add_window)
        first_name_entry.pack()

        last_name_label = tk.Label(add_window, text="Last Name:", bg="#e5e5e5")
        last_name_label.pack()
        last_name_entry = tk.Entry(add_window)
        last_name_entry.pack()

        address_label = tk.Label(add_window, text="Address:", bg="#e5e5e5")
        address_label.pack()
        address_entry = tk.Entry(add_window)
        address_entry.pack()

        contact_number_label = tk.Label(add_window, text="Contact Number:", bg="#e5e5e5")
        contact_number_label.pack()

        validate_cmd = (add_window.register(validate_numeric_input), "%P")
        contact_number_entry = tk.Entry(add_window, validate="key", validatecommand=validate_cmd)
        contact_number_entry.pack()

        add_btn = tk.Button(add_window, text="Add", width=10, command=validate_contact)
        add_btn.pack(pady=10)


    def validate_contact(self, first_name, last_name, address, contact_number, window):
        if not first_name or not last_name or not address or not contact_number:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            full_name = f"{first_name} {last_name}"
            contact = Contact(full_name, contact_number, address)
            self.address_book.add_contact(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
            window.destroy()
            self.update_contact_count()

    def update_contact_count(self):
        contact_count = len(self.address_book.contacts)
        self.contact_count_label.config(text=f"Contacts saved: {contact_count}")

    def edit_contact(self):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Contact")
        edit_window.geometry("300x250")
        edit_window.config(bg="#e5e5e5")

        if len(self.address_book.contacts) == 0:
            messagebox.showinfo("Info", "No contacts available.")
            edit_window.destroy()
            return

        select_label = tk.Label(edit_window, text="Select Contact:", bg="#e5e5e5")
        select_label.pack()

        selected_var = tk.StringVar()
        selected_var.set(self.address_book.contacts[0].name)
        select_menu = tk.OptionMenu(edit_window, selected_var, *[contact.name for contact in self.address_book.contacts])
        select_menu.pack(pady=5)

        first_name_label = tk.Label(edit_window, text="First Name:", bg="#e5e5e5")
        first_name_label.pack()
        first_name_entry = tk.Entry(edit_window)
        first_name_entry.pack()

        last_name_label = tk.Label(edit_window, text="Last Name:", bg="#e5e5e5")
        last_name_label.pack()
        last_name_entry = tk.Entry(edit_window)
        last_name_entry.pack()

        address_label = tk.Label(edit_window, text="Address:", bg="#e5e5e5")
        address_label.pack()
        address_entry = tk.Entry(edit_window)
        address_entry.pack()

        contact_number_label = tk.Label(edit_window, text="Contact Number:", bg="#e5e5e5")
        contact_number_label.pack()
        contact_number_entry = tk.Entry(edit_window)
        contact_number_entry.pack()

        selected_var.trace("w", lambda *args: self.set_initial_values(first_name_entry, last_name_entry, address_entry,
                                                                     contact_number_entry, selected_var.get()))

        update_btn = tk.Button(edit_window, text="Update", width=10,
                               command=lambda: self.validate_update(first_name_entry.get(), last_name_entry.get(),
                                                                    address_entry.get(), contact_number_entry.get(),
                                                                    selected_var.get(), edit_window))
        update_btn.pack(pady=10)

    def set_initial_values(self, first_name_entry, last_name_entry, address_entry, contact_number_entry,
                           selected_contact):
        for contact in self.address_book.contacts:
            if contact.name == selected_contact:
                first_name, last_name = contact.name.split()
                first_name_entry.delete(0, tk.END)
                first_name_entry.insert(0, first_name)
                last_name_entry.delete(0, tk.END)
                last_name_entry.insert(0, last_name)
                address_entry.delete(0, tk.END)
                address_entry.insert(0, contact.email)
                contact_number_entry.delete(0, tk.END)
                contact_number_entry.insert(0, contact.phone)
                break

    def validate_update(self, first_name, last_name, address, contact_number, selected_contact, window):
        if not first_name or not last_name or not address or not contact_number:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            full_name = f"{first_name} {last_name}"
            contact = Contact(full_name, contact_number, address)
            self.address_book.edit_contact(
                self.address_book.contacts.index(next(c for c in self.address_book.contacts if c.name == selected_contact)),
                contact)
            messagebox.showinfo("Success", "Contact updated successfully.")
            window.destroy()

    def delete_contact(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Contact")
        delete_window.geometry("300x150")
        delete_window.config(bg="#e5e5e5")

        if len(self.address_book.contacts) == 0:
            messagebox.showinfo("Info", "No contacts available.")
            delete_window.destroy()
            return

        select_label = tk.Label(delete_window, text="Select Contact:", bg="#e5e5e5")
        select_label.pack()

        selected_var = tk.StringVar()
        selected_var.set(self.address_book.contacts[0].name)
        select_menu = tk.OptionMenu(delete_window, selected_var, *[contact.name for contact in self.address_book.contacts])
        select_menu.pack(pady=5)

        delete_btn = tk.Button(delete_window, text="Delete", width=10,
                               command=lambda: self.confirm_delete(selected_var.get(), delete_window))
        delete_btn.pack(pady=10)

        self.update_contact_count()

    def confirm_delete(self, selected_contact, window):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this contact?")
        if confirm:
            self.address_book.delete_contact(
                self.address_book.contacts.index(next(c for c in self.address_book.contacts if c.name == selected_contact)))
            messagebox.showinfo("Success", "Contact deleted successfully.")
            self.update_contact_count()
        window.destroy()

    def view_contacts(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Contacts")
        view_window.geometry("400x300")
        view_window.config(bg="#e5e5e5")

        contacts_text = tk.Text(view_window, bg="white", fg="black")
        contacts_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for idx, contact in enumerate(self.address_book.contacts, start=1):
            contacts_text.insert(tk.END, f"Entry {idx}\n")
            contacts_text.insert(tk.END, f"Name: {contact.name}\n")
            contacts_text.insert(tk.END, f"Phone: {contact.phone}\n")
            contacts_text.insert(tk.END, f"Address: {contact.email}\n")
            contacts_text.insert(tk.END, "\n")

        contacts_text.config(state=tk.DISABLED)

    def search_contacts(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Address Book")
        search_window.geometry("300x200")
        search_window.config(bg="#e5e5e5")

        search_options = ["First Name", "Last Name", "Address", "Contact Number"]

        search_var = tk.StringVar()
        search_var.set(search_options[0])

        search_option_menu = tk.OptionMenu(search_window, search_var, *search_options)
        search_option_menu.pack(pady=5)

        search_label = tk.Label(search_window, text="Enter search query:", bg="#e5e5e5")
        search_label.pack()
        search_entry = tk.Entry(search_window)
        search_entry.pack(pady=5)

        search_btn = tk.Button(search_window, text="Search", width=10,
                               command=lambda: self.display_search_results(search_var.get(), search_entry.get(),
                                                                           search_window))
        search_btn.pack(pady=10)

    def display_search_results(self, search_option, query, window):
        if not query:
            messagebox.showerror("Error", "Please enter a search query.")
            return

        results = []
        for contact in self.address_book.contacts:
            if search_option == "First Name" and query.lower() in contact.name.split()[0].lower():
                results.append(contact)
            elif search_option == "Last Name" and query.lower() in contact.name.split()[-1].lower():
                results.append(contact)
            elif search_option == "Address" and query.lower() in contact.email.lower():
                results.append(contact)
            elif search_option == "Contact Number" and query in contact.phone:
                results.append(contact)

        if not results:
            messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            results_window = tk.Toplevel(self.root)
            results_window.title("Search Results")
            results_window.geometry("400x300")
            results_window.config(bg="#e5e5e5")

            results_text = tk.Text(results_window, bg="white", fg="black")
            results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            for idx, result in enumerate(results, start=1):
                results_text.insert(tk.END, f"Result {idx}\n")
                results_text.insert(tk.END, f"Name: {result.name}\n")
                results_text.insert(tk.END, f"Phone: {result.phone}\n")
                results_text.insert(tk.END, f"Address: {result.email}\n")
                results_text.insert(tk.END, "\n")

            results_text.config(state=tk.DISABLED)

        window.destroy()

    def save_address_book(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.address_book.save_to_csv(file_path)

    def load_address_book(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.address_book.load_from_csv(file_path)

    def toggle_night_mode(self):
        if self.night_mode:
            self.night_mode = False
            self.night_mode_btn.config(text="Night Mode", bg="#BB86FC", fg="black")
            self.root.config(bg="#d9b99b")
            self.set_light_mode_colors()
        else:
            self.night_mode = True
            self.night_mode_btn.config(text="Day Mode", bg="#BB86FC", fg="black")
            self.root.config(bg="#212121")
            self.set_dark_mode_colors()

    def set_light_mode_colors(self):
        colors = {
            "bg": "#d9b99b",
            "fg": "black",
            "title_bg": "#a67a5b",
            "menu_bg": "#a67a5b",
            "btn_bg": "#614e55",
            "btn_fg": "white",
            "night_mode_btn_bg": "#BB86FC",
            "night_mode_btn_fg": "black",
            "save_btn_bg": "#757575",
            "save_btn_fg": "white",
            "load_btn_bg": "#757575",
            "load_btn_fg": "white"
        }
        self.apply_colors(colors)

    def set_dark_mode_colors(self):
        colors = {
            "bg": "#212121",
            "fg": "white",
            "title_bg": "#424242",
            "menu_bg": "#303030",
            "btn_bg": "#757575",
            "btn_fg": "white",
            "night_mode_btn_bg": "#BB86FC",
            "night_mode_btn_fg": "black",
            "save_btn_bg": "#757575",
            "save_btn_fg": "white",
            "load_btn_bg": "#757575",
            "load_btn_fg": "white"
        }
        self.apply_colors(colors)

    def apply_colors(self, colors):
        self.root.config(bg=colors["bg"])
        for widget in self.root.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button)):
                if widget["text"] in ["Address Book", "What would you like to do"]:
                    widget.configure(bg=colors["title_bg"], fg=colors["fg"])
                elif widget["text"] == "Save":
                    widget.configure(bg=colors["save_btn_bg"], fg=colors["save_btn_fg"])
                elif widget["text"] == "Load":
                    widget.configure(bg=colors["load_btn_bg"], fg=colors["load_btn_fg"])
                else:
                    widget.configure(bg=colors["menu_bg"], fg=colors["fg"])

    def run(self):
        window_width = 800  # Desired window width
        window_height = 600  # Desired window height
        position_right = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.root.winfo_screenheight() / 2 - window_height / 2)

        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
        self.root.mainloop()



root = tk.Tk()
app = AddressBookGUI(root)
app.run()

