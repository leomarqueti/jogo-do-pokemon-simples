import random
import time

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

TIPOS = ["fogo","agua","eletrico"]

NOMES_POKEMONS_FOGO = [
    "charmander",
    "Vulpix",
    "Charizard",
    "Delphox",
    "Chimchar"
    ]

NOMES_POKEMONS_AGUA = [
    "Squirdle",
    "Totodile",
    "Poliwhirl",
    "Marill",
    "Psyduck"
    ]

NOMES_POKEMONS_ELETRICO = [
    "Pikachu",
    "Pichu",
    "Electrode",
    "Voltorb",
    "Raichu"
    ]


class Pokemons:

    
    def __init__(self,nome=None,tipo=None,level=None,vida=None):

        self.pokemons = []
        
        self.nome = nome

        if (level):
            self.level = level
        else: 
            self.level = random.randint(1,100)

        if (vida):
            self.vida = vida
        else:
            self.vida = 500


        if (tipo):
            if (tipo == "fogo"):
                self.tipo = "fogo"
                self.nome = random.choice(NOMES_POKEMONS_FOGO)
            elif (tipo == "agua"):
                self.tipo = "agua"
                self.nome = random.choice(NOMES_POKEMONS_AGUA)
            elif (tipo == "eletrico"):
                self.tipo = "eletrico"
                self.nome = random.choice(NOMES_POKEMONS_ELETRICO)
            else:
                self.tipo = tipo
                self.nome = nome
        else:
            tipo_aleatorio = random.choice(TIPOS)

            if (tipo_aleatorio == "fogo"):
                self.tipo = "fogo"
                self.nome = random.choice(NOMES_POKEMONS_FOGO)
            elif (tipo_aleatorio == "agua"):
                self.tipo = "agua"
                self.nome = random.choice(NOMES_POKEMONS_AGUA)
            elif (tipo_aleatorio == "eletrico"):
                self.tipo = "eletrico"
                self.nome = random.choice(NOMES_POKEMONS_ELETRICO)
            else:
                self.tipo = tipo
                self.nome = nome

        
    def __str__(self):
        return ("{} - level {} ({})".format(self.nome,self.level,self.tipo))


    def atacar(self,pokemon_adversario):

        print("------------------BATALHA--------------------")
        time.sleep(2)
        print("")

        time.sleep(2)
        print("Vai começar a BATALHA POKEMON!")
        print("")
        time.sleep(2)
        print("A luta sera {} contra {}".format(self,pokemon_adversario))
        time.sleep(2)
        print("Vai começar em...")
        time.sleep(2)
        print("3")
        time.sleep(2)
        print("2")
        time.sleep(2)
        print("1")
        time.sleep(2)

        print("Adversario - '{} EU ESCOLHO VOCE!".format(pokemon_adversario.nome))
        time.sleep(2)


        while True:

            self.vida = self.vida - random.randint(20,50) - pokemon_adversario.level
            print("{} atacou o {} : Vida {} . Vida {}".format(pokemon_adversario,self,pokemon_adversario.vida,self.vida))

            pokemon_adversario.vida = pokemon_adversario.vida - random.randint(20,50) - self.level
            print("{} atacou o {} : Vida {} . Vida {}".format(self,pokemon_adversario,self.vida,pokemon_adversario.vida))

            if (self.vida <= 0):
                print("")
                print("-------------------------------------------------------")
                print("{} perdeu a batalha para o {}".format(self,pokemon_adversario))
                print("-------------------------------------------------------")
                print(bcolors.OK + "{} GANHOU".format(pokemon_adversario) + bcolors.RESET)
                break
            elif (pokemon_adversario.vida <= 0):
                print("")
                print("-------------------------------------------------------")
                print("{} perdeu a batalha para o {}".format(pokemon_adversario,self))
                print("-------------------------------------------------------")
                print(bcolors.OK + "{} GANHOU".format(self) + bcolors.RESET)
                break


def pokemon_inicial():
    print("Ola jovem! Esta na hora de voce batalhar")
    time.sleep(1)
    print("Eu tenho uma maquina que ira sortear um pokemon para voce!")
    time.sleep(1)
    print("Tipos de pokemons...")
    print("[1] Fogo")
    print("[2] Agua")
    print("[3] Eletrico")
    time.sleep(1)
    escolha_do_tipo_pokemon = input("Qual tipo voce dejesa:")

    if (escolha_do_tipo_pokemon == "1"):
        meu_pokemon = Pokemons(tipo="fogo")
        time.sleep(1)
        print("Parabens! O seu primeiro pokemon é o: {}".format(meu_pokemon))
        return meu_pokemon
    elif (escolha_do_tipo_pokemon == "2"):
        meu_pokemon = Pokemons(tipo="agua")
        time.sleep(1)
        print("Parabens! O seu primeiro pokemon é o: {}".format(meu_pokemon))
        return meu_pokemon
    elif (escolha_do_tipo_pokemon == "3"):
        meu_pokemon = Pokemons(tipo="eletrico")
        time.sleep(1)
        print("Parabens! O seu primeiro pokemon é o: {}".format(meu_pokemon))
        return meu_pokemon
    else:
        print("Ocorreu um erro!")










