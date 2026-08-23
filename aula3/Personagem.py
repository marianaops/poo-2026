class Personagem:

    def __init__(self, nome, vida, nivel):
        self.set_nome(nome)
        self.set_vida(vida)
        self.set_nivel(nivel)

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        if nome is not None and nome.strip() != "":
            self.nome = nome
        else:
            print("Erro: o nome não pode ser vazio!")

    def get_vida(self):
        return self.vida

    def set_vida(self, vida):
        if vida >= 0 and vida <= 100:
            self.vida = vida
        else:
            print("Erro: a vida deve estar entre 0 e 100!")

    def get_nivel(self):
        return self.nivel

    def set_nivel(self, nivel):
        if nivel >= 1:
            self.nivel = nivel
        else:
            print("Erro: o nível deve ser no mínimo 1!")



personagem = Personagem("Mulan", 80, 5)

print("Nome:", personagem.get_nome())
print("Vida:", personagem.get_vida())
print("Nível:", personagem.get_nivel())


personagem.set_vida(190)
personagem.set_vida(-80)
personagem.set_nome("")
personagem.set_nivel(0)
