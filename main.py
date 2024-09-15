from tkinter import *
import requests


def get_quote():
    """Fetches a random Kanye West quote from the Kanye REST API."""
    resoponse = requests.get(url="https://api.kanye.rest")
    resoponse.raise_for_status()
    data = resoponse.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=380)
background_img = PhotoImage(file="img/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="img/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
