class Item:

    def __init__(self, nome, bonus):
        self.__nome = nome
        self.set_bonus(bonus)

    def get_nome(self):
        return self.__nome

    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, bonus):
        if bonus >= 0:
            self.__bonus = bonus
        else:
            print("Bonus não pode ser negativo.")

    def descricao(self):
        return self.__nome + " (+" + str(self.__bonus) + ")"

class Personagem:

    def __init__(self, nome, vida, nivel):
        self.set_nome(nome)
        self.set_vida(vida)
        self.set_nivel(nivel)

        self.__inventario = [None] * 10
        self.__quantidadeItens = 0

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            print("Nome não pode ser vazio.")

    def get_vida(self):
        return self.__vida

    def set_vida(self, vida):
        if 0 <= vida <= 100:
            self.__vida = vida
        else:
            print("Vida deve estar entre 0 e 100.")

    def get_nivel(self):
        return self.__nivel

    def set_nivel(self, nivel):
        if nivel >= 1:
            self.__nivel = nivel
        else:
            print("Nivel deve ser maior ou igual a 1.")

    def pegar(self, item):
        if self.__quantidadeItens < len(self.__inventario):
            self.__inventario[self.__quantidadeItens] = item
            self.__quantidadeItens += 1
        else:
            print("Inventario cheio.")

    def receber_dano(self, dano):
        self.set_vida(max(0, self.__vida - dano))

    def ficha(self):

        resultado = (
            "Nome: " + self.__nome +
            "\nVida: " + str(self.__vida) +
            "\nNivel: " + str(self.__nivel) +
            "\nInventario:"
        )

        if self.__quantidadeItens == 0:
            resultado += "\nNenhum item"
        else:
            for i in range(self.__quantidadeItens):
                resultado += "\n- " + self.__inventario[i].descricao()

        return resultado

class Mago(Personagem):

    def __init__(self, nome, vida, nivel):
        super().__init__(nome, vida, nivel)
        self.__mana = 50

    def get_mana(self):
        return self.__mana

    def set_mana(self, mana):
        if mana >= 0:
            self.__mana = mana
        else:
            print("Mana não pode ser negativa.")

    def ficha(self):
        return super().ficha() + "\nMana: " + str(self.__mana)

class Guerreiro(Personagem):

    def __init__(self, nome, vida, nivel):
        super().__init__(nome, vida, nivel)
        self.__defesa = 5

    def get_defesa(self):
        return self.__defesa

    def set_defesa(self, defesa):
        if defesa >= 0:
            self.__defesa = defesa
        else:
            print("Defesa não pode ser negativa.")

    def receber_dano(self, dano):
        dano_efetivo = max(0, dano - self.__defesa)
        super().receber_dano(dano_efetivo)

    def ficha(self):
        return super().ficha() + "\nDefesa: " + str(self.__defesa)

espada = Item("Espada de Aço", 3)

mago = Mago("Elara", 100, 1)

mago.pegar(espada)

print("----- MAGO -----")
print(mago.ficha())


guerreiro = Guerreiro("Bran", 100, 1)

guerreiro.receber_dano(8)

print("\n----- GUERREIRO -----")
print(guerreiro.ficha())

print("\nVida restante:", guerreiro.get_vida())


print("\n----- TESTANDO MANA -----")

mago.set_mana(-10)

print("Mana atual do Mago:", mago.get_mana())
