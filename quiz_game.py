print("Welcome To My Game Are You Ready To Die? >:)")

playing = input("Do you want play this game? YOU ARE READY?: ")

if playing != "Yes":
    quit()

print("Carregando jogo BIP BOP <|O_O|>")




def pergunta(pergunta, aswer):
    if aswer == pergunta:
        print("Acertou")
    else:
        print("Erooooooou!")

pergunta(input("terra dos moinhos e ventos, E um pais da EUROPA, seu idioma e o HOLÂNDES: "), "Italia")
