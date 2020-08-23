import tkinter as tk
import random
import sys
import os
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

HEIGHT = 600
WIDTH = 600
words = []
lives = 11
with open("dictionary.txt", "r") as file:
  words_unstripped = file.readlines()
  for element in words_unstripped:
    words.append(element.strip().upper())

chosen = random.choice(words)

letters = []
for letter in chosen:
    letters.append(letter)

dictofLetters = {i : letters[i] for i in range (0, len(letters))}
def win():
    message = "YOU WIN!"

    winner = tk.Label(root, font=("Comic Sans Ms", 20), bg="black", fg="white", text=message)
    winner.place(relx=0, rely=0.75, relheight=0.2, relwidth=1)
    againbutton = tk.Button(winner, bg="black", fg="white", text="PLAY\nAGAIN", font=("Comic Sans Ms", 20), command=lambda: restart_program())
    againbutton.place(relx=0,relwidth=0.2, relheight=1)
    exitbutton = tk.Button(winner, bg="black", fg="white", text="EXIT", font=("Comic Sans Ms", 20), command=root.destroy)
    exitbutton.place(relx=0.8,relwidth=0.2, relheight=1)

def lose():
    message = f"YOU LOSE!\n" \
              f"The Word Was\n" \
              f"{chosen}"

    winner = tk.Label(root, font=("Comic Sans Ms", 20), bg="black", fg="white", text=message)
    winner.place(relx=0, rely=0.75, relheight=0.2, relwidth=1)
    againbutton = tk.Button(winner, bg="black", fg="white", text="PLAY\nAGAIN", font=("Comic Sans Ms", 20), command=lambda: restart_program())
    againbutton.place(relx=0,relwidth=0.2, relheight=1)
    exitbutton = tk.Button(winner, bg="black", fg="white", text="EXIT", font=("Comic Sans Ms", 20), command=root.destroy)
    exitbutton.place(relx=0.8,relwidth=0.2, relheight=1)
def get_key(val):
    for key, value in dictofLetters.items():
        if val == value:
            return key

def letter(l):
    global dictofLetters, result_dict, lives, alpha_dict, background_dict
    try:
        key = get_key(l)
        del dictofLetters[key]
        result_dict.get(key)["text"] = l
        if len(dictofLetters) == 0:
            win()

    except:
        alpha_dict.get(l)["bg"] = "red"
        lives -= 1
        background_image["file"] = background_dict.get(lives)
        if lives == 0:
            lose()

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="background_11.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

