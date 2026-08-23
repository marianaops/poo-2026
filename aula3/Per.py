class Personagem:

    def __init__(self, nome="Thanos", vida = 100, nivel = 1):
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

    def atacar(self, dano=10):
        print(f"{self.nome} realizou um ataque de {dano} de dano!")

personagem1 = Personagem()
personagem2 = Personagem("Mulan", 80, 5)

print("Nome:", personagem1.nome)
print("Vida:", personagem1.vida)
print("Nível:", personagem1.nivel)

print("Nome:", personagem2.nome)
print("Vida:", personagem2.vida)
print("Nível:", personagem2.nivel)

personagem1.atacar()
personagem2.atacar(50)

