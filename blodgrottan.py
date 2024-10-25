import os
import random

namelist = ["dongelbär" , "honk" , "bertimus" , "bang" , "meow" , "woof", "fjärilsförstörare", "sten", "pinne"]
randomname = random.choice(namelist)
listdifficulty = []
listcharacter = []
listattack = []

# Funktion för att pausa och vänta på att spelaren trycker på valfri tangent
def forsättsist():
    input("Tryck på vilken knapp som helst för att fortsätta...")
def fortsätt():
    input("")
class Attack:
    def __init__(self, namn, damage, chance):
        self.namn = namn
        self.damage = damage
        self.chance = chance
        listattack.append(self)


class Difficulty:
    def __init__(self, namn, multi):
        self.namn = namn
        self.multi = multi
        listdifficulty.append(self)

class Character:
    def __init__(self, namn, health):
        self.namn = namn
        self.health = health
        listcharacter.append(self)


print("Blodgrottan")
print("===========")
fortsätt()

#Svårigheter (MULTI)
easy = Difficulty("Noob", 0.5)
medium = Difficulty("Pro", 1)
hard = Difficulty("Haxer", 2)

#Karaktärer (HEALTH)
guy_1 = Character("Honkel the 5th", 16)
guy_2 = Character("Dongles", 12)
guy_3 = Character("Female character 1", 8)

#Attack (DAMAGE, CHANCE)
attack_1 = Attack("Slag", 1, 70)
attack_2 = Attack("Spark", 3, 40)
attack_3 = Attack("Smack", 2, 60)
attack_4 = Attack("Headbutt", 5, 10)

your_choice2 = None

def choose_character():
    while True:
        global your_choice2
        your_choice2 = input("Vilken karaktär vill du välja? \n - Honkel the 5th \n - Dongles \n - Female character 1 \n Karaktär: ")
        for diff in listcharacter:
            if diff.namn.lower() == your_choice2.lower():
                character_name = diff.namn
                print(f"Du valde {character_name}")
                return



choose_character()

def choose_difficulty():
    while True:
        your_choice = input("\nVilken svårighet vill du välja? \n - Noob \n - Pro \n - Haxer\n \n - Svårighet: ")
        for diff in listdifficulty:
            if diff.namn.lower() == your_choice.lower():
                difficulty_name = diff.namn
                print(f"Du valde {difficulty_name}")
                return

choose_difficulty()

def display_health(current_health, max_health):
    # Skapa en hälsorad med fyllda hjärtan för nuvarande hälsa och tomma hjärtan för förlorad hälsa
    health_bar = "♥" * current_health + "♡" * (max_health - current_health)
    # Returnera strängen som visar hälsoraden och numeriska värden
    return f"HP: {health_bar} ({current_health}/{max_health})"

# Exempel på användning i ditt spel:
def update_health_display():
    # Hämta karaktärens nuvarande hälsa och maxhälsa
    for char in listcharacter:
        if char.namn.lower() == your_choice2.lower():
            max_health = char.health
            current_health = char.health  # Detta skulle uppdateras under strid
            
            # Visa hälsoraden
            health_status = display_health(current_health, max_health)
            print(health_status)
            return health_status


# Till exempel, om en karaktär har 8 i hälsa, skulle det visa:
# HP: ♥♥♥♥♥♥♥♥ (8/8)
# Om de tar 3 i skada:
# HP: ♥♥♥♥♥♡♡♡ (5/8)

def attack_choice():
    random_chance = random.randint(0, 100)
    choose_attack = input("Välj din attack: ")
    


name = input("\nVad heter du grottman? ")


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

# Efter varje attack eller hälsoförändring kan du anropa:
update_health_display()