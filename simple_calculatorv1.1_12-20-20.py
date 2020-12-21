from tkinter import*

window = Tk()
window.title("Simple Calculator")
#window.minsize(300,300)

frame = Frame(window)
frame.grid(row=0, column=0)

operator = ""
temp_results = ""
text_input = StringVar()
key_list = ["C","/","*","D",7,8,9,"-",4,5,6,"+",1,2,3,"=",0,"."]
btn_dict = {}


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

def create_btn(btn_val,row_num, col_num,spec_bool):
    global btn_dict
    global window
    w = 30
    h = 30
    
    if btn_val == "C":
        btn_dict.update({btn_val: Button(window,padx = w, pady = h, bd = 8,fg = 'black',font =('arial',20,'bold'),
                            text=btn_val,command= lambda:btn_clear_display()).grid(row=row_num,column=col_num)})
        window.bind("<Escape>", lambda i : btn_clear_display())
    elif btn_val == "D":
        btn_dict.update({btn_val: Button(window,padx = w, pady = h, bd = 8,fg = 'black',font =('arial',20,'bold'),
                            text=btn_val,command= lambda:btn_clear_display()).grid(row=row_num,column=col_num)})
        window.bind("<Delete>", lambda i : btn_clear_display())
    elif btn_val == "=":
        btn_dict.update({btn_val: Button(window,padx = w, pady = (2*h+10), bd = 8,fg = 'black',font =('arial',20,'bold'),
                            text=btn_val,command= lambda:btn_equals_input()).grid(row=row_num,rowspan = 2,column=col_num)})
        window.bind("<Return>", lambda i : btn_equals_input())
    else:
        if btn_val == "0":
            btn_dict.update({btn_val: Button(window,padx = 2*w, pady = 2*h, bd = 8,fg = 'black',font =('arial',20,'bold'),
                                text=btn_val,command= lambda:btn_click(btn_val)).grid(row=row_num,column=col_num, columnspan = 2)})
        else:
            btn_dict.update({btn_val: Button(window,padx = w, pady = h, bd = 8,fg = 'black',font =('arial',20,'bold'),
                                text=btn_val,command= lambda:btn_click(btn_val)).grid(row=row_num,column=col_num)})
        window.bind(btn_val, lambda i: btn_click(btn_val))



#center_window(window)
txt_display = Entry(window, font =('arial',20,'bold'),textvariable = text_input, bd = 20, insertwidth = 4,
                    bg = "powder blue", justify = 'right').grid(row=1,columnspan = 4)
pos_r = 2
pos_c = 0
                         
for btn_key in key_list:
    if pos_c % 4 == 0 and pos_c > 0:
        pos_r +=1
        pos_c = 0
    if btn_key == "C" or btn_key == "D" or btn_key == "=":
        create_btn(btn_key, pos_r,pos_c,True)
    else:
        if btn_key == ".":
            create_btn(btn_key,pos_r, (pos_c + 1), False)
        else:
            create_btn(btn_key,pos_r,pos_c,False)
    pos_c += 1

window.mainloop()

