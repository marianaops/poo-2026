class Personagem:

    def __init__(self, nome, vida, nivel):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if nome is not None and nome.strip() != "":
            self._nome = nome
        else:
            print("Erro: o nome não pode ser vazio!")

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, vida):
        if 0 <= vida <= 100:
            self._vida = vida
        else:
            print("Erro: a vida deve estar entre 0 e 100!")

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        if nivel >= 1:
            self._nivel = nivel
        else:
            print("Erro: o nível deve ser no mínimo 1!")



personagem = Personagem("Mulan", 80, 5)


print("Nome:", personagem.nome)
print("Vida:", personagem.vida)
print("Nível:", personagem.nivel)


personagem.vida = 150
personagem.vida = -10
personagem.nome = ""
personagem.nivel = 0
