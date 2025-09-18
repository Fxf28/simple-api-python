# A simple Tkinter app that fetches and displays random Kanye West quotes.

# Import necessary libraries
from tkinter import *
from tkinter import messagebox
import requests

# Function to fetch and display a new quote
def get_quote():
    try:
        response = requests.get("https://api.kanye.rest/", timeout=5)
        response.raise_for_status()
        data = response.json()
        quote = data["quote"]
        canvas.itemconfig(quote_text, text=quote)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request Error", f"Could not fetch quote.\n\n{e}")

# Set up the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Set up the canvas with background and text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white"
)
canvas.grid(row=0, column=0)

# Set up the button to get a new quote
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Start the Tkinter event loop
window.mainloop()
