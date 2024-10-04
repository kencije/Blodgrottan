import random

class Gladiator:

    def __init__(self, namn):
        self.namn = namn
        self.hälsa = 100

    def slå(self, motståndare):
        skada = random.randint(5, 15)
        motståndare.hälsa -= skada
        print(f"{self.namn} slår {motståndare.namn} för {skada} skada!")

    def sparka(self, motståndare):
        skada = random.randint(10, 20)
        motståndare.hälsa -= skada
        print(f"{self.namn} sparkar {motståndare.namn} för {skada} skada!")

    def bitas(self, motståndare):
        skada = random.randint(5, 10)
        motståndare.hälsa -= skada
        print(f"{self.namn} biter {motståndare.namn} för {skada} skada!")

    def kasta(self, motståndare):
        skada = random.randint(15, 25)
        motståndare.hälsa -= skada
        print(f"{self.namn} kastar {motståndare.namn} för {skada} skada!")

    def är_vid_liv(self):
        return self.hälsa > 0

def välj_attack(spelare):
    print("\nVälj din attack:")
    print("1. Slå")
    print("2. Sparka")
    print("3. Bitas")
    print("4. Kasta")
    val = input("Ditt val: ")
    
    if val == "1":
        return spelare.slå
    elif val == "2":
        return spelare.sparka
    elif val == "3":
        return spelare.bitas
    elif val == "4":
        return spelare.kasta
    else:
        print("Ogiltigt val, du gör ett slag!")
        return spelare.slå

def starta_kamp(gladiator_spelare, gladiator_ai):
    while gladiator_spelare.är_vid_liv() and gladiator_ai.är_vid_liv():

        attack = välj_attack(gladiator_spelare)
        attack(gladiator_ai)

        if not gladiator_ai.är_vid_liv():
            break

        attack = random.choice([gladiator_ai.slå, gladiator_ai.sparka, gladiator_ai.bitas, gladiator_ai.kasta])
        attack(gladiator_spelare)

        print(f"{gladiator_spelare.namn}: {gladiator_spelare.hälsa} HP | {gladiator_ai.namn}: {gladiator_ai.hälsa} HP\n")

    vinnare = gladiator_spelare if gladiator_spelare.är_vid_liv() else gladiator_ai
    print(f"{vinnare.namn} vinner kampen!")

print("Du vaknar framför en dörr...")
print("Dörren öppnas långsamt och du ser en stor arena...")
print("Utropare: Välkommen till gladiatorerna!")
print("Utropare: Nu skall blod spillas!\n")

gladiator_spelare = Gladiator("Spelaren")
gladiator_ai = Gladiator("AI Gladiator")

starta_kamp(gladiator_spelare, gladiator_ai)
