from tkinter import *
from PIL import Image, ImageTk


def keep_flat(event):
    if event.widget is submit:
        event.widget.config(relief=FLAT, bg="linen")


def conversion():
    try:
        rawData = input.get()
        val = float(input.get())
        # print(val)
        output = val * 0.013
        output_round = round(output, 2)
        display_output.config(
            text=f"₹ {rawData} (Rupees/INR) is equal to $ {output_round} (Dollars/USD)")
    except ValueError:
        display_output.config(
            text="Sorry, Invalid Input !!! Enter the input in Numbers :(")
    except Exception:
        display_output.config(
            text="Oh oh !!! Maybe there is some error at our end. Please try again later :(")


root = Tk()
root.geometry("800x450+350+150")
root.title("USD to INR")
root.iconbitmap(
    r"favicon.ico")
root.config(bg="linen")

header = Label(root, text="INR to USD Converter", font=(
    "Josefin Sans", 21), fg="red", bg="linen")
header.pack(pady=40)


input_label = Label(root, text="Enter the value in INR below:-",
                    bg="linen", font=("Josefin Sans", 8), fg="firebrick1")
input_label.pack()
input = Entry(root, width=25, background="LightPink1",
              fg="navy", relief=FLAT, borderwidth=10)
input.pack()

image = Image.open(
    r"btn.png")
resize_image = image.resize((150, 150))
img = ImageTk.PhotoImage(resize_image)

submit = Button(root, text="Convert", command=conversion,
                relief=FLAT, image=img, bg="linen", activebackground='linen')
submit.pack()

display_output = Label(root, text="Submit to get value in USD",
                       fg="firebrick2", font=("Josefin Sans", 15))
display_output.pack(pady=40)

root.bind('<Button-1>', keep_flat)

root.mainloop()
