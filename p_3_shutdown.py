from tkinter import *
import os

shutDown = Tk()
shutDown.title("ShutDown Application")
shutDown.geometry("500x500")
shutDown.config(bg="pink")

def restart():
    os.system("shutdown /r /t 1")

    
def logout():
    os.system("shutdown -l")
    

r_button = Button(shutDown, text="Restart", font=("Time New Roman", 15, "bold"),relief=RAISED,  borderwidth=10, command=restart)
r_button.place(x=200, y=50, width=120, height=120)


log_button = Button(shutDown, text="Logout", font=("Time New Roman", 15, "bold"),relief=RAISED,  borderwidth=10, command=logout)
log_button.place(x=200, y=180, width=120, height=120)


# s_button = Button(shutDown, text="Logout", font=("Time New Roman", 15, "bold"),relief=RAISED,  borderwidth=10, command=shutDown)
# s_button.place(x=200, y=180, width=120, height=120)







shutDown.mainloop()