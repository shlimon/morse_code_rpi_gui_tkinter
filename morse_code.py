from tkinter import *
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

def dit():
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(12, GPIO.LOW)

def dah():
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(12, GPIO.LOW)


def gap():
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.75)

def morse_code(word):
    word.lower()
    for i in range(len(word)):
        if word[i] == 'a':
            dit()
            dah()
            gap()
        elif word[i] == 'b':
            dah()
            dit()
            dit()
            dit()
            gap()
        elif word[i] == 'c':
            dah()
            dit()
            dah()
            dit()
            gap()
        elif word[i] == 'd':
            dah()
            dit()
            dit()
            gap()
        elif word[i] == 'e':
            dit()
            gap()
        elif word[i] == 'f':
            dit()
            dit()
            dah()
            dit()
            gap()
        elif word[i] == 'g':
            dah()
            dah()
            dit()
            gap()
        elif word[i] == 'h':
            dit()
            dit()
            dit()
            dit()
            gap()
        elif word[i] == 'i':
            dit()
            dit()
            gap()
        elif word[i] == 'j':
            dit()
            dah()
            dah()
            dah()
            gap()
        elif word[i] == 'k':
            dah()
            dit()
            dah()
            gap()
        elif word[i] == 'l':
            dit()
            dah()
            dit()
            dit()
            gap()
        elif word[i] == 'm':
            dah()
            dah()
            gap()
        elif word[i] == 'n':
            dah()
            dit()
            gap()
        elif word[i] == '0':
            dah()
            dah()
            dah()
            gap()
        elif word[i] == 'p':
            dit()
            dah()
            dah()
            dit()
            gap()
        elif word[i] == 'q':
            dah()
            dah()
            dit()
            dah()
            gap()
        elif word[i] == 'r':
            dit()
            dah()
            dit()
            gap()
        elif word[i] == 's':
            dit()
            dit()
            dit()
            gap()
        elif word[i] == 't':
            dah()
            gap()
        elif word[i] == 'u':
            dit()
            dit()
            dah()
            gap()
        elif word[i] == 'v':
            dit()
            dit()
            dit()
            dah()
            gap()
        elif word[i] == 'w':
            dit()
            dah()
            dah()
            gap()
        elif word[i] == 'x':
            dah()
            dit()
            dit()
            dah()
            gap()
        elif word[i] == 'y':
            dah()
            dit()
            dah()
            dah()
            gap()
        elif word[i] == 'b':
            dah()
            dah()
            dit()
            dit()
            gap()
    i += 1


def click():
    user_input = text.get()
    output.delete(0.0, END)
    if len(user_input) < 12:
        output.insert(END,'successfully converted to morse code')
        morse_code(user_input)

    elif len(user_input) > 12:
        output.insert(END,'Unsuccessfully converted to morse code. Please provide less than 12 character')
    GPIO.cleanup()


window = Tk()
window.title("Morse Code")

Label(window, text = "Enter the word to convert to morse code", fg = "black", font = "none 12 bold") .grid(row = 0, column=1)
text = Entry(window, width = 20, bg = "white")
text.grid(row = 1, column=1)

Button(window, text ="CONVERT", width = 8, command = click) .grid(row =3, column=1)


output = Text(window, width = 75, height =6, wrap = WORD, background='green')
output.grid(row = 4, column=1, columnspan=2)


window.mainloop()





