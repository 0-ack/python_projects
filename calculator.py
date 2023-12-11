#!/usr/bin/env python
#coding: utf-8

# # CALCULATOR
#
#SIMPLE CALCULATOR THAT CAN PERFORM FOLLOWING OPERATIONS
#BASIC OPERATIONS
#1. ADDITION
#2. SUBTRACTION
#3. MULTIPLICATION
#4. DIVISION
#5. MODULUS
#
#ADVANCED OPERATIONS
#1. NATURAL LOG
#2. TRIGNOMETRIC CALCULATIONS
#3. EXPONENTIAL CALCULATIONS

#in[ ]:



from tkinter import *
import math as m
root = Tk()
# GIVING TITLE TO THE APPLICATION AS simple calculator
root.title('Simple Calculator')
e = Entry(root, width = 50, borderwidth = 5, relief = RIDGE, fg = 'White', bg = 'Black')
e.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 15)

#Creating some userdefined functions for the operations involved in the application.
def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old + to_print)
    return

def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result = ''
    if text == 'deg':
        result = str(m.degrees(float(no)))
    if text == 'sin':
        result = str(m.sin(float(no)))
    if text == 'cos':
        result = str(m.cos(float(no)))
    if text == 'tan':
        result = str(m.tan(float(no)))
    if text == 'lg':
        result = str(m.log10(float(no)))
    if text == 'ln':
        result = str(m.log(float(no)))
    if text == 'Sqrt':
        result = str(m.sqrt(float(no)))
    if text == 'x!':
        result = str(m.factorial(float(no)))
    if tect == '1/x':
        result = str(m.1/(float(no)))
    if text == 'pi':
        if no == '':
            result = str(m.pi)
        else:
            result = str(float(no) * m.pi)
    if text == 'e':
        if no == '':
            result = str(m.e)
        else:
            result = str(m.e**float(no))

    e.delete(0, END)
    e.insert(0, result)

#This function clears all the contents displayed on the computation window.
def clear():
    e.delete(0, END)
    return

#This function clears one character from the rare end of the string.
def bksps():
    current = e.get()
    length = len(current) - 1
    e.delete(length, END)

#This function is defind to evaluate the results and to prompt on the console.
def evaluate():
    ans = e.get()
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)

#Arrangement of buttons for better visualization and computation.
lg = Button(root, text= 'log', padx = 24, pady = 10, relief = RAISED, bg = 'Black', fg = 'White')
lg.bind('<Button-1>', sc)
ln = Button(root, text = 'ln', padx = 28, pady = 10, relief = RAISED, bg = 'Black', fg = 'White')
ln.bind('<Button-1>', sc)
par1st = Button(root, text = '(', padx = 29, pady = 10, relief = RAISED, bg = 'Black', fg = 'White', command = lambda: click('('))
par2nd = Button(root, text = ')', padx = 30, pady = 10, relief = RAISED, bg = 'Black', fg = 'White', command = lambda: click(')'))
dot = Button(root, text = '.', padyx = 29, pady = 10, relief, = RAISED, bg = 'Green', fg = 'Black', command = lambda: click('.'))

exp = Button(root, text = '^', padx = 29, pady = 10, relieft = RAISED, bg = 'Black', fg = 'White', command = lambda: click('**'))

degb = Button(root, text = 'deg', padx = 23, pady = 10, relief = RAISED, bg = 'Black', fg = 'White')
degb.bind('<Button-1>', sc)
sinb = Button(root, text = 'sin', padx = 24, pady = 10, relief = RAISED, bg = 'Black', fg = 'White')
sinb.bind('<Button-1>', sc)
cosb = Button(root, text = 'cos', padx = 23, pady = 10, relief = RAISED, bg = 'Black', fg = 'White')
cosb.bind('<Button-1>', sc)
tanb = Button(root, text = 'tan', padx = 23, pady = 10, relief = RAISED, bg = 'Black', fg = 'White')
tanb.bind('<Button-1>', sc)


sqrtm = Button(root, text = 'Sqrt', padx = 23, pady = 10, relief = RAISED, bg = 'Black', fg = 'White')
sqrtm.bind('<Button-1>', sc)
ac = Button(root, text = 'C', padx = 29, pady = 10, relief = RAISED, bg = 'Dark Red', fg = 'White', command = lambda: clear())
bksp = Button(root, text = 'DEL', padx =24, pady = 10, relief = RAISED, bg = 'Dark Red', fg = 'White', command = lambda: bksps())
mod = Button(root, text = '%', padx = 24, pady = 10, relief = RAISED, bg = 'Black', fg = 'White', command = lambda: click('%'))
div = Button(root, text = '/', padx = 29, pady = 10, relief = RAISED, bg = 'yellow', fg = 'Black', command = lambda: click('/'))

fact =


























