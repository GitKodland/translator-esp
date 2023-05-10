import random
import time


eng_words = ['Hi','Bye','Task', 'Programm']
sp_words = ['Hola','Adiós','Tarea', 'Programa']
score = 0

mode = input("Elige un modo: 0 - añadir nuevas palabras, 1 - entrenamiento: \n")
while ((mode != '0') and (mode != '1')):
    mode = input("Símbolo no válido. Elija 0 o 1. (0 añade nuevas palabras, mientras que 1 permite el entrenamiento) \n")

if mode == "1":
    print("¡Traduce tantas palabras como puedas! ¡Tienes 10 intentos!")
    for i in range(10):
        number = random.randint(0, len(eng_words)-1)
        print("Cómo deberíamos traducirlo " + eng_words[number])
        if input() == sp_words[number]:
            print("¡¡¡Genial!!!")
            score += 1
        else:
            print("No, no del todo... La palabra correcta es - " + eng_words[number])
else:
    word = input("Escribe una palabra en español: ")
    translate = input("Escriba la traducción de esta palabra: ")
    if len(word) > 0 and len(translate) > 0:
        sp_words.append(word)
        eng_words.append(translate)
        print("La palabra se ha añadido correctamente")
