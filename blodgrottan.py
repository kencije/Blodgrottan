import os
import random

namelist = ["dongelbär" , "honk" , "bertimus" , "bang" , "meow" , "woof", "fjärilsförstörare", "sten", "pinne"]
randomname = random.choice(namelist)
listdifficulty = []

# Funktion för att pausa och vänta på att spelaren trycker på valfri tangent
def forsättsist():
    input("Tryck på vilken knapp som helst för att fortsätta...")
def fortsätt():
    input("")
class Difficulty:
    def __init__(self, namn, multi):
        self.namn = namn
        self.multi = multi
        listdifficulty.append(self)

class Character:
    def __init__(self, namn, health):
        self.namn = namn
        self.health = health
        


print("Blodgrottan")
print("===========")
fortsätt()

#Svårigheter (MULTI)
easy = Difficulty("Noob", 0.5)
medium = Difficulty("Pro", 1)
hard = Difficulty("Haxer", 2)

#Karaktärer (HEALTH)
guy_1 = Character("Honkel the 5th", 8)

def choose_character():
    your_choice2 = input("Vilken karaktär vill du välja? \n ")
    print

def choose_difficulty():
    your_choice = input("Vilken svårighet vill du välja? \n Noob \n Pro \n Haxer ")

    for diff in listdifficulty:
        if diff.namn.lower() == your_choice.lower():
            difficulty_name = diff.namn
            print(f"Du valde {difficulty_name}")
choose_difficulty()




    

name = input("Vad heter du, grottman? ")


print(f"Du är grottmannen {name}, och nu ska du strida mot grottmannen {randomname}.")
fortsätt()

print("Ni står i en stor grotta, omgiven av hungriga ögon från stammedlemmar.")
fortsätt()

print("Stämningen är spänd, och alla väntar på att se vem som blir den starkaste.")
fortsätt()

print("Du har inga vapen, bara din styrka och mod. Du är klädd i ett par korta läderbyxor, som är gjorda av djurens skinn. Ditt bröst är naket, och musklerna glänser i det svaga ljuset från elden.")
fortsätt()

print("Stammedlemmarna sitter runt omkring er, deras hjärtan slår hårt av förväntan.")
fortsätt()

print(f"{randomname} gör sig redo, hans blick är hård som stål, och han förbereder sig för att anfalla.")
fortsätt()

print("Striden kan börja när som helst.\n")
forsättsist()