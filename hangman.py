"""
Hangman is a classic word game in which you must guess as many secret words as you can before time runs out! 
"""
import random
import re


class Hangman:
    inputs = []

    def __init__(self):
        self.words = ["python", "java", "kotlin", "javascript"]
        self.choose = random.choice(self.words)
        self.initial = "-" * len(self.choose)

    def error_check(self, letter):
        if len(letter) > 1:
            print("You should input a single letter")
            return True
        if not letter.islower():
            print("It is not an ASCII lowercase letter")
            return True

    def play(self):
        counter = 0
        while counter < 8:
            print()
            print(self.initial)
            letter = input("Input a letter: ")
            if self.error_check(letter):
                continue
            if letter in Hangman.inputs:
                print("You already typed this letter")
                continue
            Hangman.inputs.append(letter)
            if letter in self.choose:
                position = [m.start() for m in re.finditer(letter, self.choose)]
                for pos in position:
                    self.initial = (
                        self.initial[:pos] + letter + self.initial[pos + 1 :]
                    )
            else:
                counter += 1
                print("No such letter in the word")

        if self.choose == self.initial:
            print("{}\nYou guessed the word!\nYou survived!".format(self.choose))
        else:
            print("You are hanged!")
        
    def menu(self):
        while True:
            choice = input('Type "play" to play the game, "exit" to quit:')
            if choice == "play":
                self.play()
            elif choice == "exit":
                exit()
            else:
                continue
        


if __name__ == "__main__":
    print("H A N G M A N")
    game = Hangman()
    game.menu()
