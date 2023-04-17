class gato:
    color_de_ojos = ""
    color_de_pelaje = ""

    def __init__(self) -> None:
        print(f"Meow, soy un gato con ojos {self.color_de_ojos} y pelaje {self.color_de_pelaje}")

Kiara = gato()
Kiara.color_de_ojos="verdes"
Kiara.color_de_pelaje="blanco, negro y cafe"
Kiara.__init__()

chanchito_feliz = 2
