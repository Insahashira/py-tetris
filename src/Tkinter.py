import tkinter as tk
import tkinter.font as font
import Logic


def update():

    nextBlock.config(text = Logic.next_screen_display())
    mainScreen.config(text = Logic.display())
    auxScreen.config(text = Logic.aux_screen_display())
    Logic.time_measure()
    base.after(16, update)

def key_detector(event):

    if event.keysym == 'w' or event.keysym == "space":
        Logic.drop()

    elif event.keysym == 'a':
        Logic.moveLeft()

    elif event.keysym == 's':
        Logic.moveDown()

    elif event.keysym == 'd':
        Logic.moveRight()

    elif event.keysym == 'q':
        Logic.rotateLeft()

    elif event.keysym == 'e':
        Logic.rotateRight()

    elif event.keysym == "Tab":
        Logic.flip()

    elif event.keysym == "Shift_L":
        Logic.save_block()


def font_change(event = None):
    new_font = font.Font(family = "Courier", size = int(base.winfo_width()/50), weight = "bold")
    mainScreen.config(font = new_font)
    auxScreen.config(font = new_font)
    nextBlock.config(font = new_font)

base = tk.Tk()

base.title("Pytris")
base.configure(bg='black')
base.geometry("1000x600")
base.resizable(True, True)

gui_font = font.Font(family="Courier", size=20, weight="bold")

Logic.spawner()

mainPlate = tk.Frame(base, bg = "Black")
mainPlate.place(relx = 0.5, rely = 0.5, anchor = "center")

mainScreen = tk.Label(mainPlate, text=Logic.display(), bg ="black", fg ="green", font = gui_font)
auxScreen = tk.Label(mainPlate, text = " ", bg = "black", fg = "green", font = gui_font)
nextBlock = tk.Label(mainPlate, text = Logic.next_screen_display(), bg ="black", fg ="green", font = gui_font)

mainScreen.grid(row = 1, column = 2)
auxScreen.grid(row = 1, column = 1)
nextBlock.grid(row = 1, column = 3)

Logic.time_start()
Logic.time_measure()

base.bind("<KeyPress>", key_detector)
base.bind("<Configure>", font_change)

update()
base.mainloop()
