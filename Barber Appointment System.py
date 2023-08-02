import tkinter as tk
import webbrowser

def submit_name():
    global username
    username = name_entry.get()
    name_entry.delete(0, tk.END)  # Clear the entry field
    show_main_page()

def visit_linkedin():
    webbrowser.open("https://www.linkedin.com/in/zafran-haider-9755b8187/")

def show_main_page():
    first_page.destroy()
    global main_page
    main_page = tk.Tk()
    main_page.title("Barber Appointment System")
    main_page.geometry("400x300")
    main_page.configure(bg="blue")

    welcome_label = tk.Label(main_page, text=f"Hello, {username}!", bg="blue", fg="white")
    welcome_label.pack(pady=20)

    options_label = tk.Label(main_page, text="Here are the options. Which type of cut do you want?", bg="blue", fg="white")
    options_label.pack(pady=10)

    fade_button = tk.Button(main_page, text="Fade Cut", bg="green", command=lambda: select_cut("Fade Cut"))
    fade_button.pack(pady=5)

    buzz_button = tk.Button(main_page, text="Buzz Cut", bg="green", command=lambda: select_cut("Buzz Cut"))
    buzz_button.pack(pady=5)

    undercut_button = tk.Button(main_page, text="UnderCut", bg="green", command=lambda: select_cut("UnderCut"))
    undercut_button.pack(pady=5)

    crew_cut_button = tk.Button(main_page, text="Crew Cut", bg="green", command=lambda: select_cut("Crew Cut"))
    crew_cut_button.pack(pady=5)

    temple_cut_button = tk.Button(main_page, text="Temple Cut", bg="green", command=lambda: select_cut("Temple Cut"))
    temple_cut_button.pack(pady=5)

    exit_button = tk.Button(main_page, text="Exit", bg="green", command=main_page.quit)
    exit_button.pack(pady=10)

def select_cut(cut_type):
    main_page.destroy()
    appointment_page(cut_type)

def appointment_page(cut_type):
    appointment_page = tk.Tk()
    appointment_page.title("Barber Appointment System")
    appointment_page.geometry("400x300")
    appointment_page.configure(bg="blue")

    day_label = tk.Label(appointment_page, text="Enter Day:", bg="blue", fg="white")
    day_label.pack(pady=10)

    day_entry = tk.Entry(appointment_page)
    day_entry.pack(pady=5)

    time_label = tk.Label(appointment_page, text="Enter Time:", bg="blue", fg="white")
    time_label.pack(pady=10)

    time_entry = tk.Entry(appointment_page)
    time_entry.pack(pady=5)

    submit_button = tk.Button(appointment_page, text="Submit", bg="green", command=lambda: appointment_confirmation(cut_type, day_entry.get(), time_entry.get()))
    submit_button.pack(pady=20)

def appointment_confirmation(cut_type, day, time):
    confirmation_page = tk.Toplevel()
    confirmation_page.title("Barber Appointment System")
    confirmation_page.geometry("1280x720")
    confirmation_page.configure(bg="blue")

    confirmation_label = tk.Label(confirmation_page, text=f"Barber appointed successfully! Please visit nearest Usman Barber Shop on {day} at {time}. Thank you.", bg="blue", fg="white")
    confirmation_label.pack(pady=100)

    created_by_label = tk.Label(confirmation_page, text="Created and Tested By Zafran Haider", bg="blue", fg="white")
    created_by_label.pack(side="bottom")

    linkedin_button = tk.Button(confirmation_page, text="Visit My LinkedIn", bg="green", command=visit_linkedin)
    linkedin_button.pack(side="left", padx=20, pady=10)

    confirmation_page.mainloop()


# First Page
first_page = tk.Tk()
first_page.title("Barber Appointment System")
first_page.geometry("400x300")
first_page.configure(bg="blue")

logo_label = tk.Label(first_page, text="Created And Tested By Zafran Haider", bg="blue", fg="white")
logo_label.pack(side="bottom")

name_label = tk.Label(first_page, text="Enter Name:", bg="blue", fg="white")
name_label.pack(pady=10)

name_entry = tk.Entry(first_page)
name_entry.pack(pady=5)

submit_button = tk.Button(first_page, text="Submit", bg="green", command=submit_name)
submit_button.pack(pady=20)

# Start the main loop
first_page.mainloop()
