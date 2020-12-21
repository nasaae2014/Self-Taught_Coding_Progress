from tkinter import*

window = Tk()
window.title("Simple Calculator")
#window.minsize(300,300)

frame = Frame(window)
frame.grid(row=0, column=0)

operator = ""
temp_results = ""
text_input = StringVar()


def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() //2) - (width//2)
    y = (win.winfo_screenheight() //2) - (height//2)
    win.geometry('{}x{}+{}+{}'.format(width,height,x,y))

def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btn_clear_display():
    global operator
    operator = ""
    text_input.set("")

def btn_equals_input():
    global operator
    answer = str(eval(operator))
    text_input.set(answer)
    operator = answer

#center_window(window)
#ROW 1
txt_display = Entry(window, font =('arial',20,'bold'),textvariable = text_input, bd = 30, insertwidth = 4,
                    bg = "powder blue", justify = 'right').grid(row=1,columnspan = 4)

btnclear = Button(window,padx = 25, bd = 8, fg = 'black', font=('arial',20,'bold'),
                  text = "C",command = lambda:btn_clear_display()).grid(row = 1,column = 4)
window.bind("<Escape>",lambda i : btn_clear_display())

#ROW 2
btn7 = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="7",command= lambda:btn_click(7)).grid(row=2,column=0)
window.bind("7",lambda i : btn_click(7))
btn8 = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="8",command= lambda:btn_click(8)).grid(row=2,column=1)
window.bind("8",lambda i : btn_click(8))
btn9 = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="9",command= lambda:btn_click(9)).grid(row=2,column=2)
window.bind("9",lambda i : btn_click(9))

btnplus = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="+",command= lambda:btn_click("+")).grid(row=2,column=3)
window.bind("<+>",lambda i : btn_click("+"))

#ROW 3
btn4 = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="4",command= lambda:btn_click(4)).grid(row=3,column=0)
window.bind("4",lambda i : btn_click(4))
btn5 = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="5",command= lambda:btn_click(5)).grid(row=3,column=1)
window.bind("5",lambda i : btn_click(5))
btn6 = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="6",command= lambda:btn_click(6)).grid(row=3,column=2)
window.bind("6",lambda i : btn_click(6))

btnminus = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="-",command= lambda:btn_click("-")).grid(row=3,column=3)
window.bind("-",lambda i : btn_click("-"))

#ROW 4
btn1 = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="1",command= lambda:btn_click(1)).grid(row=4,column=0)
window.bind("1",lambda i : btn_click(1))
btn2 = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="2",command= lambda:btn_click(2)).grid(row=4,column=1)
window.bind("2",lambda i : btn_click(2))
btn3 = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="3",command= lambda:btn_click(3)).grid(row=4,column=2)
window.bind("3",lambda i : btn_click(3))

btnmultiply = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="*",command= lambda:btn_click("*")).grid(row=4,column=3)
window.bind("<*>",lambda i : btn_click("*"))

#ROW 5
btn0 = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="0",command= lambda:btn_click(0)).grid(row=5,column=0)
window.bind("0",lambda i : btn_click(0))
btndecimal = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text=".",command= lambda:btn_click(".")).grid(row=5,column=1)
window.bind("<.>",lambda i : btn_click("."))
btnequal = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="=",command= lambda:btn_equals_input()).grid(row=5,column=2)
window.bind("<Return>",lambda i : btn_equals_input())

btndivide = Button(window,padx = 25, bd = 8,fg = 'black',font =('arial',20,'bold'),
              text="/",command= lambda:btn_click("/")).grid(row=5,column=3)
window.bind("</>",lambda i : btn_click("/"))



window.mainloop()

