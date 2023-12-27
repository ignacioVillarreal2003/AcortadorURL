import requests
from tkinter import *
from tkinter import messagebox as MessageBox
import pyperclip

def shorten_url_isgd():
    originalURL = original_url.get()
    customName = custom_name.get()
    print(originalURL)
    print(customName)
    base_url = "https://is.gd/create.php"
    params = {
        "format": "json",
        "url": originalURL,
        "shorturl": customName
    }
    response = requests.get(base_url, params=params)
    response_data = response.json()
    if 'shorturl' in response_data:
        shorten_url = response_data['shorturl']
        resultado.set(shorten_url)
        pyperclip.copy(shorten_url)
        print(shorten_url)
        MessageBox.showinfo("Éxito", "La URL corta se ha copiado al portapapeles.")
    else:
        resultado.set("Error, pruebe de nuevo, con otro nombre.")

root = Tk()
ancho = 500
alto = 300
root.geometry(f"{ancho}x{alto}")
root.config(bd=50)
root.title('Acorta urls.')

label_original_url = Label(root, text="URL original")
label_original_url.grid(row=1, column=0, pady=(0, 20))
original_url = Entry(root, width=30, font=("Helvetica", 12))
original_url.grid(row=1, column=1, pady=(0, 20))

label_custom_name = Label(root, text="Nombre de la URL")
label_custom_name.grid(row=2, column=0, pady=(0, 20))
custom_name = Entry(root, width=30, font=("Helvetica", 12))
custom_name.grid(row=2, column=1, pady=(0, 20))

boton = Button(root, text='Convertir', command=shorten_url_isgd)
boton.grid(row=3, column=1)

resultado = StringVar()
result = Label(root, textvariable=resultado, font=("Helvetica", 12))
result.grid(row=4, column=1, pady=(20, 20))

root.mainloop()


