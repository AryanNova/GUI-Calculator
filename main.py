import tkinter as tk
import math

def cal(text_widget):
    try:
        exp=text_widget.get(1.0,tk.END)
        result=eval(exp)
        text_widget.insert(tk.END,f"\n{result}")


    except:
        text_widget.delete(1.0,tk.END)
        text_widget.insert(tk.END,"Error")






def button_press(value,text_widget):
    text_widget.insert(tk.END,value)

def erasetext(text_widget):
    text_widget.delete(1.0,tk.END)
    


def click():
    root=tk.Tk()
    root.title("Calculator")
    root.geometry("450x500")
    root.config(bg="black")
    text=tk.Text(root,height=2,width=30,font=("Ariel",20,"bold"),insertwidth=5,fg="#333333",bg="#888888")
    text.grid(row=0,column=0,columnspan=4,sticky="nsew")
    root.grid_rowconfigure(0,weight=1)
    for i in range (1,5):
        root.grid_rowconfigure(i,weight=1)
    for i in range(0,4):
        root.grid_columnconfigure(i,weight=1)

    buttonvalue = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    row, col = 1, 0 

    for value in buttonvalue:
        button = tk.Button(root, text=value,font=("Ariel",9,"bold"), command=lambda v=value: button_press(v, text), height=6, width=2,fg="black",bg="dimgray")
        button.grid(row=row, column=col,sticky="nsew")

        col += 1  
        if col > 2:#
            col = 0
            row += 1
        
    button = tk.Button(root, text="+",font=("Ariel",9,"bold"), command=lambda: button_press("+", text), height=6, width=2,fg="black",bg="gray")
    button.grid(row=1, column=3,sticky="nsew")
    button = tk.Button(root, text="-",font=("Ariel",9,"bold"), command=lambda: button_press("-", text), height=6, width=2,fg="black",bg="gray")
    button.grid(row=2, column=3,sticky="nsew")
    button = tk.Button(root, text="/",font=("Ariel",9,"bold"), command=lambda: button_press("/", text), height=6, width=2,fg="black",bg="gray")
    button.grid(row=3, column=3,sticky="nsew")
    button = tk.Button(root, text="*",font=("Ariel",9,"bold"), command=lambda: button_press("*", text), height=6, width=2,fg="black",bg="gray")
    button.grid(row=4, column=3,sticky="nsew")
    button = tk.Button(root, text="=",font=("Ariel",9,"bold"), command=lambda: cal(text), height=6, width=2,fg="black",bg="gray")
    button.grid(row=4, column=2,sticky="nsew")
    button = tk.Button(root, text=".",font=("Ariel",9,"bold"), command=lambda: button_press(".", text), height=6, width=2,fg="black",bg="gray")
    button.grid(row=4, column=1,sticky="nsew")


    button=tk.Button(root,text="Erase",command=lambda: erasetext(text),height=2,width=10,fg="White",bg="gray10")
    button.grid(row=5,column=0,columnspan=4,sticky="nsew")



    


    root.mainloop()

click()