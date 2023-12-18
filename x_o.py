import random
import tkinter as tk
win_attempts = 0
lose_attempts = 0
def color_but(a,b,c):
     d = a.cget("text")
     e = b.cget("text")
     f = c.cget("text")
     if d == e == f == "X":
          a.config(bg="aqua")
          b.config(bg="aqua")
          c.config(bg="aqua")
def restart ():
    buttons_s = [t1,t2,t3,t4,t5,t6,t7,t8,t9]
    for a in buttons_s:
         if a not in buttons:
              buttons.append(a)
    for b in buttons:
        b.config(text="",state=tk.NORMAL,bg=default_color)
    winbox.config(text="")
def change_text(button):
        global win_attempts, lose_attempts
        button.config(text="X", state=tk.DISABLED)
        buttons.remove(button)
        tx1 = t1.cget("text")
        tx2 = t2.cget("text")
        tx3 = t3.cget("text")
        tx4 = t4.cget("text")
        tx5 = t5.cget("text")
        tx6 = t6.cget("text")
        tx7 = t7.cget("text")
        tx8 = t8.cget("text")
        tx9 = t9.cget("text")
        if (tx1 == tx2 == tx3 == "X") or \
            (tx4 == tx5 == tx6 == "X") or \
            (tx7 == tx8 == tx9 == "X") or \
            (tx1 == tx4 == tx7 == "X") or \
            (tx2 == tx5 == tx8 == "X") or \
            (tx3 == tx6 == tx9 == "X") or \
            (tx1 == tx5 == tx9 == "X") or \
            (tx3 == tx5 == tx7 == "X"):
            t1.config(state=tk.DISABLED)
            t2.config(state=tk.DISABLED)
            t3.config(state=tk.DISABLED)
            t4.config(state=tk.DISABLED)
            t5.config(state=tk.DISABLED)
            t6.config(state=tk.DISABLED)
            t7.config(state=tk.DISABLED)
            t8.config(state=tk.DISABLED)
            t9.config(state=tk.DISABLED)
            win_attempts = win_attempts + 1
            color_but(t1,t2,t3)
            color_but(t4,t5,t6)
            color_but(t7,t8,t9)
            color_but(t1,t4,t7)
            color_but(t2,t5,t8)
            color_but(t3,t6,t9)
            color_but(t3,t5,t7)
            color_but(t1,t5,t9)
            winbox.config(text="You Win")
            l2.config(text=f"User Wins: {win_attempts}")
        elif not buttons:
             print("there is a tie")
             winbox.config(text="Tie, No Winner")
        elif buttons:
            random_button = random.choice(buttons)
            random_button.config(text="O", state=tk.DISABLED)
            buttons.remove(random_button)
            tx1 = t1.cget("text")
            tx2 = t2.cget("text")
            tx3 = t3.cget("text")
            tx4 = t4.cget("text")
            tx5 = t5.cget("text")
            tx6 = t6.cget("text")
            tx7 = t7.cget("text")
            tx8 = t8.cget("text")
            tx9 = t9.cget("text")
            if (tx1 == tx2 == tx3 == "O") or \
                (tx4 == tx5 == tx6 == "O") or \
                (tx7 == tx8 == tx9 == "O") or \
                (tx1 == tx4 == tx7 == "O") or \
                (tx2 == tx5 == tx8 == "O") or \
                (tx3 == tx6 == tx9 == "O") or \
                (tx1 == tx5 == tx9 == "O") or \
                (tx3 == tx5 == tx7 == "O"):
                t1.config(state=tk.DISABLED)
                t2.config(state=tk.DISABLED)
                t3.config(state=tk.DISABLED)
                t4.config(state=tk.DISABLED)
                t5.config(state=tk.DISABLED)
                t6.config(state=tk.DISABLED)
                t7.config(state=tk.DISABLED)
                t8.config(state=tk.DISABLED)
                t9.config(state=tk.DISABLED)
                lose_attempts = lose_attempts + 1
                print("You Lose")
                winbox.config(text="You Lose")
                color_b = [t1,t2,t3,t4,t5,t6,t7,t8,t9]
                for b in color_b:
                     b.config(bg="red")
                l1.config(text=f"PC Wins: {lose_attempts}")
            elif not buttons:
                 print("There is a tie")
                 winbox.config(text="Tie, No Winner")


window = tk.Tk()
window.title("XO Game")
window.minsize(width=300,height=300)
lframe = tk.Frame(window,relief="raised")
lframe.grid(column=2,row=0,padx=10, pady=10,sticky="nsew")
l1 = tk.Label(lframe,text=f"Pc Wins: {lose_attempts}")
l1.grid(column=0,row=0,sticky="nsew")
l2 = tk.Label(lframe,text=f"User Wins: {win_attempts}")
l2.grid(column=1,row=0,sticky="nsew")
winbox = tk.Label(window,font=40)
winbox.grid(column=2,row=1,sticky="nsew")
rs = tk.Button(window,font=25,text="Restart",command=restart)
rs.grid(column=2,row=2,sticky="nsew")
frame = tk.Frame(window,relief="raised")
frame.grid(column=2, row=3, padx=10, pady=10,sticky="nsew")
t1 = tk.Button(frame,font=25,command=lambda:change_text(t1),fg="black")
t1.grid(column=0,row=0,sticky="nsew")
t2 = tk.Button(frame,font=25,command=lambda:change_text(t2),fg="black")
t2.grid(column=1,row=0,sticky="nsew")
t3 = tk.Button(frame,font=25,command=lambda:change_text(t3),fg="black")
t3.grid(column=2,row=0,sticky="nsew")
t4 = tk.Button(frame,font=25,command=lambda:change_text(t4),fg="black")
t4.grid(column=0,row=1,sticky="nsew")
t5 = tk.Button(frame,font=25,command=lambda:change_text(t5),fg="black")
t5.grid(column=1,row=1,sticky="nsew")
t6 = tk.Button(frame,font=25,command=lambda:change_text(t6),fg="black")
t6.grid(column=2,row=1,sticky="nsew")
t7 = tk.Button(frame,font=25,command=lambda:change_text(t7),fg="black")
t7.grid(column=0,row=2,sticky="nsew")
t8 = tk.Button(frame,font=25,command=lambda:change_text(t8),fg="black")
t8.grid(column=1,row=2,sticky="nsew")
t9 = tk.Button(frame,font=25,command=lambda:change_text(t9),fg="black")
t9.grid(column=2,row=2,sticky="nsew")
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(0,weight=1)
frame.rowconfigure(1,weight=1)
frame.rowconfigure(2,weight=1)
lframe.columnconfigure(0, weight=1)
lframe.columnconfigure(1, weight=1)
lframe.rowconfigure(0,weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
buttons = [t1,t2,t3,t4,t5,t6,t7,t8,t9]
default_color = t1.cget("bg")
window.mainloop()

   
    
        
        
    



