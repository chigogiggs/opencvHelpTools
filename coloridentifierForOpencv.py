from tkinter import *
import cv2
import numpy as np
import threading

master = Tk()

rvalue = 0
bvalue = 0
gvalue = 0

urvalue = 255
ubvalue = 255
ugvalue = 255

def record():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        # hsv = hue, saturation, value
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lowerred = np.array([rvalue, bvalue, gvalue])
        upperred = np.array([urvalue, ubvalue, ugvalue])

        mask = cv2.inRange(hsv, lowerred, upperred)
        # result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        # cv2.imshow('result', result)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()


recordthread = threading.Thread(target=record, args=())
recordthread.start()
def onescale_cb(value):
    global rvalue,bvalue,gvalue, urvalue, ubvalue, ugvalue

    rvalue = int(value)
    print(rvalue,bvalue,gvalue,'\n',urvalue, ubvalue, ugvalue)

def twoscale_cb(value):
    global rvalue,bvalue,gvalue, urvalue, ubvalue, ugvalue
    bvalue = int(value)
    print(rvalue,bvalue,gvalue,'\n',urvalue, ubvalue, ugvalue)

def threescale_cb(value):
    global rvalue,bvalue,gvalue, urvalue, ubvalue, ugvalue
    gvalue = int(value)
    print(rvalue,bvalue,gvalue,'\n',urvalue, ubvalue, ugvalue)




def upperonescale_cb(value):
    global rvalue,bvalue,gvalue, urvalue, ubvalue, ugvalue

    urvalue = int(value)
    print(rvalue,bvalue,gvalue,'\n',urvalue, ubvalue, ugvalue)

def uppertwoscale_cb(value):
    global rvalue,bvalue,gvalue, urvalue, ubvalue, ugvalue

    ubvalue = int(value)
    print(rvalue,bvalue,gvalue,'\n',urvalue, ubvalue, ugvalue)


def upperthreescale_cb(value):
    global rvalue,bvalue,gvalue, urvalue, ubvalue, ugvalue

    ugvalue = int(value)
    print(rvalue,bvalue,gvalue,'\n',urvalue, ubvalue, ugvalue)



###################################################################
redlowervar = StringVar()
redtext = Label(master,textvariable= redlowervar, fg='red')
redlowervar.set("Red lower")
redtext.pack()
red = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=onescale_cb)
red.pack()

upperredvar = StringVar()
upperredtext = Label(master,textvariable= upperredvar, fg='red')
upperredvar.set("Red upper")
upperredtext.pack()
upperred = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=upperonescale_cb)
upperred.pack()

###################################################################

bluelowervar = StringVar()
bluetext = Label(master,textvariable= bluelowervar, fg='blue')
bluelowervar.set("blue lower")
bluetext.pack()
blue = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=twoscale_cb)
blue.pack()


upperbluevar = StringVar()
upperbluetext = Label(master,textvariable= upperbluevar, fg='blue')
upperbluevar.set("blue upper")
upperbluetext.pack()
upperblue = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=uppertwoscale_cb)
upperblue.pack()


###################################################################

greenlowervar = StringVar()
greentext = Label(master,textvariable= greenlowervar, fg='green')
greenlowervar.set("green lower")
greentext.pack()
green = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=threescale_cb)
green.pack()

uppergreenvar = StringVar()
uppergreentext = Label(master,textvariable= uppergreenvar, fg='green')
uppergreenvar.set("green upper")
uppergreentext.pack()
uppergreen = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=upperthreescale_cb)
uppergreen.pack()

###################################################################




mainloop()