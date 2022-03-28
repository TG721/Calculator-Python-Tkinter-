import tkinter
import operator
import math
from tkinter import messagebox
from PIL import ImageTk, Image

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '÷' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

root = tkinter.Tk()
root.title("Calculator")
root.iconbitmap(r'icon.ico')
root.resizable(False, False)

e = tkinter.Entry(root, width=40, font=('Arial 12'), )
eAbove = tkinter.Entry(root, width=40, font=('Arial 12'), )
ee = tkinter.Entry(root, width=40)

eAbove.grid(row=0, column=0, columnspan=8)
e.grid(row=1, column=0, columnspan=8)




# functions
def errorDivisionBy0():
    tkinter.messagebox.showerror("Error", "Division by 0")
def sqrtOfNegativeNum():
    messagebox.showerror("Error", "square root of negative number")

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def clearr():
    e.delete(0, tkinter.END)
    eAbove.delete(0, tkinter.END)
def getButton(buttonn):
    current = e.get()
    if buttonn != "T" and buttonn != "F":
        e.delete(0, tkinter.END)
        e.insert(0, current + buttonn)
    # ee.insert(0, len(e.get()))
    # eee.insert(0, e.get())
    # global result
    # result = "23"
    elif(current==""):
        if(eAbove.get()==""):
            e.delete(0, tkinter.END)
            e.insert(0, buttonn)
        else:
            pass
    elif(current[0]=="∨" or current[0]=="∧" or current[0]=="→" or current[0]=="↔"):
        e.delete(0, tkinter.END)
        e.insert(0, current[0]+buttonn)
def getOp(buttonn):
    current = e.get()
    if current!="T" and current!="F":
        if(current.isdigit() or isfloat(current) and float(current)>0 ):
            eAbove.insert(0, current)
            e.delete(0, tkinter.END)
            e.insert(0, buttonn)
        elif(len(current)>=2 and current[0]=='-' and (current[1:].isdigit() or isfloat(current)) and len(eAbove.get())==0):
            e.delete(0, tkinter.END)
            eAbove.insert(0, current)
            e.insert(0, buttonn)
        else:
            e.delete(0, tkinter.END)
            e.insert(0, buttonn)
        # a = result
        # ee.insert(0,a)
    else:
        eAbove.insert(0, current)
        e.delete(0, tkinter.END)
        e.insert(0, buttonn)
def getResult():
    current = e.get()
    if(current==""):
        pass
    elif(current[len(current)-1]!="T" and current[len(current)-1]!="F"):
        oper=current[0];
        first = float(eAbove.get())
        second = float(current[1:])
        # ee.insert(0,second)
        if second==0 and oper=="÷":
            errorDivisionBy0()
        else:
            Finresult = ops[oper](first, second)
            eAbove.delete(0, tkinter.END)
            eAbove.insert(0, Finresult)
            e.delete(0, tkinter.END)
    else:
        oper = current[0];
        first = eAbove.get()
        second = current[1:]
        eAbove.delete(0, tkinter.END)
        e.delete(0, tkinter.END)
        if(oper=="∧"):
            if(first=="T" and second=="T"):
                eAbove.insert(0, "T")
            else:
                eAbove.insert(0, "F")
        if(oper=="∨"):
            if(first=="F" and second=="F"):
                eAbove.insert(0, "F")
            else:
                eAbove.insert(0, "T")
        if(oper=="→"):
            if(first=="T" and second=="F"):
                eAbove.insert(0, "F")
            else:
                eAbove.insert(0, "T")
        if(oper=="↔"):
            if(first==second):
                eAbove.insert(0, "T")
            else:
                eAbove.insert(0, "F")

def inPowTwo():
    first = float(e.get())**2
    eAbove.insert(0, first)
    e.delete(0, tkinter.END)

def sqrtOf():
    if float(e.get())<0:
        sqrtOfNegativeNum()
    else:
        first = math.sqrt(float(e.get()))
        eAbove.insert(0, first)
        e.delete(0, tkinter.END)

def oneDivided():
    if e.get()=="0":
        errorDivisionBy0()
    else:
        first = 1/float(e.get())
        eAbove.insert(0, first)
        e.delete(0, tkinter.END)

