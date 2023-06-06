import random

print("aceitas uma rodada de forca?")
palavras = ["cavalo", "dinossauro", "fralda", "mamada"]

escolha = random.choice(palavras)
display = []

for numero in range(len(escolha)):
    display.append("_")
print("a palavra tem", numero+1, "letras")
print(display) 
   

vida = 6

while vida > 0 and "_" in display:
    cont = 0
    acerto = False
    chute = input("mande seu palpite  ")
    for letra in escolha:
        if chute in letra:
            display[cont]=chute
            print(display)
            acerto = True
        cont += 1
    if not acerto:
        vida -= 1
    print("tens ", vida, "vidas sobrando") 
if vida == 0:
    print("perdeste seu besta")
    print("nao descobriste que a palavra era " +escolha)
else:
    print("es uma lenda, ganhaste")
    print("poucos saberiam que a palvra era " +escolha)