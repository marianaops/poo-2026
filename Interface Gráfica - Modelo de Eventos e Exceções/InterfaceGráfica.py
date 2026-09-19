# REGISTRO DO USO DE INTELIGENCIA ARTIFICIAL
#
# Ferramenta utilizada: ChatGPT (OpenAI)
#
# A ferramenta foi utilizada como apoio durante o desenvolvimento
# do projeto, principalmente para esclarecer alguns conceitos de
# programacao orientada a objetos e para auxiliar na implementacao
# do codigo em Python.
#
# Tambem foi utilizada para auxiliar na diferenca entre Java e Python,
# identificando quais partes do codigo Java precisavam ser adaptadas
# para a sintaxe e funcionamento do Python.
#
# A ferramenta tambem foi utilizada para identificar e corrigir erros
# no codigo, melhorar a organizacao das classes, metodos, excecoes
# e da interface grafica.
#
# As modificacoes e validacoes finais foram realizadas manualmente,
# verificando o funcionamento do programa, a criacao dos personagens,
# as classes Mago e Guerreiro, seus atributos e o tratamento de erros.
import tkinter as tk
from tkinter import messagebox


class SemManaException(Exception):
    def __init__(self, mana):
        super().__init__(f"Mana insuficiente: {mana}")


class ForcaInsuficienteException(Exception):
    def __init__(self, forca):
        super().__init__(f"Forca insuficiente: {forca}")


class Item:
    def __init__(self, nome, bonus):
        self.nome = nome
        self.set_bonus(bonus)

    def get_nome(self):
        return self.nome

    def get_bonus(self):
        return self.bonus

    def set_bonus(self, bonus):
        if bonus >= 0:
            self.bonus = bonus
        else:
            raise ValueError("Bonus nao pode ser negativo.")

    def descricao(self):
        return f"{self.nome} (+{self.bonus})"


class Personagem:
    def __init__(self, nome, vida, nivel):
        self.set_nome(nome)
        self.set_vida(vida)
        self.set_nivel(nivel)
        self.inventario = []
        self.quantidade_itens = 0

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        if not nome or not nome.strip():
            raise ValueError("Nome nao pode ser vazio.")
        self.nome = nome

    def get_vida(self):
        return self.vida

    def set_vida(self, vida):
        if vida < 0 or vida > 200:
            raise ValueError("Vida deve estar entre 0 e 200.")
        self.vida = vida

    def get_nivel(self):
        return self.nivel

    def set_nivel(self, nivel):
        if nivel < 1:
            raise ValueError("Nivel deve ser maior ou igual a 1.")
        self.nivel = nivel

    def pegar(self, item):
        if self.quantidade_itens < 10:
            self.inventario.append(item)
            self.quantidade_itens += 1
        else:
            raise ValueError("Inventario cheio.")

    def receber_dano(self, dano):
        self.set_vida(max(0, self.vida - dano))

    def habilidade(self):
        raise NotImplementedError

    def ficha(self):
        texto = f"Nome: {self.nome}\n"
        texto += f"Vida: {self.vida}\n"
        texto += f"Nivel: {self.nivel}\n"
        texto += "Inventario:\n"

        for item in self.inventario:
            texto += f"- {item.descricao()}\n"

        return texto


class Mago(Personagem):
    def __init__(self, nome, vida, nivel):
        super().__init__(nome, vida, nivel)
        self.mana = 50

    def get_mana(self):
        return self.mana

    def set_mana(self, mana):
        if mana < 0:
            raise ValueError("Mana nao pode ser negativa.")
        self.mana = mana

    def lancar_feitico(self):
        if self.mana < 10:
            raise SemManaException(self.mana)

        self.mana -= 10
        print("O mago lancou um feitico.")

    def habilidade(self):
        return "Transmutacao"

    def ficha(self):
        return super().ficha() + f"Mana: {self.mana}\n"


