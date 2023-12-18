import random
import tkinter as tk

win_attempts = 0
lose_attempts = 0

def color_buttons(buttons_to_color):
    for button in buttons_to_color:
        button.config(bg="aqua")

def restart():
    global win_attempts, lose_attempts
    for button in buttons:
        button.config(text="", state=tk.NORMAL, bg=default_color)
    winbox.config(text="")
    win_attempts = 0
    lose_attempts = 0
    update_labels()

def check_winner(symbol):
    for combo in winning_combinations:
        if all(buttons[i].cget("text") == symbol for i in combo):
            color_buttons([buttons[i] for i in combo])
            return True
    return False

def update_labels():
    l1.config(text=f"PC Wins: {lose_attempts}")
    l2.config(text=f"User Wins: {win_attempts}")

def change_text(button):
    global win_attempts, lose_attempts
    symbol = "X"
    opponent_symbol = "O"

    button.config(text=symbol, state=tk.DISABLED)
    buttons.remove(button)

    if check_winner(symbol):
        disable_all_buttons()
        win_attempts += 1
        winbox.config(text="You Win")
        update_labels()
    elif not buttons:
        print("There is a tie")
        winbox.config(text="Tie, No Winner")
    else:
        random_button = random.choice(buttons)
        random_button.config(text=opponent_symbol, state=tk.DISABLED)
        buttons.remove(random_button)

        if check_winner(opponent_symbol):
            disable_all_buttons()
            lose_attempts += 1
            winbox.config(text="You Lose")
            color_buttons(buttons)
            update_labels()

def disable_all_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

window = tk.Tk()
window.title("XO Game")
window.minsize(width=300, height=300)

lframe = tk.Frame(window, relief="raised")
lframe.grid(column=2, row=0, padx=10, pady=10, sticky="nsew")

l1 = tk.Label(lframe, text=f"PC Wins: {lose_attempts}")
l1.grid(column=0, row=0, sticky="nsew")

l2 = tk.Label(lframe, text=f"User Wins: {win_attempts}")
l2.grid(column=1, row=0, sticky="nsew")

winbox = tk.Label(window, font=40)
winbox.grid(column=2, row=1, sticky="nsew")

rs = tk.Button(window, font=25, text="Restart", command=restart)
rs.grid(column=2, row=2, sticky="nsew")

frame = tk.Frame(window, relief="raised")
frame.grid(column=2, row=3, padx=10, pady=10, sticky="nsew")

buttons = []

for _ in range(9):
    button = tk.Button(frame, font=25, command=lambda b=buttons[-1] if buttons else None: change_text(b), fg="black")
    buttons.append(button)
buttons = [tk.Button(frame, font=25, command=lambda button=button: change_text(button), fg="black") for button in range(9)]

default_color = buttons[0].cget("bg") if buttons else "white"

for i, button in enumerate(buttons):
    button.grid(column=i % 3, row=i // 3, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

lframe.columnconfigure(0, weight=1)
lframe.columnconfigure(1, weight=1)
lframe.rowconfigure(0, weight=1)

window.columnconfigure(2, weight=1)
window.rowconfigure(3, weight=1)

winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

default_color = buttons[0].cget("bg")

window.mainloop()
