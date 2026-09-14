"""
Registro de uso de ferramenta de IA (Claude)

Ferramenta utilizada: Claude
Para quê: ajudar na estrutura do código e em alguns conceitos de
orientação a objetos (herança, exceções personalizadas, blocos
try/except/finally), além de auxiliar a identificar e corrigir erros.
O que foi modificado/validado manualmente: o código foi revisado,
testado e ajustado manualmente antes da entrega.
"""

from abc import ABC, abstractmethod


class Personagem(ABC):

    def __init__(self, nome, vida, nivel):
        self.set_nome(nome)
        self.set_vida(vida)
        self.set_nivel(nivel)
        self.inventario = []

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        if nome is not None and nome != "":
            self._nome = nome
        else:
            raise ValueError("Nome inválido: não pode ser vazio.")

    def get_vida(self):
        return self._vida

    def set_vida(self, vida):
        if 0 <= vida <= 200:
            self._vida = vida
        else:
            raise ValueError(
                f"Vida inválida: {vida} (esperado um valor entre 0 e 200)"
            )

    def get_nivel(self):
        return self._nivel

    def set_nivel(self, nivel):
        if nivel >= 1:
            self._nivel = nivel
        else:
            raise ValueError(
                f"Nível inválido: {nivel} (esperado um valor maior ou igual a 1)"
            )

    def pegar(self, item):
        if len(self.inventario) < 10:
            self.inventario.append(item)
        else:
            print("Inventário cheio.")

    def receber_dano(self, dano):
        self.set_vida(max(0, self._vida - dano))

    @abstractmethod
    def habilidade(self):
        pass

    def ficha(self):
        resultado = (
            f"Nome: {self._nome}\n"
            f"Vida: {self._vida}\n"
            f"Nível: {self._nivel}\n"
            "Inventário:"
        )

        if not self.inventario:
            resultado += "\nNenhum item"
        else:
            for item in self.inventario:
                resultado += f"\n- {item.descricao()}"

        return resultado


class Item:

    def __init__(self, nome, bonus):
        self.nome = nome
        self.set_bonus(bonus)

    def get_bonus(self):
        return self._bonus

    def set_bonus(self, bonus):
        if bonus >= 0:
            self._bonus = bonus
        else:
            raise ValueError(
                f"Bônus inválido: {bonus} (esperado um valor maior ou igual a 0)"
            )

    def descricao(self):
        return f"{self.nome} (+{self._bonus})"


class SemManaError(Exception):
    def __init__(self, mana):
        super().__init__(
            f"Mana insuficiente: {mana} (esperado pelo menos 10)"
        )


class ForcaInsuficienteError(Exception):
    def __init__(self, forca):
        super().__init__(
            f"Força insuficiente: {forca} (esperado pelo menos 10)"
        )


class Mago(Personagem):

    def __init__(self, nome, vida, nivel):
        super().__init__(nome, vida, nivel)
        self._mana = 50

    def get_mana(self):
        return self._mana

    def set_mana(self, mana):
        if mana < 0:
            raise ValueError(
                f"Mana inválida: {mana} (esperado um valor maior ou igual a 0)"
            )
        self._mana = mana

    def lancar_feitico(self):
        if self._mana < 10:
            raise SemManaError(self._mana)

        self._mana -= 10
        print("O Mago lançou um feitiço!")

    def habilidade(self):
        return "transmutação"

    def ficha(self):
        return super().ficha() + f"\nMana: {self._mana}"


class Guerreiro(Personagem):

    def __init__(self, nome, vida, nivel):
        super().__init__(nome, vida, nivel)
        self._defesa = 5
        self._forca = 5

    def get_defesa(self):
        return self._defesa

    def set_defesa(self, defesa):
        if defesa < 0:
            raise ValueError(
                f"Defesa inválida: {defesa} (esperado um valor maior ou igual a 0)"
            )
        self._defesa = defesa

    def get_forca(self):
        return self._forca

    def set_forca(self, forca):
        if forca < 0:
            raise ValueError(
                f"Força inválida: {forca} (esperado um valor maior ou igual a 0)"
            )
        self._forca = forca

    def golpe_especial(self):
        if self._forca < 10:
            raise ForcaInsuficienteError(self._forca)

        print("O Guerreiro realizou um golpe especial!")

    def habilidade(self):
        return "golpe mortal"

    def receber_dano(self, dano):
        dano_efetivo = max(0, dano - self._defesa)
        super().receber_dano(dano_efetivo)

    def ficha(self):
        return super().ficha() + f"\nDefesa: {self._defesa}\nForça: {self._forca}"


