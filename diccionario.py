meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "POV": "Adelantacion de algo, posibilidad de pasar algo"
            "SPOILER": "Adelantacion de algo que pasara algun momento"
            }
word = input("Escribe una palabra que no entiendas (con mayusculas): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Por favor di otra")
    print("No esta en nuestro diccionario")
