import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9

        # Create buttons
        self.buttons = []
        for i in range(9):
            row, col = i // 3, i % 3
            button = tk.Button(self.window, text="", font=('normal', 20), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)

            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Draw", "The game is a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ""):
                return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="", state=tk.NORMAL)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
