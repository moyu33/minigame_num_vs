#importazione moduli random & time
import random
import time

def gameNum():

    #inizializzazione variabili per gestire le vittorie
    vittorie_umano = 0
    vittorie_computer = 0

    print("Game Start!")

    #creazione ciclo while per gestire conclusione gioco quando umano o computer arriva a 5 vittorie
    while vittorie_umano < 3 and vittorie_computer < 3:

    #scelta computer
        print("Il Computer sta pensando...")
        time.sleep(3)
        scelta_computer = random.choice(range(1, 6))
        print("Il Computer ha scelto.")

    #creazione ciclo per gestire scelta umano non valida
        while True:
            try:
                scelta_giocatore = int(input("Scegli un numero tra 1 e 5: "))
                if scelta_giocatore < 1 or scelta_giocatore > 5:
                    print("Per favore inserisci un valore valido tra 1 e 5.")
                    continue 
                break
            except ValueError:
                print("Per favore inserisci un valore numerico valido.")
                continue
            
        time.sleep(2)
        print("Computer ha scelto {}".format(scelta_computer))

    #gestione conteggio vittorie
        if scelta_computer > scelta_giocatore:
            vittorie_computer += 1
            print("COMPUTER VINCE.")
        elif scelta_computer < scelta_giocatore:
            vittorie_umano += 1
            print("UMANO VINCE.")
        else:
            print("QUESTO È UN PAREGGIO!")

    if vittorie_umano == 3:
        print("UMANO VINCE LA SFIDA!")
    elif vittorie_computer == 3:
        print("COMPUTER VINCE LA SFIDA!")


    if vittorie_umano > vittorie_computer:
        print("L'umano ha vinto {} volte".format(vittorie_umano))
    elif vittorie_umano < vittorie_computer:
        print("Il computer ha vinto {} volte".format(vittorie_computer))  

    print("Game Over")

gameNum()

#fine gioco
input("Press Enter to exit...")
