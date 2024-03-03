meme_dict = {

            "CRINGE": "Algo excepcionalmente raro o embarazoso", "LOL": "Una respuesta común a algo gracioso",
            "AFK": "fuera del teclado",
            "BOOMER": "Muy viejo y no quiere entender a lo jovenes",
            "BASADO": "tiene a su disposicion toda la verdad", "CREEPY": "Tenebroso o de miedo",
            "GG":" buena partida",
            "NT":"Buen intento", 
            "EZ":"Facil"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])

else:
    print("no se encuentra el significado de la palabra")
