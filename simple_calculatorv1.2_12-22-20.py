from tkinter import*

window = Tk()
window.title("Simple Calculator")


operator = ""
temp_results = ""
text_input = StringVar()
key_list = ["C","+/-","/","*",7,8,9,"-",4,5,6,"+",1,2,3,"=",0,"."]
btn_dict = {}
eval_press = False
eval_error = False

def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() //2) - (width//2)
    y = (win.winfo_screenheight() //2) - (height//2)
    win.geometry('{}x{}+{}+{}'.format(width,height,x,y))

def isMathOperatorIn():
    global text_input

    temp = text_input.get()
    if "+" in temp and temp.rindex("+") >0:
        return True
    elif "-" in temp and temp.rindex("-") >0:
        return True
    elif "*" in temp:
        return True
    elif "/" in temp:
        return True
    else:
        return False

def isMathOpAdd():
    global text_input
    return text_input.get().rfind("+") != -1

def isMathOpSub():
    global text_input
    return text_input.get().rfind("-") != -1 and text_input.get().rfind("-") != 0

def isMathOpMult():
    global text_input
    return text_input.get().rfind("*") != -1

def isMathOpDiv():
    global text_input
    return text_input.get().rfind("/") != -1

def MathOpSignSwap(display_txt):
    if isMathOpAdd():
        return display_txt.replace("+","-")
    else:
        temp = convert_to_list(display_txt)
        temp[display_txt.rindex("-")] = "+"
        return convert_to_str(temp)
    
def btn_click(numbers):
    global operator
    global eval_press

    if eval_error:
        operator += ""
    else:
        if (eval_press and str(numbers).isnumeric()) or (eval_press and operator.isdecimal()):
            operator += ""
        else:        
            if numbers == "+" or numbers == "-" or numbers == "/" or numbers == "*":
                if isMathOperatorIn() == False:
                    operator = operator + str(numbers)
            else:
                operator += str(numbers)
            eval_press = False
                
    text_input.set(operator)
    
def btn_clear_display():
    global operator
    global eval_press
    global eval_error
    
    operator = ""
    text_input.set("")
    eval_press = False
    eval_error = False

def removeNegSign(display_txt):
    temp = convert_to_list(display_txt)
    temp[0]=""
    return convert_to_str(temp)

def convert_to_list(str_display):
    temp = []
    temp[:0] = str_display
    return temp

def convert_to_str(list_display):
    temp = ""
    return temp.join(list_display)

def btn_one_char_clear():
    global operator
    temp = convert_to_list(operator)
    temp.pop()
    operator = convert_to_str(temp)
    text_input.set(operator)
    
def btn_pos_neg():
    global operator
    global text_input
    global eval_error
    operator = text_input.get()
    
    if eval_error:
        operator += ""
    elif isMathOperatorIn() == False:
        if "-" in operator and operator.index("-") == 0:
            operator = removeNegSign(operator)
        else:
            operator = "-"+operator
    else:
        if isMathOpAdd() or isMathOpSub():
            operator = MathOpSignSwap(operator)
        elif isMathOpMult() or isMathOpDiv():
            if operator.find("-") == 0:
                operator = removeNegSign(operator)
            else:
                operator = "-"+operator
    text_input.set(operator)
            
def btn_equals_input():
    global operator
    global eval_press
    global eval_error

    if eval_error:
        answer = "E"
        eval_error = True
    else:
        try:
            answer = str(eval(operator))
        except ZeroDivisionError:
            answer = "E"
            eval_error = True
    text_input.set(answer)
    operator = answer
    eval_press = True
    

def create_btn(btn_val,row_num, col_num,spec_bool):
    global btn_dict
    global window
    w = 30
    h = 30
    
    if btn_val == "C":
        btn_dict.update({btn_val: Button(window,padx = w, pady = h, bd = 8,fg = 'black',font =('arial',20,'bold'),
                            text=btn_val,command= lambda:btn_clear_display()).grid(row=row_num,column=col_num)})
        window.bind("<Escape>", lambda i : btn_clear_display())
    elif btn_val == "+/-":
        btn_dict.update({btn_val: Button(window,padx = w, pady = h, bd = 8,fg = 'black',font =('arial',20,'bold'),
                            text=btn_val,command= lambda:btn_pos_neg()).grid(row=row_num,column=col_num)})
        #window.bind("<BackSpace>", lambda i : btn_one_char_clear())
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
txt_display = Entry(window, font =('arial',20,'bold'),textvariable = text_input, bd = 10, insertwidth = 4,
                    bg = "powder blue", justify = 'right').grid(row=1,columnspan = 4)
pos_r = 2
pos_c = 0
                         
for btn_key in key_list:
    if pos_c % 4 == 0 and pos_c > 0:
        pos_r +=1
        pos_c = 0
    if btn_key == "C" or btn_key == "+/-" or btn_key == "=":
        create_btn(btn_key, pos_r,pos_c,True)
    else:
        if btn_key == ".":
            create_btn(btn_key,pos_r, (pos_c + 1), False)
        else:
            create_btn(btn_key,pos_r,pos_c,False)
    pos_c += 1

window.mainloop()

