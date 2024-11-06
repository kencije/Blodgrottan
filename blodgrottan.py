import random

namelist = ["dongelbär", "honk", "bertimus", "bang", "meow", "woof", "fjärilsförstörare", "sten", "pinne"]
listdifficulty = []
listcharacter = []
listattack = []

# Funktion för att pausa och vänta på att spelaren trycker på valfri tangent
def forsättsist():
    input("Tryck på vilken knapp som helst för att fortsätta...")

def enter():
    input("Klicka på enter för att fortsätta...")


# Klassdefinitioner för Attack, Svårighet och Karaktär
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

# Skapa svårigheter, karaktärer och attacker
def setup_game():
    Difficulty("Noob", 0.5)
    Difficulty("Pro", 1)
    Difficulty("Haxer", 2)

    Character("Honkel the 5th", 16)
    Character("Dongles", 12)
    Character("Female character 1", 8)

    Attack("Slag", 1, 70)
    Attack("Spark", 3, 40)
    Attack("Smack", 2, 60)
    Attack("Headbutt", 5, 10)

# Välj karaktär och svårighet
def choose_character():
    while True:
        your_choice = input("Vilken karaktär vill du välja? \n - Honkel the 5th \n - Dongles \n - Female character 1 \n Karaktär: ")
        for char in listcharacter:
            if char.namn.lower() == your_choice.lower():
                print(f"Du valde {char.namn}")
                return char
        print("Ogiltigt val, försök igen.")

def choose_difficulty():
    while True:
        your_choice = input("\nVilken svårighet vill du välja? \n - Noob \n - Pro \n - Haxer\n \nSvårighet: ")
        for diff in listdifficulty:
            if diff.namn.lower() == your_choice.lower():
                print(f"Du valde {diff.namn}")
                return diff
        print("Ogiltigt val, försök igen.")

# Visa hälsa
def display_health(character):
    health_bar = "♥" * character.health + "♡" * (character.health - character.health)
    print(f"HP: {health_bar} ({character.health}/{character.health})")

# Välj attack
def choose_attack():
    print("\nVälj din attack:")
    for i, attack in enumerate(listattack, start=1):
        print(f"{i}. {attack.namn} - Damage: {attack.damage}, Chance: {attack.chance}%")
    
    while True:
        choice = input("Välj attack nummer: ")
        if choice.isdigit() and 1 <= int(choice) <= len(listattack):
            return listattack[int(choice) - 1]
        print("Ogiltigt val, försök igen.")

# Strid
def battle(player, opponent, difficulty):
    print(f"\nStriden börjar mellan {player.namn} och {opponent.namn}!")
    fortsätt()

    while player.health > 0 and opponent.health > 0:
        # Spelaren väljer en attack
        player_attack = choose_attack()
        
        # Beräkna om attacken träffar baserat på sannolikheten
        if random.randint(1, 100) <= player_attack.chance:
            damage_done = int(player_attack.damage * difficulty.multi)
            opponent.health -= damage_done
            print(f"{player.namn} träffar med {player_attack.namn} och gör {damage_done} skada!")
        else:
            print(f"{player.namn}'s {player_attack.namn} missar!")
        
        # Kontrollera om motståndaren är besegrad
        if opponent.health <= 0:
            print(f"{opponent.namn} har besegrats! Du vann!")
            return
        
        # Motståndarens tur att anfalla
        opponent_attack = random.choice(listattack)
        if random.randint(1, 100) <= opponent_attack.chance:
            damage_done = opponent_attack.damage
            player.health -= damage_done
            print(f"{opponent.namn} träffar med {opponent_attack.namn} och gör {damage_done} skada!")
        else:
            print(f"{opponent.namn}'s {opponent_attack.namn} missar!")
        
        # Kontrollera om spelaren är besegrad
        if player.health <= 0:
            print(f"{player.namn} har besegrats! Du förlorade.")
            return
        
        # Visa båda karaktärernas hälsa
        print(f"\n{player.namn}'s hälsa: {player.health}")
        print(f"{opponent.namn}'s hälsa: {opponent.health}")
        fortsätt()

# Starta spelet
def start_game():
    print("Blodgrottan")
    print("===========")
    enter()
    
    name = input("\nVad heter du grottman? ")
    randomname = random.choice(namelist)
    print(f"Du är grottmannen {name}, och nu ska du strida mot grottmannen {randomname}.")
    enter()
    print("Ni står i en stor grotta, omgiven av hungriga ögon från stammedlemmar.")
    enter()
    print("Stämningen är spänd, och alla väntar på att se vem som blir den starkaste.")
    enter()

def main():
    setup_game()
    start_game()
    player = choose_character()
    opponent = random.choice(listcharacter)
    difficulty = choose_difficulty()
    
    # Starta striden
    battle(player, opponent, difficulty)

main()