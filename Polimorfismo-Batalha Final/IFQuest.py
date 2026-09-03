# Uso de IA:
# Ferramenta utilizada: ChatGPT.
# Finalidade: 
# 
# Esclarecer dúvidas sobre classes, herança e classes abstratas.
# Modificações/validações manuais: revisei o código e conferi seu funcionamento.
# Tive um pouco de dificuldade com Python, pois tenho mais facilidade e prefiro trabalhar com Java.

from abc import ABC, abstractmethod

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
        return f"{self.__nome} (+{self.__bonus})"


class Personagem(ABC):

    def __init__(self, nome_personagem, vida_personagem, nivel_personagem):
        self.set_nome(nome_personagem)
        self.set_vida(vida_personagem)
        self.set_nivel(nivel_personagem)

        self.__inventario = [None] * 10
        self.__quantidade_itens = 0

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome is not None and nome != "":
            self.__nome = nome
        else:
            print("Nome não pode ser vazio.")

    def get_vida(self):
        return self.__vida

    def set_vida(self, vida):
        if 0 <= vida <= 200:
            self.__vida = vida
        else:
            print("Vida deve estar entre 0 e 200.")

    def get_nivel(self):
        return self.__nivel

    def set_nivel(self, nivel):
        if nivel >= 1:
            self.__nivel = nivel
        else:
            print("Nivel deve ser maior ou igual a 1.")

    def pegar(self, item):
        if self.__quantidade_itens < len(self.__inventario):
            self.__inventario[self.__quantidade_itens] = item
            self.__quantidade_itens += 1
        else:
            print("Inventario cheio.")

    def receber_dano(self, dano):
        self.set_vida(max(0, self.__vida - dano))

    @abstractmethod
    def habilidade(self):
        pass

    def ficha(self):
        resultado = (
            f"Nome: {self.__nome}"
            f"\nVida: {self.__vida}"
            f"\nNivel: {self.__nivel}"
            f"\nInventario:"
        )

        if self.__quantidade_itens == 0:
            resultado += "\nNenhum item"
        else:
            for i in range(self.__quantidade_itens):
                resultado += f"\n- {self.__inventario[i].descricao()}"

        return resultado


class Mago(Personagem):

    def __init__(self, nome_personagem, vida_personagem, nivel_personagem):
        super().__init__(
            nome_personagem,
            vida_personagem,
            nivel_personagem
        )

        self.__mana = 50

    def get_mana(self):
        return self.__mana

    def set_mana(self, mana):
        if mana >= 0:
            self.__mana = mana
        else:
            print("Mana não pode ser negativa.")

    def habilidade(self):
        return "transmutação"

    def ficha(self):
        return super().ficha() + f"\nMana: {self.__mana}"


class Guerreiro(Personagem):

    def __init__(self, nome_personagem, vida_personagem, nivel_personagem):
        super().__init__(
            nome_personagem,
            vida_personagem,
            nivel_personagem
        )

        self.__defesa = 5

    def get_defesa(self):
        return self.__defesa

    def set_defesa(self, defesa):
        if defesa >= 0:
            self.__defesa = defesa
        else:
            print("Defesa não pode ser negativa.")

    def habilidade(self):
        return "golpe mortal"

    def receber_dano(self, dano):
        dano_efetivo = max(0, dano - self.__defesa)
        super().receber_dano(dano_efetivo)

    def ficha(self):
        return super().ficha() + f"\nDefesa: {self.__defesa}"


class Chefe(Personagem):

    def __init__(self, nome_personagem, vida_personagem, nivel_personagem):
        super().__init__(nome_personagem, 200, 1)

        self.__forca = 20

    def get_forca(self):
        return self.__forca

    def set_forca(self, forca):
        if forca >= 0:
            self.__forca = forca
        else:
            print("Força não pode ser negativa.")

    def habilidade(self):
        return "telecinese - força fenix"

    def ficha(self):
        return (
            f"[CHEFE] {self.get_nome()}"
            f" (vida: {self.get_vida()}"
            f", forca: {self.__forca})"
        )


if __name__ == "__main__":

    espada = Item("machado", 4)

    mago = Mago("Laine", 100, 2)

    mago.pegar(espada)

    print("----- MAGO -----")
    print(mago.ficha())
    print("Habilidade:", mago.habilidade())

    guerreiro = Guerreiro("ken", 100, 2)

    guerreiro.receber_dano(8)

    print("\n----- GUERREIRO -----")
    print(guerreiro.ficha())
    print("Habilidade:", guerreiro.habilidade())

    print("\nVida restante:", guerreiro.get_vida())

    print("\n----- TESTANDO MANA -----")

    mago.set_mana(-20)

    print("Mana atual do Mago:", mago.get_mana())

    print("\n===== BATALHA FINAL =====")

    herois = []

    herois.append(mago)
    herois.append(guerreiro)

    chefe = Chefe("João", 200, 1)

    for heroi in herois:

        print("\n----- HERÓI -----")
        print(heroi.ficha())

        print(
            "Habilidade:",
            heroi.get_nome(),
            "usa",
            heroi.habilidade()
        )

        dano = 20

        chefe.receber_dano(dano)

        print(
            heroi.get_nome(),
            "atacou o Chefe causando",
            dano,
            "de dano."
        )

    print("\n===== CHEFE APÓS OS ATAQUES =====")
    print(chefe.ficha())
