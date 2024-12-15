import tkinter as tk
import tkinter.font as font
import Logic


def update():
    mainScreen.config(text=Logic.matrixForDisplay.display())


def keyDetector(event):
    if event.keysym == 'a':
        Logic.moveLeft()

    elif event.keysym == 'd':
        Logic.moveRight()

    elif event.keysym == 's':
        Logic.moveDown()

    elif event.keysym == 'q':
        Logic.rotateLeft()

    elif event.keysym == 'e':
        Logic.rotateRight()

    update()


base = tk.Tk()

base.title("Tetris")
base.configure(bg='black')
base.geometry("1000x600")
base.resizable(True, True)

font = font.Font(family="Courier", size=20, weight="bold")

mainScreen = tk.Label(base, text=Logic.matrixForDisplay.display(), bg="black", fg="green", font=font)

mainScreen.pack(expand=True, fill="both")

Logic.spawn(Logic.blockSelector())
mainScreen.config(text=Logic.matrixForDisplay.display())

base.bind("<KeyPress>", keyDetector)
base.mainloop()