button_1 = tkinter.Button(root, text="1", height=3, activebackground='lime', command=lambda: getButton("1"))
button_2 = tkinter.Button(root, text="2", height=3, activebackground='lime', command=lambda: getButton("2"))
button_3 = tkinter.Button(root, text="3", height=3, activebackground='lime', command=lambda: getButton("3"))
button_4 = tkinter.Button(root, text="4", height=3, activebackground='lime', command=lambda: getButton("4"))
button_5 = tkinter.Button(root, text="5", height=3, activebackground='lime', command=lambda: getButton("5"))
button_6 = tkinter.Button(root, text="6", height=3, activebackground='lime', command=lambda: getButton("6"))
button_7 = tkinter.Button(root, text="7", height=3, activebackground='lime', command=lambda: getButton("7"))
button_8 = tkinter.Button(root, text="8", height=3, activebackground='lime', command=lambda: getButton("8"))
button_9 = tkinter.Button(root, text="9", height=3, activebackground='lime', command=lambda: getButton("9"))
button_0 = tkinter.Button(root, text="0", height=3, activebackground='lime', command=lambda: getButton("0"))
button_float = tkinter.Button(root, text=".", height=3, activebackground='lime', command=lambda: getButton("."))




button_oneDividedBy = tkinter.Button(root, text="1/x", height=3, bg="green", command=lambda: oneDivided())
button_inPowTwo = tkinter.Button(root, text="x\u00b2", height=3,  bg="green", command=lambda: inPowTwo())
button_sqrt = tkinter.Button(root, text="√x", height=3,  bg="green", command=lambda: sqrtOf())
button_oneDividedBy.grid(row=2, column=0, columnspan=2, sticky="WE")
button_inPowTwo.grid(row=2, column=2, columnspan=2, sticky="WE")
button_sqrt.grid(row=2, column=4, columnspan=2, sticky="WE")
button_equal = tkinter.Button(root, text="=", height=3, bg="blue", command=lambda: getResult())
button_plus = tkinter.Button(root, text="+", height=3, bg="red", command=lambda: getOp("+"))
button_minus = tkinter.Button(root, text="-", height=3, bg="red", command=lambda: getOp("-"))
button_division = tkinter.Button(root, text="÷", height=3, bg="red", command=lambda: getOp("÷"))
button_multiply = tkinter.Button(root, text="*", height=3, bg="red", command=lambda: getOp("*"))
button_division.grid(row=2, column=6, columnspan=2, sticky="WE")
button_multiply.grid(row=3, column=6, columnspan=2, sticky="WE")
button_minus.grid(row=4, column=6, columnspan=2, sticky="WE")
button_plus.grid(row=5, column=6, columnspan=2, sticky="WE")
button_equal.grid(row=6, column=6, columnspan=2, sticky="WE")
button_0.grid(row=6, column=0, columnspan=2, sticky="WE")
button_float.grid(row=6, column=2, columnspan=2, sticky="WE")

button_a = tkinter.Button(root, text="A ∧ B", height=3, bg="violet", command=lambda: getOp("∧"))
button_b = tkinter.Button(root, text="A ∨ B ", height=3, bg="violet", command=lambda: getOp("∨"))
button_c = tkinter.Button(root, text="A → B", height=3, bg="violet", command=lambda: getOp("→"))
button_d = tkinter.Button(root, text="A ↔ B", height=3, bg="violet", command=lambda: getOp("↔"))
button_true = tkinter.Button(root, text="T", height=3, activebackground='lime', command=lambda: getButton("T"))
button_false = tkinter.Button(root, text="F", height=3, activebackground='lime', command=lambda: getButton("F"))
button_clear = tkinter.Button(root, text="C", height=3, command=clearr, bg="yellow")
button_clear.grid(row=6, column=4, columnspan=2, sticky="WE")

button_a.grid(row=7, column=2, columnspan=2, sticky="WE")
button_b.grid(row=7, column=0, columnspan=2, sticky="WE")
button_c.grid(row=7, column=4, columnspan=2, sticky="WE")
button_d.grid(row=7, column=6, columnspan=2, sticky="WE")
button_true.grid(row=8, column=0, columnspan=4, sticky="WE")
button_false.grid(row=8, column=4, columnspan=4, sticky="WE")
# e_A = tkinter.Entry(root, width=5)
# e_B = tkinter.Entry(root,  width=5, )
# e_A.grid(row=5, column=0, columnspan=1, )
# e_B.grid(row=5, column=1, columnspan=1, )

ee.grid(row=8, column=0, columnspan=8)

button_1.grid(row=5, column=0, columnspan=2, sticky="WE")
button_2.grid(row=5, column=2, columnspan=2, sticky="WE")
button_3.grid(row=5, column=4, columnspan=2, sticky="WE")
button_4.grid(row=4, column=0, columnspan=2, sticky="WE")
button_5.grid(row=4, column=2, columnspan=2, sticky="WE")
button_6.grid(row=4, column=4, columnspan=2, sticky="WE")
button_7.grid(row=3, column=0, columnspan=2, sticky="WE")
button_8.grid(row=3, column=2, columnspan=2, sticky="WE")
button_9.grid(row=3, column=4, columnspan=2, sticky="WE")

root.mainloop()