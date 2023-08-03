from tkinter import *
from  F_Serial import *

def onClosing():
    arduino.sendData([60,140,0])
    arduino.close()
    print("Arduino desconectado")
    root.destroy()

def getAngle(int):
    q1Angle.set(q1Scale.get())
    arduino.sendData([q1Scale.get(),0,0])
    print(q1Scale.get())
    #pass

def getAngle2(int):
    q2Angle.set(q2Scale.get())
    arduino.sendData([q2Scale.get(),0,1])
    print(q2Scale.get())
    #pass
def q1MinusOk():
    q1Angle.set(int(q1Angle.get()) - int(q1Value.get()))
    q1Scale.set(q1Angle.get())

def q2MinusOk():
    q2Angle.set(int(q2Angle.get()) - int(q2Value.get()))
    q2Scale.set(q2Angle.get())

def q1PlusOk():
    q1Angle.set(int(q1Angle.get()) + int(q1Value.get()))
    q1Scale.set(q1Angle.get())

def q2PlusOk():
    q2Angle.set(int(q2Angle.get()) + int(q2Value.get()))
    q2Scale.set(q2Angle.get())
    
def callback():
    arduino.sendData([q1Angle.get(),0,0])
    root.after(1000, callback)
    
def callback2():
    arduino.sendData([q2Angle.get(),0,1])
    root.after(2000, callback2)
    
########### COMUNICACIÓN SERIAL ###########

port = "COM5"
arduino = serialArduino(port)

########### INTERFAZ GRÁFICA ###########


root = Tk()
root.geometry("800x600")
root.protocol("WM_DELETE_WINDOW", onClosing)
root.title("Interfaz de Control")
title = Label(root, text = "CONTROL MANIPULADOR", font = ("Arial", 15, "bold"))
title.place(x = 300, y = 10)
######################
q1Angle = IntVar()
q2Angle = IntVar()

q1Scale = Scale(root, command = getAngle, label = "Eslabon 1", font = ("Arial 14"), from_ =0 , to =180, orient = HORIZONTAL, length = 300)
q1Scale.place(x = 40, y = 50)

q2Scale = Scale(root, command = getAngle, label = "Eslabon 2", font = ("Arial 14"), from_ =0 , to =180, orient = HORIZONTAL, length = 300)
q2Scale.place(x = 40, y = 250)

q1Minus = Button(root, text = "- q1", font = ("Arial 14"), command = q1MinusOk, height = 1, width = 6)
q1Minus.place(x = 40, y = 140)

q2Minus = Button(root, text = "- q2", font = ("Arial 14"), command = q2MinusOk, height = 1, width = 6)
q2Minus.place(x = 40, y = 340)

q1Value = Entry(root,width = 6, font = ("Arial 18"))
q1Value.place(x = 240, y = 142)
q1Value.insert(0, "10")

q2Value = Entry(root,width = 6, font = ("Arial 18"))
q2Value.place(x = 240, y = 342)
q2Value.insert(0, "10")

q1Plus = Button(root, text = "+ q1", font = ("Arial 14"), command = q1PlusOk, height = 1, width = 6)
q1Plus.place(x = 240, y = 142)

q2Plus = Button(root, text = "+ q2", font = ("Arial 14"), command = q2PlusOk, height = 1, width = 6)
q2Plus.place(x = 240, y = 342)

root.after(500, callback)
root.after(500, callback2)
root.mainloop()