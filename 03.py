import turtle
import tkinter

george = turtle.Turtle()
george.color("yellow")
for side in [1,2,3,4]:
    george.forward(100)
    george.right(90)
tkinter.mainloop()