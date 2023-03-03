import random
import time


eng_words = ['Hi','Bye','Task', 'Programm']
fr_words = ['Salut','Au revoir','Tâche', 'Programme']
score = 0

mode = input("Pick a mode: 0 - add new words, 1 - training: \n")
while ((mode != '0') and (mode != '1')):
    mode = input("Invalid dymbol! Pick either 0 or 1. (0 adds new words, while 1 enables training) \n")

if mode == "1":
    print("Translate as many words as you can! You have 10 attempts!")
    for i in range(10):
        number = random.randint(0, len(eng_words))
        print("How should we translate: " + eng_words[number])
        if input() == fr_words[number]:
            print("Great!!!")
            score += 1
        else:
            print("Nope, not quite... The correct word is - " + eng_words[number])
else:
    word = input("Type in an English word: ")
    translate = input("Type in this word's translation: ")
    if len(word) > 0 and len(translate) > 0:
        eng_words.append(word)
        fr_words.append(translate)
        print("The word was added successfully!")
