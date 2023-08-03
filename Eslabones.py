from tkinter import *
from  PyArduino import *

def onClosing():
    #arduino.sendData([60,120,0])
    #arduino.close()
    print("Arduino desconectado")
    root.destroy()
# funcion base 
def getAngle(int):
    q1Angle.set(q1Scale.get())
    #arduino.sendData([q1Scale.get(),q2Angle.get(),q3Angle.get()])
    print(q1Scale.get())
    #pass
# funcion brazo   
def getAngle2(int):
    q2Angle.set(q2Scale.get())
    #arduino.sendData([q1Scale2.get(),q2Angle.get(),q3Angle.get()])
    print(q2Scale.get())
    #pass
    
def getAngle3(int):
    q3Angle.set(q3Scale.get())
    #arduino.sendData([q1Scale2.get(),q2Angle.get(),q3Angle.get()])
    print(q3Scale.get())
    #pass
    
# base 
def q1MinusOk():
    q1Angle.set(int(q1Angle.get()) - int(q1Value.get()))
    q1Scale.set(q1Angle.get())
    
# brazo 
def q2MinusOk():
    q2Angle.set(int(q2Angle.get()) - int(q2Value.get()))
    q2Scale.set(q2Angle.get())

def q3MinusOk():
    q3Angle.set(int(q3Angle.get()) - int(q3Value.get()))
    q3Scale.set(q3Angle.get())

# base     
def q1PlusOk():
    q1Angle.set(int(q1Angle.get()) + int(q1Value.get()))
    q1Scale.set(q1Angle.get())
    
# brazo 
def q2PlusOk():
    q2Angle.set(int(q2Angle.get()) + int(q2Value.get()))
    q2Scale.set(q2Angle.get())
    
def q3PlusOk():
    q3Angle.set(int(q3Angle.get()) + int(q3Value.get()))
    q3Scale.set(q3Angle.get())
    
def callback():
    global k
    if isRun:
        #arduino.sendData([q1[k],q2[k],q3[k]])
        if k < len(q1) - 1:
            k = k + 1
        else:
            k = 0
    else:
        #arduino.sendData([q1Angle.get(),q2Angle.get(),q3Angle.get()])
        k = 0 #se borra cuando se conecta el arduino
    root.after(2000, callback)
    
def enviar():
    q1Angle.set(q1Value.get())
    q2Angle.set(q2Value.get())
    q3Angle.set(q3Value.get())
    
    q1Angle.set(q1Value.get())
    q2Angle.set(q2Value.get())
    q3Angle.set(q3Value.get())
    
def home():
    global isRun
    q1Angle.set(0) #se cambian los 0 por los valores de home
    q2Angle.set(0)
    q3Angle.set(0)
    
    q1Angle.set(q1Angle.get())
    q2Angle.set(q2Angle.get())
    q3Angle.set(q3Angle.get())
    
    isRun = False
    
def save():
    global q1, q2, q3
    q1.append(q1Angle.get())
    print(q1)
    q2.append(q2Angle.get())
    print(q2)
    q3.append(q3Angle.get())
    print(q3)

def ejecutar():
    global isRun
    isRun = True
    
def delete():
    global isRun
    isRun = False
    
    q1.clear()
    q2.clear()
    q3.clear()
    
    print(q1)
    print(q2)
    print(q3)
    
    home()
    
########### COMUNICACIÓN SERIAL ###########

port = "COM4"
#arduino = serialArduino(port)

########### INTERFAZ GRÁFICA ###########


root = Tk()
root.geometry("800x600")
root.protocol("WM_DELETE_WINDOW", onClosing)
root.title("Interfaz de Control")
title = Label(root, text = "CONTROL MANIPULADOR", font = ("Arial", 15, "bold"))
title.place(x = 300, y = 10)

############################################################################

q1Angle = IntVar()
# base
q1Scale = Scale(root, command = getAngle, label = "Eslabon 1", font = ("Arial 14"), from_ =0 , to =180, orient = HORIZONTAL, length = 300)
q1Scale.place(x = 40, y = 50)
# base 
q1Minus = Button(root, text = "- q1", font = ("Arial 14"), command = q1MinusOk, height = 1, width = 6)
q1Minus.place(x = 40, y = 140)
# base 
q1Value = Entry(root,width = 6, font = ("Arial 18"))
q1Value.place(x = 140, y = 142)
q1Value.insert(0, "1")

q1Plus = Button(root, text = "+ q1", font = ("Arial 14"), command = q1PlusOk, height = 1, width = 6)
q1Plus.place(x = 240, y = 142)

#________________________________________ brazo_________________________________________-
q2Angle = IntVar()

q2Scale = Scale(root, command = getAngle2, label = "Eslabon 2", font = ("Arial 14"), from_ =0 , to =180, orient = HORIZONTAL, length = 300)
q2Scale.place(x = 40, y = 190)

q2Minus = Button(root, text = "- q2", font = ("Arial 14"), command = q2MinusOk, height = 1, width = 6)
q2Minus.place(x = 40, y = 270)

q2Value = Entry(root,width = 6, font = ("Arial 18"))
q2Value.place(x = 140, y = 272)
q2Value.insert(0, "1")

q2Plus = Button(root, text = "+ q2", font = ("Arial 14"), command = q2PlusOk, height = 1, width = 6)
q2Plus.place(x = 240, y = 272)

#_________________________________________________________________________________________
q3Angle = IntVar()

q3Scale = Scale(root, command = getAngle3, label = "Eslabon 3", font = ("Arial 14"), from_ =0 , to =180, orient = HORIZONTAL, length = 300)
q3Scale.place(x = 40, y = 350)

q3Minus = Button(root, text = "- q3", font = ("Arial 14"), command = q3MinusOk, height = 1, width = 6)
q3Minus.place(x = 40, y = 450)

q3Value = Entry(root,width = 6, font = ("Arial 18"))
q3Value.place(x = 140, y = 450)
q3Value.insert(0, "1")

q3Plus = Button(root, text = "+ q3", font = ("Arial 14"), command = q3PlusOk, height = 1, width = 6)
q3Plus.place(x = 240, y = 450)

####################################################################
sendBtn = Button(root, text = "Enviar", font = ("Arial 14"), command = enviar)
sendBtn.place (x = 40, y = 520)

####################################################################
homeBtn = Button(root, text = "Home", font = ("Arial 14"), command = home)
homeBtn.place (x = 140, y = 520)

#####################################################################
q1 = []
q2 = []
q3 = []
saveBtn = Button(root, text = "Save", font = ("Arial 14"), command = save)
saveBtn.place (x = 480, y = 200)

#####################################################################
isRun = False
k = 0
runBtn = Button(root, text = "Run", font = ("Arial 14"), command = ejecutar)
runBtn.place (x = 620, y = 200)

#####################################################################
deleteBtn = Button(root, text = "Delete", font = ("Arial 14"), command = delete)
deleteBtn.place (x = 480, y = 250)


root.after(500, callback)
root.mainloop()
