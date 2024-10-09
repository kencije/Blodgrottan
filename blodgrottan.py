import os

# Funktion för att pausa och vänta på att spelaren trycker på valfri tangent
def forsättsist():
    input("Tryck på vilken knapp som helst för att fortsätta...")
def fortsätt():
    input("")

# Visa första delen av texten
print("Blodgrottan")
print("===========")
fortsätt()

# Be spelaren om sitt namn
name = input("Vad heter du, grottman? : ")

# Visa nästa del och pausa mellan varje steg
print(f"Du är grottmannen {name}, och nu ska du strida mot grottmannen dingleberry.")
fortsätt()

print("Ni står i en stor grotta, omgiven av hungriga ögon från stammedlemmar.")
fortsätt()

print("Stämningen är spänd, och alla väntar på att se vem som blir den starkaste.")
fortsätt()

print("Du har inga vapen, bara din styrka och mod. Du är klädd i ett par korta läderbyxor, som är gjorda av djurens skinn. Ditt bröst är naket, och musklerna glänser i det svaga ljuset från elden.")
fortsätt()

print("Stammedlemmarna sitter runt omkring er, deras hjärtan slår hårt av förväntan.")
fortsätt()

print("Postumius gör sig redo, hans blick är hård som stål, och han förbereder sig för att anfalla.")
fortsätt()

print("Striden kan börja när som helst.\n")
forsättsist()
