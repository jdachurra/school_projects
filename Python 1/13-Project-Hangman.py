'''
Mihail Zuniga
mihail.zunigaona@tuni.fi
student number: 152235231

Jose Achurra 
jose.achurrasantos(at)tuni.fi
stundent number: 151487475
PROJECT: BATTLESHIP
'''

import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        """
        Hangman Game - Graphical User Interface

        This Hangman game allows the player to guess a randomly selected word.
        The player has a limited number of attempts to guess the word.

        Usage:
        - Enter a single letter in the Entry field and press the "Guess" button.
        - The word to guess is displayed with underscores representing unknown letters.
        - The player has a maximum of 6 incorrect guesses.
        - Duplicate guesses or invalid inputs will be handled with error messages.

        Have fun playing Hangman!

        :param master: Tkinter root window
        """
        self.master = master
        self.master.title("Hangman Game")

        self.word_list = ["python", "hangman", "programming", "interface", "project", "assignment", "example", "tampere", "suomi", "fancy", "gaming"]
        self.word_to_guess = ""
        self.max_attempts = 5
        self.guesses_left = 0
        self.current_word_state = []

        self.create_widgets()

    def create_widgets(self):
        '''
        this function creates the widgets for the game
        the widgets are the labels, entry, buttons and the pack
        '''
        self.word_label = tk.Label(self.master, text="Word: ")
        self.word_label.pack()

        self.word_display = tk.Label(self.master, text="")
        self.word_display.pack()

        self.attempts_label = tk.Label(self.master, text="Attempts left:")
        self.attempts_label.pack()

        self.guess_label = tk.Label(self.master, text="Enter a letter:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

        self.new_game_button = tk.Button(self.master, text="New Game", command=self.new_game)
        self.new_game_button.pack()

        self.new_game()

    def new_game(self):
        '''
        this function creates a new game
        it chooses a random word from the word list
        it also resets the current word state and the guesses left
        it also updates the word display and the attempts label
        it also shows a message box with the instructions
        '''
        self.word_to_guess = random.choice(self.word_list)
        self.current_word_state = ["_"] * len(self.word_to_guess)
        self.guesses_left = self.max_attempts

        self.update_word_display()
        self.update_attempts_label()

        messagebox.showinfo("Game Start", f"Welcome to Hangman! Try to guess the word.\nYou have {self.guesses_left} attempts.")

    def update_word_display(self):
        '''
        this function updates the word display
        it joins the current word state with spaces in between
        '''
        self.word_display.config(text=" ".join(self.current_word_state))

    def update_attempts_label(self):
        '''
        this function updates the attempts label
        it shows the number of guesses left
        '''
        self.attempts_label.config(text=f"Attempts left: {self.guesses_left}")

    def make_guess(self):
        '''
        this function makes a guess
        it checks if the guess is valid
        it checks if the guess is a duplicate
        it checks if the guess is in the word
        it updates the word display
        it checks the game status
        '''
        guess = self.guess_entry.get().lower()

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showerror("Invalid Guess", "Please enter a single letter.")
            return

        if guess in self.current_word_state:
            messagebox.showinfo("Duplicate Guess", "You've already guessed this letter.")
            return

        if guess in self.word_to_guess:
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == guess:
                    self.current_word_state[i] = guess
            self.update_word_display()
        else:
            self.guesses_left -= 1

        self.update_attempts_label()
        self.check_game_status()

    def check_game_status(self):
        '''
        this function checks the game status
        it checks if the word has been guessed
        it checks if the player has run out of guesses
        it asks the player if they want to continue
        '''
        if "_" not in self.current_word_state:
            messagebox.showinfo("Congratulations", f"You guessed the word! You win!\nThe word was: {self.word_to_guess}")
            self.ask_to_continue()
        elif self.guesses_left == 0:
            messagebox.showinfo("Game Over", f"You ran out of guesses. The word was: {self.word_to_guess}")
            self.ask_to_continue()

    def ask_to_continue(self):
        '''
        this function asks the player if they want to continue
        it disables the board if the player chooses to quit
        it creates a new game if the player chooses to continue
        '''
        response = messagebox.askyesno("Continue?", "Do you want to play another round?")
        if response:
            self.new_game()
        else:
            self.disable_board()
            messagebox.showinfo("Thanks for playing!", "Thanks for playing Hangman!")

    def disable_board(self):
        '''
        this function disables the board
        it disables the entry, guess button and new game button
        '''
        self.guess_entry.config(state="disabled")
        self.guess_button.config(state="disabled")
        self.new_game_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()