class Chefe(Personagem):

    def __init__(self, nome, vida, nivel):
        super().__init__(nome, vida, nivel)
        self._forca = 20

    def get_forca(self):
        return self._forca

    def set_forca(self, forca):
        if forca < 0:
            raise ValueError(
                f"Força inválida: {forca} (esperado um valor maior ou igual a 0)"
            )
        self._forca = forca

    def habilidade(self):
        return "telecinese - força fênix"

    def ficha(self):
        return f"[CHEFE] {self.get_nome()} (vida: {self.get_vida()}, força: {self._forca})"


def escolher_heroi(herois):
    while True:
        print("\nEscolha o herói que deseja controlar:")
        for indice, heroi in enumerate(herois):
            print(f"{indice} - {heroi.get_nome()}")

        entrada = input("Número do herói: ")

        try:
            indice_escolhido = int(entrada)

            if indice_escolhido < 0:
                raise IndexError(indice_escolhido)

            return herois[indice_escolhido]

        except ValueError:
            print("Digite um número!")

        except IndexError:
            print(f"Não existe herói com o número {entrada}.")


def main():

    try:
        mago_teste = Mago("Laine", 100, 2)
        print("Criação do Mago bem sucedida!")

        mago_invalido = Mago("Laine", -100, 2)
        print("Criação do Mago bem sucedida!")

    except ValueError as erro:
        print(f"Erro ao criar personagem: {erro}")

    finally:
        print("Fim de turno")

    espada = Item("machado", 4)
    mago = Mago("Laine", 100, 2)
    mago.pegar(espada)

    print("\n----- MAGO -----")
    print(mago.ficha())
    print(f"Habilidade: {mago.habilidade()}")

    guerreiro = Guerreiro("Naju", 100, 2)

    try:
        guerreiro.golpe_especial()

    except ForcaInsuficienteError as erro:
        print(erro)
        print("O Guerreiro não conseguiu realizar o golpe especial.")

    finally:
        print("Fim de turno")

    guerreiro.receber_dano(8)

    print("\n----- GUERREIRO -----")
    print(guerreiro.ficha())
    print(f"Habilidade: {guerreiro.habilidade()}")

    print(f"\nVida restante: {guerreiro.get_vida()}")

    print("\n----- TESTANDO MANA -----")
    mago.set_mana(20)
    print(f"Mana atual do Mago: {mago.get_mana()}")

    print("\n===== BATALHA FINAL =====")

    herois = [mago, guerreiro]
    chefe = Chefe("João", 200, 1)

    for heroi in herois:

        print("\n----- HERÓI -----")
        print(heroi.ficha())

        try:
            if isinstance(heroi, Mago):
                print(f"Habilidade: {heroi.get_nome()} usa {heroi.habilidade()}")

                heroi.lancar_feitico()

                chefe.receber_dano(20)
                print("O Mago atacou o Chefe causando 20 de dano.")

            elif isinstance(heroi, Guerreiro):
                print(f"Habilidade: {heroi.get_nome()} usa {heroi.habilidade()}")

                heroi.golpe_especial()
                chefe.receber_dano(20)
                print("O Guerreiro atacou o Chefe causando 20 de dano.")

        except SemManaError as erro:
            print(f"\n{erro}")
            print("O Mago perdeu o turno.")

            chefe.receber_dano(20)
            print("O Guerreiro atacou no lugar do Mago causando 20 de dano!")

        except ForcaInsuficienteError as erro:
            print(f"\n{erro}")
            print("O Guerreiro não conseguiu realizar o golpe especial.")

        finally:
            print("Fim de turno")

    print("\n===== CHEFE APÓS OS ATAQUES =====")
    print(chefe.ficha())

    heroi_escolhido = escolher_heroi(herois)
    print(f"\nVocê escolheu controlar: {heroi_escolhido.get_nome()}")


if __name__ == "__main__":
    main()
