import tkinter
from tkinter import ttk # means themed tkinter
from tkinter import messagebox


def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            registered_status = reg_status_var.get()
            course = completed_spinbox.get()
            semester = num_semester_spinbox.get()

            
            print("Title: ", title,"First name: ", firstname, "Last name: ", lastname)
            print("Age: ", age, "Nationality: ", nationality)
            print("Courses: ", course, "Semesters: ", semester)
            print("------------------------------------------")
        
            # make connection with sqlite3
            conn = sqlite3.connect('data.db') # .db means like .py

            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data
                        (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT,
                        registration_status TEXT, course INT, semester INT)
            '''
            conn.execute(table_create_query)

            data_insert_query = '''INSERT INTO Student_Data 
            (firstname, lastname, title, age, nationality, registration_status, course, semester) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, title, age, nationality, registered_status, course, semester)
            # why not just write it in the '?', because those are strings and wouldnt be able to access through the variables
            cursor = conn.cursor()  #processess between the sqlite and database. exe queries and inserts.
            cursor.execute(data_insert_query, data_insert_tuple) # exe query and puts the tuples 
            conn.commit()   # imp
            conn.close()        #create and close
        else:
            tkinter.messagebox.showwarning(title="Error", message="first name and last name required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms.")
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()


# Labels and Entries
# Labels: name of the labels
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)
# pad creates gaps around the frames 

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

# Entries: where you type it
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)


title = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Mrs.", "Ms.", "Dr."])
title.grid(row=0, column= 2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)


nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", 
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
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", 
    "United Arab Emirates", "United Kingdom", "United States", "Uruguay", 
    "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", 
    "Zambia", "Zimbabwe"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

# paddings for the widgets
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving course info
course_frame = tkinter.LabelFrame(frame)
course_frame.grid(row=1, column=0, sticky= "news", padx= 20, pady=10)   # sticky="news" means north east west and south, making the gaps on all angles




registered_label = tkinter.Label(course_frame, text="Registrration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")      # if the value is null, the default will remain as ticked

registered_check = tkinter.Checkbutton(course_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")    #won't run if on and off aren't speficied


registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

completed_label = tkinter.Label(course_frame, text="Completed Courses")
completed_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
completed_label.grid(row=0, column=1)
completed_spinbox.grid(row=1, column=1)

num_semester_label = tkinter.Label(course_frame, text="Semesters")
num_semester_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
num_semester_label.grid(row=0, column=2)
num_semester_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# T's & C's
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")        #similar as above
terms_check.grid(row=0, column=0)

button = tkinter.Button(frame, text="Confirm", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