result0 = tk.Label(root, bg="black", font=("Comic Sans Ms", 20), fg="white")
result0.place(relx=0.11, rely=0.6, relheight=0.09, relwidth=0.09)
result1 = tk.Label(root, bg="black", font=("Comic Sans Ms", 20), fg="white")
result1.place(relx=0.21, rely=0.6, relheight=0.09, relwidth=0.09)
result2 = tk.Label(root, bg="black", font=("Comic Sans Ms", 20), fg="white")
result2.place(relx=0.31, rely=0.6, relheight=0.09, relwidth=0.09)
result3 = tk.Label(root, bg="black", font=("Comic Sans Ms", 20), fg="white")
result3.place(relx=0.41, rely=0.6, relheight=0.09, relwidth=0.09)
result4 = tk.Label(root, bg="black", font=("Comic Sans Ms", 20), fg="white")
result4.place(relx=0.51, rely=0.6, relheight=0.09, relwidth=0.09)
result5 = tk.Label(root, bg="black", font=("Comic Sans Ms", 20), fg="white")
result5.place(relx=0.61, rely=0.6, relheight=0.09, relwidth=0.09)
result6 = tk.Label(root, bg="black", font=("Comic Sans Ms", 20), fg="white")
result6.place(relx=0.71, rely=0.6, relheight=0.09, relwidth=0.09)
result7 = tk.Label(root, bg="black", font=("Comic Sans Ms", 20), fg="white")
result7.place(relx=0.81, rely=0.6, relheight=0.09, relwidth=0.09)
buttonA = tk.Button(root, text="A", font=("Comic Sans Ms", 12), command=lambda: letter("A"))
buttonA.place(relx=0.1, rely=0.8, relheight=0.061, relwidth=0.061)
buttonB = tk.Button(root, text="B", font=("Comic Sans Ms", 12), command=lambda: letter("B"))
buttonB.place(relx=0.162, rely=0.8, relheight=0.061, relwidth=0.061)
buttonC = tk.Button(root, text="C", font=("Comic Sans Ms", 12), command=lambda: letter("C"))
buttonC.place(relx=0.225, rely=0.8, relheight=0.061, relwidth=0.061)
buttonD = tk.Button(root, text="D", font=("Comic Sans Ms", 12), command=lambda: letter("D"))
buttonD.place(relx=0.288, rely=0.8, relheight=0.061, relwidth=0.061)
buttonE = tk.Button(root, text="E", font=("Comic Sans Ms", 12), command=lambda: letter("E"))
buttonE.place(relx=0.351, rely=0.8, relheight=0.061, relwidth=0.061)
buttonF = tk.Button(root, text="F", font=("Comic Sans Ms", 12), command=lambda: letter("F"))
buttonF.place(relx=0.414, rely=0.8, relheight=0.061, relwidth=0.061)
buttonG = tk.Button(root, text="G", font=("Comic Sans Ms", 12), command=lambda: letter("G"))
buttonG.place(relx=0.476, rely=0.8, relheight=0.061, relwidth=0.061)
buttonH = tk.Button(root, text="H", font=("Comic Sans Ms", 12), command=lambda: letter("H"))
buttonH.place(relx=0.538, rely=0.8, relheight=0.061, relwidth=0.061)
buttonI = tk.Button(root, text="I", font=("Comic Sans Ms", 12), command=lambda: letter("I"))
buttonI.place(relx=0.601, rely=0.8, relheight=0.061, relwidth=0.061)
buttonJ = tk.Button(root, text="J", font=("Comic Sans Ms", 12), command=lambda: letter("J"))
buttonJ.place(relx=0.664, rely=0.8, relheight=0.061, relwidth=0.061)
buttonK = tk.Button(root, text="K", font=("Comic Sans Ms", 12), command=lambda: letter("K"))
buttonK.place(relx=0.726, rely=0.8, relheight=0.061, relwidth=0.061)
buttonL = tk.Button(root, text="L", font=("Comic Sans Ms", 12), command=lambda: letter("L"))
buttonL.place(relx=0.788, rely=0.8, relheight=0.061, relwidth=0.061)
buttonM = tk.Button(root, text="M", font=("Comic Sans Ms", 12), command=lambda: letter("M"))
buttonM.place(relx=0.851, rely=0.8, relheight=0.061, relwidth=0.061)
buttonN = tk.Button(root, text="N", font=("Comic Sans Ms", 12), command=lambda: letter("N"))
buttonN.place(relx=0.1, rely=0.863, relheight=0.061, relwidth=0.061)
buttonO = tk.Button(root, text="O", font=("Comic Sans Ms", 12), command=lambda: letter("O"))
buttonO.place(relx=0.162, rely=0.863, relheight=0.061, relwidth=0.061)
buttonP = tk.Button(root, text="P", font=("Comic Sans Ms", 12), command=lambda: letter("P"))
buttonP.place(relx=0.225, rely=0.863, relheight=0.061, relwidth=0.061)
buttonQ = tk.Button(root, text="Q", font=("Comic Sans Ms", 12), command=lambda: letter("Q"))
buttonQ.place(relx=0.288, rely=0.863, relheight=0.061, relwidth=0.061)
buttonR = tk.Button(root, text="R", font=("Comic Sans Ms", 12), command=lambda: letter("R"))
buttonR.place(relx=0.351, rely=0.863, relheight=0.061, relwidth=0.061)
buttonS = tk.Button(root, text="S", font=("Comic Sans Ms", 12), command=lambda: letter("S"))
buttonS.place(relx=0.414, rely=0.863, relheight=0.061, relwidth=0.061)
buttonT = tk.Button(root, text="T", font=("Comic Sans Ms", 12), command=lambda: letter("T"))
buttonT.place(relx=0.476, rely=0.863, relheight=0.061, relwidth=0.061)
buttonU = tk.Button(root, text="U", font=("Comic Sans Ms", 12), command=lambda: letter("U"))
buttonU.place(relx=0.538, rely=0.863, relheight=0.061, relwidth=0.061)
buttonV = tk.Button(root, text="V", font=("Comic Sans Ms", 12), command=lambda: letter("V"))
buttonV.place(relx=0.601, rely=0.863, relheight=0.061, relwidth=0.061)
buttonW = tk.Button(root, text="W", font=("Comic Sans Ms", 12), command=lambda: letter("W"))
buttonW.place(relx=0.664, rely=0.863, relheight=0.061, relwidth=0.061)
buttonX = tk.Button(root, text="X", font=("Comic Sans Ms", 12), command=lambda: letter("X"))
buttonX.place(relx=0.726, rely=0.863, relheight=0.061, relwidth=0.061)
buttonY = tk.Button(root, text="Y", font=("Comic Sans Ms", 12), command=lambda: letter("Y"))
buttonY.place(relx=0.788, rely=0.863, relheight=0.061, relwidth=0.061)
buttonZ = tk.Button(root, text="Z", font=("Comic Sans Ms", 12), command=lambda: letter("Z"))
buttonZ.place(relx=0.851, rely=0.863, relheight=0.061, relwidth=0.061)
result_dict = {0: result0, 1: result1, 2: result2, 3: result3, 4: result4, 5: result5, 6: result6, 7: result7}
alpha_dict = {"A": buttonA, "B": buttonB, "C": buttonC, "D": buttonD, "E": buttonE, "F": buttonF, "G": buttonG, "H": buttonH, "I": buttonI, "J": buttonJ, "K": buttonK,"L": buttonL, "M": buttonM, "N": buttonN, "O": buttonO, "P": buttonP, "Q": buttonQ, "R": buttonR, "S": buttonS, "T": buttonT, "U": buttonU, "V": buttonV, "W": buttonW, "X": buttonX, "Y": buttonY, "Z": buttonZ}
background_dict = {0: "background_0.png", 1: "background_1.png", 2: "background_2.png", 3: "background_3.png",
                   4: "background_4.png", 5: "background_5.png", 6: "background_6.png", 7: "background_7.png",
                   8: "background_8.png", 9: "background_9.png", 10: "background_10.png", 11: "background_11.png"}
first_letter = random.choice(letters)
key = get_key(first_letter)
del dictofLetters[key]
result_dict.get(key)["text"] = first_letter
root.mainloop()