from tkinter import *
import os 
from PIL import ImageTk, Image
import tkinter as tk

def toggle_microphone():
    # Add your code here to handle microphone control
    # For example, you can start/stop recording audio or enable/disable voice input
    # This part depends on the specific implementation and requirements
    pass

def exit_application():
    # Add your code here to exit the application
    # This can include closing any open resources or windows
    window.destroy()

def send_message():
    message = entry.get()
    display.insert(tk.END, message + "\n", "right")
    entry.delete(0, tk.END)


# Create the main window
window = Tk()
window.title("GUZEL BOT")
window_width = 1340
window_height = 690
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg="#525561")
window.geometry('1340x690')

background_image = Image.open("python\\new\\chatbg.png")
background_image = background_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to hold the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


display = tk.Text(window, height=23, width=70, bg="white", fg="black", wrap=tk.WORD)
# display.pack(pady=10)
display.place(x=600,y=35)


entry = tk.Entry(window, width=50)
# entry.pack(pady=10)

entry.place(x=600,y=500)

# Create a frame to contain the chat frames
# chat_frame = tk.Frame(window, bg="#245c62")
# chat_frame.place(x=300, y=10, width=740, height=300)

# scrollbar = tk.Scrollbar(chat_frame)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# # Load user and bot images
# user_image = ImageTk.PhotoImage(file="python\\new\\user.png")
# bot_image = ImageTk.PhotoImage(file="python\\new\\robot.png")

# entry_image = ImageTk.PhotoImage(file="python\\new\\robot.png")


# # Create an input field for the user to enter messages


# Login_emailName_image_Label = Label(
#         window,
#         borderwidth=0,
#         bg='#A28DCF'
       
#     )
# Login_emailName_image_Label.place(x=590, y=460, width=570, height=60)


# entry= Entry(window, bg='#A28DCF', fg='white', width=6, font=("", 15, "bold"))

# entry.place(x=590, y=460, width=570, height=60)
# entry.bind("<Return>", send_message) 

image = Image.open("python\\new\\send.png")
image = image.resize((50, 50))
photo = ImageTk.PhotoImage(image)

image = Image.open("python\\new\\exit.png")
image = image.resize((50, 50))
photo1 = ImageTk.PhotoImage(image)

image = Image.open("python\\new\\mic.png")
image = image.resize((50, 50))
photo2 = ImageTk.PhotoImage(image)

# Create a send button to trigger the send_message function
send_button = tk.Button(window, image=photo, text="Send", command=send_message, height=50, width=50, bg='#245c62')
send_button.place(x=650, y=520)

# Create a microphone button to trigger the toggle_microphone function
mic_button = tk.Button(window, image=photo2, text="Microphone", command=toggle_microphone, height=50, width=50, bg='#245c62')
mic_button.place(x=450, y=520)

# Create an exit button to trigger the exit_application function
exit_button = tk.Button(window, image=photo1, text="Exit", command=exit_application, height=50, width=50, bg='#245c62')
exit_button.place(x=850, y=520)


display.tag_configure("right", justify="right")
display.tag_configure("left", justify="left")

def receive_message(message):
    box_color = "lightblue"
    display.insert(tk.END, message + "\n")
    display.tag_add("box", "end-2l", "end")
    display.tag_config("box", background=box_color)

    # Scroll to the end of the display
    display.see(tk.END)

# Simulate receiving a message from the bot
receive_message("Hello, how can I assist you?")


# Run the main loop
window.mainloop()
