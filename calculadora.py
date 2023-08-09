from tkinter import *
from tkinter import ttk

# cores
greyColor = "#1b1c1c"
whiteColor = "#ffffff"
blueColor = "#2a336e"
redColor = "#cc6666"
orangeColor = "#d18b45"


# inicializando a janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("400x600")
janela.config(bg=greyColor)

# criando os frames
frameTela = Frame(janela, width=400, height=150, bg=blueColor)
frameTela.grid(row=0, column=0)

frameCorpo = Frame(janela, width=400, height=450, bg=whiteColor)
frameCorpo.grid(row=1, column=0)

# criando funções
textoDisplay = ""


def entryValue(value):
    
    global textoDisplay

    textoDisplay += str(value)

    exibirNaTela.set(textoDisplay)

def calculate():
    resultado = eval(textoDisplay)
    exibirNaTela.set(resultado)

def clear():
    global textoDisplay
    textoDisplay = ""
    exibirNaTela.set(textoDisplay)


# exibirNaTela.set(resultado)


# criando label

exibirNaTela = StringVar()

labelResultado = Label(
    frameTela,
    textvariable=exibirNaTela,
    width=19,
    height=4,
    anchor="e",
    relief=FLAT,
    justify=RIGHT,
    font="Ivy 25 bold",
    bg=blueColor,
    fg=whiteColor,
    padx=10,
)
labelResultado.place(x=0, y=0)


# criando os botões
buttonClear = Button(
    frameCorpo,
    command=lambda: clear(),
    bg=redColor,
    text="C",
    width=19,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
    
)
buttonClear.place(x=0, y=0)

buttonPercentage = Button(
    frameCorpo,
    command=lambda: entryValue("%"),
    text="%",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonPercentage.place(x=200, y=0)

buttonDivision = Button(
    frameCorpo,
    command=lambda: entryValue("/"),
    text="/",
    width=9,
    height=4,
    bg=orangeColor,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonDivision.place(x=300, y=0)

buttonNumber7 = Button(
    frameCorpo,
    command=lambda: entryValue("7"),
    text="7",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonNumber7.place(x=1, y=90)

buttonNumber8 = Button(
    frameCorpo,
    command=lambda: entryValue("8"),
    text="8",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonNumber8.place(x=100, y=90)

buttonNumber9 = Button(
    frameCorpo,
    command=lambda: entryValue("9"),
    text="9",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonNumber9.place(x=200, y=90)

buttonMultiplication = Button(
    frameCorpo,
    command=lambda: entryValue("*"),
    text="*",
    width=9,
    height=4,
    bg=orangeColor,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonMultiplication.place(x=300, y=90)

buttonNumber4 = Button(
    frameCorpo,
    command=lambda: entryValue("4"),
    text="4",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonNumber4.place(x=1, y=180)

buttonNumber5 = Button(
    frameCorpo,
    command=lambda: entryValue("5"),
    text="5",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonNumber5.place(x=100, y=180)

buttonNumber6 = Button(
    frameCorpo,
    command=lambda: entryValue("6"),
    text="6",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonNumber6.place(x=200, y=180)

buttonSubtraction = Button(
    frameCorpo,
    command=lambda: entryValue("-"),
    text="-",
    width=9,
    height=4,
    bg=orangeColor,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonSubtraction.place(x=300, y=180)

buttonNumber1 = Button(
    frameCorpo,
    command=lambda: entryValue("1"),
    text="1",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonNumber1.place(x=1, y=270)

buttonNumber2 = Button(
    frameCorpo,
    command=lambda: entryValue("2"),
    text="2",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonNumber2.place(x=100, y=270)

buttonNumber3 = Button(
    frameCorpo,
    command=lambda: entryValue("3"),
    text="3",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonNumber3.place(x=200, y=270)

buttonAddition = Button(
    frameCorpo,
    command=lambda: entryValue("+"),
    text="+",
    width=9,
    height=4,
    bg=orangeColor,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonAddition.place(x=300, y=270)

buttonNumber0 = Button(
    frameCorpo,
    command=lambda: entryValue("0"),
    text="0",
    width=19,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonNumber0.place(x=1, y=360)

buttonDot = Button(
    frameCorpo,
    command=lambda: entryValue("."),
    text=".",
    width=9,
    height=4,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonDot.place(x=200, y=360)

buttonEquals = Button(
    frameCorpo,
    command=lambda: calculate(),
    text="=",
    width=9,
    height=4,
    bg=orangeColor,
    font="Ivy 13 bold",
    relief=RAISED,
    overrelief=RIDGE,
)
buttonEquals.place(x=300, y=360)


janela.mainloop()
