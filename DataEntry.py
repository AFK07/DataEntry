import tkinter
from tkinter import ttk  # means themed tkinter
from tkinter import messagebox
import sqlite3

# Function to check inputs and update button color
def check_inputs():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    title = title_combobox.get()
    nationality = nationality_combobox.get()
    accepted = accept_var.get()

    # Check if required fields are filled
    if firstname and lastname and title and nationality and accepted == "Accepted":
        button.config(bg="green")  # Change button to green if all inputs are valid
    else:
        button.config(bg="red")  # Change button to red if inputs are invalid

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            registered_status = "Registered" if reg_status_var.get() else "Not Registered"
            course = completed_spinbox.get()
            semester = num_semester_spinbox.get()

            print("Title: ", title, "First name: ", firstname, "Last name: ", lastname)
            print("Age: ", age, "Nationality: ", nationality)
            print("Courses: ", course, "Semesters: ", semester)
            print("------------------------------------------")
        
            # Make connection with sqlite3
            conn = sqlite3.connect('data.db')  # .db means like .py

            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data
                        (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT,
                        registration_status TEXT, course INT, semester INT)
            '''
            conn.execute(table_create_query)

            data_insert_query = '''INSERT INTO Student_Data 
            (firstname, lastname, title, age, nationality, registration_status, course, semester) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, title, age, nationality, registered_status, course, semester)
            cursor = conn.cursor()  # processes between the sqlite and database. exe queries and inserts.
            cursor.execute(data_insert_query, data_insert_tuple)  # exe query and puts the tuples 
            conn.commit()  # important
            conn.close()  # create and close
            reset_form()  # Call reset_form after entering data
        else:
            messagebox.showwarning(title="Error", message="First name and last name required.")
    else:
        messagebox.showwarning(title="Error", message="You have not accepted the terms.")

# Function to reset all form fields
def reset_form():
    first_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    title_combobox.set('')  # Reset the title combobox
    age_spinbox.delete(0, 'end')  # You may also want to reset to a default value
    age_spinbox.insert(0, 18)  # Resets the age to 18
    nationality_combobox.set('')  # Reset the nationality combobox
    reg_status_var.set(False)  # Reset the registration status
    completed_spinbox.delete(0, 'end')
    completed_spinbox.insert(0, 0)  # Reset the completed courses to 0
    num_semester_spinbox.delete(0, 'end')
    num_semester_spinbox.insert(0, 0)  # Reset the semester count to 0
    accept_var.set("Not Accepted")  # Reset terms and conditions check
    check_inputs()  # Recheck inputs after resetting

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# divided the window into 3 frames
# upper for user information
# middle frame for registration details
# lower frame for terms and conditions

# Upper Frame for User Information
upper_frame = tkinter.LabelFrame(frame, text="User Information")
upper_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(upper_frame, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label(upper_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(upper_frame)
first_name_entry.grid(row=1, column=0)
first_name_entry.bind("<KeyRelease>", lambda event: check_inputs())

last_name_entry = tkinter.Entry(upper_frame)
last_name_entry.grid(row=1, column=1)
last_name_entry.bind("<KeyRelease>", lambda event: check_inputs())

title_label = tkinter.Label(upper_frame, text="Title")
title_label.grid(row=0, column=2)
title_combobox = ttk.Combobox(upper_frame, values=["", "Mr.", "Mrs.", "Ms.", "Dr."])
title_combobox.grid(row=1, column=2)
title_combobox.bind("<<ComboboxSelected>>", lambda event: check_inputs())

age_label = tkinter.Label(upper_frame, text="Age")
age_label.grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(upper_frame, from_=18, to=110)
age_spinbox.grid(row=3, column=0)
age_spinbox.bind("<KeyRelease>", lambda event: check_inputs())

nationality_label = tkinter.Label(upper_frame, text="Nationality")
nationality_label.grid(row=2, column=1)
nationality_combobox = ttk.Combobox(upper_frame, values=["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", 
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", 
    "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", 
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", 
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", 
    "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", 
    "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", 
    "Cyprus", "Czech Republic", "Democratic Republic of the Congo", "Denmark", 
    "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", 
    "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", 
    "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", 
    "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", 
    "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", 
    "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", 
    "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", 
    "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", 
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", 
    "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", 
    "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", 
    "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", 
    "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", 
    "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", 
    "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", 
    "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", 
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", 
    "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", 
    "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", 
    "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", 
    "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", 
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", 
    "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", 
    "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"])  # You can populate this later
nationality_combobox.grid(row=3, column=1)
nationality_combobox.bind("<<ComboboxSelected>>", lambda event: check_inputs())

# Middle Frame for Registration Details
middle_frame = tkinter.LabelFrame(frame, text="Registration Details")
middle_frame.grid(row=1, column=0, padx=20, pady=10)

# Change from StringVar to BooleanVar for registration status
reg_status_var = tkinter.BooleanVar(value=False)  # Start with unchecked

reg_status_label = tkinter.Label(middle_frame, text="Registration Status")
reg_status_label.grid(row=0, column=0)

# Create a Checkbutton to toggle registration status
def toggle_registration():
    if reg_status_var.get():
        reg_status_label.config(text="Registered")
    else:
        reg_status_label.config(text="Not Registered")

reg_status_checkbox = tkinter.Checkbutton(
    middle_frame,
    text="Registered",
    variable=reg_status_var,
    command=toggle_registration
)
reg_status_checkbox.grid(row=1, column=0)

completed_label = tkinter.Label(middle_frame, text="Courses Completed")
completed_spinbox = tkinter.Spinbox(middle_frame, from_=0, to=100)
completed_label.grid(row=0, column=1, padx=20, pady=10)
completed_spinbox.grid(row=1, column=1, padx=20, pady=10)

num_semester_label = tkinter.Label(middle_frame, text="Number of Semesters")
num_semester_label.grid(row=0, column=2, padx=20, pady=10)
num_semester_spinbox = tkinter.Spinbox(middle_frame, from_=0, to=10)
num_semester_spinbox.grid(row=1, column=2, padx=20, pady=10)

# Lower Frame for Terms and Conditions
lower_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
lower_frame.grid(row=2, column=0, padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
accept_checkbox = tkinter.Checkbutton(lower_frame, text="I accept the terms and conditions", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted", command=check_inputs)
accept_checkbox.grid(row=0, column=0, sticky="news")

# Confirm Button
button = tkinter.Button(frame, text="Confirm", command=enter_data, bg="red")  # Start with red background
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()

