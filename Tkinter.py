import tkinter as tk
import Matrix
import Logic

base = tk.Tk()

def keyDetector(event):
    if(event.keysym == 'a'):
        Logic.moveLeft()
        update()
    elif(event.keysym == 'd'):
        Logic.moveRight()
        update()
    elif(event.keysym == 's'):
        Logic.moveDown()
        update()

def update():
    mainscreen.config(text=Matrix.display())

base.title("Tetris")
base.configure(bg='black')
base.geometry("1000x600")
base.resizable(True, True)

font = tk.font.Font(family = "Courier", size = 20, weight = "bold")

mainscreen = tk.Label(base, text = Matrix.display(), bg = "black", fg = "green", font = font) 
mainscreen.pack()

Logic.spawn(Logic.blockSelector())
mainscreen.config(text=Matrix.display())
while True:
    base.bind("<KeyPress>", keyDetector)
    base.mainloop()