class Guerreiro(Personagem):
    def __init__(self, nome, vida, nivel):
        super().__init__(nome, vida, nivel)
        self.defesa = 5
        self.forca = 5

    def get_defesa(self):
        return self.defesa

    def set_defesa(self, defesa):
        if defesa < 0:
            raise ValueError("Defesa nao pode ser negativa.")
        self.defesa = defesa

    def get_forca(self):
        return self.forca

    def set_forca(self, forca):
        if forca < 0:
            raise ValueError("Forca nao pode ser negativa.")
        self.forca = forca

    def golpe_especial(self):
        if self.forca < 10:
            raise ForcaInsuficienteException(self.forca)

        self.forca -= 10
        print("O guerreiro realizou um golpe especial.")

    def habilidade(self):
        return "Golpe mortal"

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        super().receber_dano(dano_final)

    def ficha(self):
        return (
            super().ficha()
            + f"Defesa: {self.defesa}\n"
            + f"Forca: {self.forca}\n"
        )


class Chefe(Personagem):
    def __init__(self, nome, vida, nivel):
        super().__init__(nome, vida, nivel)
        self.forca = 20

    def habilidade(self):
        return "Telecinese - forca fenix"

    def ficha(self):
        return super().ficha() + f"Forca: {self.forca}\n"


class TelaCriacaoHeroi:
    def __init__(self, janela):
        self.janela = janela

        self.janela.title("IF Quest")
        self.janela.geometry("450x350")

        tk.Label(janela, text="Nome:").pack()
        self.campo_nome = tk.Entry(janela)
        self.campo_nome.pack()

        tk.Label(janela, text="Vida:").pack()
        self.campo_vida = tk.Entry(janela)
        self.campo_vida.pack()

        tk.Label(janela, text="Classe:").pack()
        self.campo_classe = tk.Entry(janela)
        self.campo_classe.pack()

        tk.Button(
            janela,
            text="Criar Heroi",
            command=self.criar_heroi
        ).pack(pady=20)

        self.rotulo_status = tk.Label(janela, text="")
        self.rotulo_status.pack()

    def criar_heroi(self):
        try:
            nome = self.campo_nome.get()
            vida = int(self.campo_vida.get())
            classe = self.campo_classe.get().lower()

            if classe == "mago":
                mago = Mago(nome, vida, 1)

                self.rotulo_status.config(
                    text=f"Heroi {nome} criado com vida {vida}!"
                )

                print("\n===== CRIACAO DO HEROI =====")
                print("Classe: Mago")
                print("Nome:", mago.get_nome())
                print("Vida:", mago.get_vida())
                print("Mana:", mago.get_mana())

            elif classe == "guerreiro":
                guerreiro = Guerreiro(nome, vida, 1)

                self.rotulo_status.config(
                    text=f"Heroi {nome} criado com vida {vida}!"
                )

                print("\n===== CRIACAO DO HEROI =====")
                print("Classe: Guerreiro")
                print("Nome:", guerreiro.get_nome())
                print("Vida:", guerreiro.get_vida())
                print("Defesa:", guerreiro.get_defesa())
                print("Forca:", guerreiro.get_forca())

            else:
                messagebox.showerror(
                    "Erro",
                    "A classe deve ser Mago ou Guerreiro!"
                )

        except ValueError as e:
            messagebox.showerror("Erro", str(e))


def main():
    try:
        teste = Mago("Teste", -100, 2)
    except ValueError as e:
        print("Erro ao criar personagem:", e)
    finally:
        print("Fim de turno")

    espada = Item("machado", 4)

    mago = Mago("Laine", 100, 2)
    guerreiro = Guerreiro("Naju", 100, 2)

    mago.pegar(espada)

    print("\n----- MAGO -----")
    print(mago.ficha())
    print("Habilidade:", mago.habilidade())

    print("\n----- GUERREIRO -----")
    print(guerreiro.ficha())
    print("Habilidade:", guerreiro.habilidade())

    personagens = [mago, guerreiro]

    chefe = Chefe("Joao", 150, 5)

    print("\n----- BATALHA -----")

    for personagem in personagens:
        try:
            if isinstance(personagem, Mago):
                personagem.lancar_feitico()
                chefe.receber_dano(20)
                print(personagem.get_nome(), "causou 20 de dano.")

            elif isinstance(personagem, Guerreiro):
                personagem.golpe_especial()
                chefe.receber_dano(20)
                print(personagem.get_nome(), "causou 20 de dano.")

        except SemManaException as e:
            print("Mago perdeu o turno:", e)

        except ForcaInsuficienteException as e:
            print("Guerreiro perdeu o turno:", e)

    print("\nVida do chefe:", chefe.get_vida())


if __name__ == "__main__":
    main()

    janela = tk.Tk()
    tela = TelaCriacaoHeroi(janela)
    janela.mainloop()
