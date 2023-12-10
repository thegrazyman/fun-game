import tkinter as tk
from tkinter import messagebox
import base64
import pyautogui
import time

def create_new_window(image_data):
    new_window = tk.Tk()
    new_window.geometry("500x100")

    text_label = tk.Label(new_window, text="this is the moment you realize your pc is gonna shutdown")
    text_label.pack()


def get_embedded_image():
    # Replace 'path/to/your/image.png' with the actual path to your image
    image_path = "C:/Users/Thijmen/OneDrive/Bureaublad/scripts/cookie.png"

    # Open the image file
    with open(image_path, 'rb') as f:
        # Convert the image data to base64
        encoded_image = base64.b64encode(f.read()).decode('utf-8')

    return encoded_image

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        main()

def shutdown():
    pyautogui.press("win")
    pyautogui.typewrite("cmd")
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.typewrite("shutdown /s /a")   #command you wanna use
    time.sleep(0.05)
    pyautogui.press("enter")

def delayed_shutdown():
    # Get the image data
    image_data = get_embedded_image()

    # Create a new window immediately with the image
    create_new_window(image_data)

    # Schedule the shutdown function to be called after 5 seconds
    window.after(5000, shutdown)

def main():
    # Create the main window
    global window
    window = tk.Tk()

    # Set the title of the window
    window.title("Clicker game")

    # Decode the base64 image data
    image_data = get_embedded_image()

    # Create a PhotoImage object from the base64 data
    img = tk.PhotoImage(data=image_data)

    # sets the size of the window
    window.geometry("400x300")

    # button that executes code
    tk.Button(window, text="Click me", command=delayed_shutdown).pack()

    # Create a label to display the image
    image_label = tk.Label(window, image=img)
    image_label.image = img  # Keep a reference to the image
    image_label.pack()  # Use pack to place the label in the window

    # Add other widgets or functionality here if needed

    # Bind the closing event to the on_closing function
    window.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the main loop
    window.mainloop()

if __name__ == "__main__":
    main()
