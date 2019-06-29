from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import webbrowser

def main_screen():
    # Set global variable as screen
    global screen
    screen = Tk()
    # Icon
    screen.iconbitmap(default="logo.ico")
    # Title
    screen.title("Hubox configurator")
    # Background color
    screen.configure(background='white')
    # Set width and height of screen
    w = 500
    h = 300
    # Get screen width and height
    ws = screen.winfo_screenwidth()
    hs = screen.winfo_screenheight()
    # Calculate position x, y to place screen in center
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2) - 30
    screen.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Logo
    image = PhotoImage(file='logo.png')
    image = image.subsample(2, 2)
    label = Label(screen, image=image, background="white")
    label.place(x=165, y=40)

    # Intro text (top)
    intro = Label(screen, text="Welcome to the Hubox configurator", font=("Arial", 11), background='white')
    intro.place(x=133, y=27)

    # Info text (bottom)
    info = Label(screen, text="Click on Start to begin the configuration of your Hubox", font=("Arial", 11), background='white')
    info.place(x=71, y=180)

    # Start button
    ttk.Style().configure("TButton", background="blue", foreground="blue")
    button = Button(screen, text="Start", width="12", command=second_screen)
    button.place(x=206, y=225)

    # Display main screen with contents
    screen.mainloop()


def second_screen():
    # Destroy previous screen
    screen.destroy()

    # Set global variable as screen
    screen1 = Tk()
    # Icon
    screen1.iconbitmap(default="logo.ico")
    # Title
    screen1.title("Hubox configurator")
    # Background color
    screen1.configure(background='white')
    # Set width and height of screen
    w = 500
    h = 300
    # Get screen width and height
    ws = screen1.winfo_screenwidth()
    hs = screen1.winfo_screenheight()
    # Calculate position x, y to place screen in center
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2) - 30
    screen1.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Intro text (top)
    intro = Label(screen1, text="Please enter your Wi-Fi credentials", font=("Arial", 11), background='white')
    intro.place(x=133, y=27)

    # Wi-Fi SSID
    ssid_label = Label(screen1, text="Wi-Fi SSID (Username):", background='white')
    ssid_label.place(x=140, y=80)
    ssid_var = StringVar()
    ssid_textbox = Entry(screen1, width="35", textvariable=ssid_var)
    ssid_textbox.place(x=140, y=103)

    # Wi-Fi password
    password_label = Label(screen1, text="Wi-Fi Password:", background='white')
    password_label.place(x=140, y=132)
    password_var = StringVar()
    password_textbox = Entry(screen1, width="35", textvariable=password_var)
    password_textbox.place(x=140, y=155)

    # Register function
    def register():
        # Get Wi-Fi SSID and password from textbox
        ssid = str(ssid_var.get())
        password = str(password_var.get())

        # Ensure fields are not empty
        if len(ssid) == 0 or len(password) == 0:
            messagebox.showerror("Error", "Fields cannot be empty!", parent=screen1)
        else:
            # Read settings.ini file and fetch every line in lines list
            with open("settings.ini", "r") as f:
                lines = f.readlines()

            # Write settings.ini with Wi-Fi SSID and password
            with open("settings.ini", "w") as f:
                for line in lines:
                    if line.startswith("wifi_network = "):
                        f.write(f"wifi_network = {ssid}\n")
                    elif line.startswith("wifi_password = "):
                        f.write(f"wifi_password = {password}\n")
                    else:
                        f.write(line)

            # Display success message and close the application
            messagebox.showinfo("Success", "Wi-Fi credentials added!", parent=screen1)
            screen1.destroy()

    # Submit button
    ttk.Style().configure("TButton", background="blue", foreground="blue")
    button = Button(screen1, text="Submit", width="12", command=register)
    button.place(x=206, y=190)

    # Info text (bottom)
    info = Label(screen1, text="All other settings can be edited from your phone", font=("Arial", 9), background='white')
    info.place(x = 117, y = 230)
    info1 = Label(screen1, text="or computer. For help, visit ", font=("Arial", 9), background='white')
    info1.place(x = 138, y = 245)

    # URL
    def callback(url):
        webbrowser.open_new(url)
    info2 = Label(screen1, text="bit.ly/hubox1", cursor="hand2", font=("Arial", 9, "underline"), background='white')
    info2.place(x = 285, y = 245)
    info2.bind("<Button-1>", lambda e: callback("bit.ly/hubox1"))

    # Display main screen with contents
    screen1.mainloop()

if __name__ == "__main__":
    main_screen()
