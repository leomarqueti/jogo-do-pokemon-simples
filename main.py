from mimetypes import init
from pokemons import *

if __name__ == "__main__":
    print("---------------------POKEMON-------------------------")
    print("")

    print("Bem-vindo as batalhas de pokemons!")
    print("")


    while True:
        print("-------------------------------------------------")
        print("[1] Batalhar")
        print("[0] Sair")
        escolha_usuario = input("Qual deseja: ")
        print("------------------------------------")

        if (escolha_usuario == "1"):
            pokemon_adversario = Pokemons()
            pokemon_inicial().atacar(pokemon_adversario)
        elif (escolha_usuario == "0"):
            print("")
            print("Finalizando...")
            break
        else: 
            print("")
            print("Ocorreu um erro!")
        