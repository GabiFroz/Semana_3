class Album:
    def __init__(self, nome, ano, faixas):
        self.nome = nome
        self.ano = ano
        self.faixas = faixas  # Lista com as músicas do álbum

    def mostrar_informacoes(self):
        print(f"Álbum: {self.nome} ({self.ano})")
        print("Músicas:")
        for faixa in self.faixas:
            print(f"- {faixa}")
        print("\n")


album_harry_styles = Album('Harry Styles', 2017, [
    "Meet Me in the Hallway", 
    "Sign of the Times", 
    "Carolina", 
    "Two Ghosts", 
    "Sweet Creature", 
    "Only Angel", 
    "Kiwi", 
    "Ever Since New York", 
    "Woman", 
    "From the Dining Table"
])

album_fine_line = Album('Fine Line', 2019, [
    "Golden", 
    "Watermelon Sugar", 
    "Sugar Waterfall", 
    "Falling", 
    "Vineyard Vines", 
    "Cherry", 
    "To Be So Lonely", 
    "She", 
    "Sunflower, Vol. 6", 
    "Canyon Moon", 
    "Treat People With Kindness", 
    "Fine Line"
])

album_harrys_house = Album("Harry's House", 2022, [
    "Music For a Sushi Restaurant", 
    "Late Night Talking", 
    "Grapejuice", 
    "As It Was", 
    "Daylight", 
    "Little Freak", 
    "Matilda", 
    "Cinema", 
    "Keep Driving", 
    "Satellite", 
    "Boyfriends", 
    "Love of My Life"
])

album_harry_styles.mostrar_informacoes()
album_fine_line.mostrar_informacoes()
album_harrys_house.mostrar_informacoes()
