/*
 * REGISTRO DO USO DE FERRAMENTAS DE IA
 *
 * - Ferramenta utilizada:
 *   ChatGPT.
 *
 * - Para quê foi utilizada:
 *   Auxiliar na revisão e compreensão do código Java,
 *   especialmente conceitos de herança, encapsulamento,
 *   polimorfismo e classes abstratas.
 *
 * - O que foi modificado ou validado manualmente:
 *   - Verifiquei a estrutura das classes Personagem, Mago,
 *     Guerreiro e Item.
 *   - Validei manualmente o uso de getters e setters.
 *   - Validei a sobrescrita dos métodos habilidade(),
 *   - Criei do 0 a class chefe.
 *   - Modifiquei o Main acrescentando a parte do chefe e herói nele.
 */

import java.util.ArrayList;
import java.util.List;

public class Main {


    public static void main(String[] args) {

        Item espada = new Item("machado", 4);

        Mago mago = new Mago("Laine", 100, 2);

        mago.pegar(espada);

        System.out.println("----- MAGO -----");
        System.out.println(mago.ficha());
        System.out.println("Habilidade: " + mago.habilidade());

        Guerreiro guerreiro = new Guerreiro("ken", 100, 2);

        guerreiro.receberDano(8);

        System.out.println("\n----- GUERREIRO -----");
        System.out.println(guerreiro.ficha());
        System.out.println("Habilidade: " + guerreiro.habilidade());

        System.out.println("\nVida restante: " + guerreiro.getVida());

        System.out.println("\n----- TESTANDO MANA -----");

        mago.setMana(-20);

        System.out.println("Mana atual do Mago: " + mago.getMana());

        System.out.println("\n===== BATALHA FINAL =====");

        List<Personagem> herois = new ArrayList<>();

        herois.add(mago);
        herois.add(guerreiro);

        Chefe chefe = new Chefe("João",200,1);

        for (Personagem heroi : herois) {

            System.out.println("\n----- HERÓI -----");
            System.out.println(heroi.ficha());

            System.out.println("Habilidade: " + heroi.getNome() + " usa " + heroi.habilidade());

            int dano = 20;

            chefe.receberDano(dano);

            System.out.println(heroi.getNome() + " atacou o Chefe causando " + dano + " de dano.");
        }

        System.out.println("\n===== CHEFE APÓS OS ATAQUES =====");
        System.out.println(chefe.ficha());
    }
}



abstract class Personagem {

    private String nome;
    private int vida;
    private int nivel;

    private Item[] inventario;
    private int quantidadeItens;

    public Personagem(String nomePersonagem, int vidaPersonagem, int nivelPersonagem) {

        setNome(nomePersonagem);
        setVida(vidaPersonagem);
        setNivel(nivelPersonagem);

        inventario = new Item[10];
        quantidadeItens = 0;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        if (nome != null && !nome.isEmpty()) {
            this.nome = nome;
        } else {
            System.out.println("Nome não pode ser vazio.");
        }
    }

    public int getVida() {
        return vida;
    }

    public void setVida(int vida) {
        if (vida >= 0 && vida <= 200) {
            this.vida = vida;
        } else {
            System.out.println("Vida deve estar entre 0 e 200.");
        }
    }

    public int getNivel() {
        return nivel;
    }

    public void setNivel(int nivel) {
        if (nivel >= 1) {
            this.nivel = nivel;
        } else {
            System.out.println("Nivel deve ser maior ou igual a 1.");
        }
    }

    public void pegar(Item item) {
        if (quantidadeItens < inventario.length) {
            inventario[quantidadeItens] = item;
            quantidadeItens++;
        } else {
            System.out.println("Inventario cheio.");
        }
    }

    public void receberDano(int dano) {
        setVida(Math.max(0, vida - dano));
    }

    public abstract String habilidade();

    public String ficha() {

        String resultado =
                "Nome: " + nome +
                "\nVida: " + vida +
                "\nNivel: " + nivel +
                "\nInventario:";

        if (quantidadeItens == 0) {
            resultado += "\nNenhum item";
        } else {
            for (int i = 0; i < quantidadeItens; i++) {
                resultado += "\n- " + inventario[i].descricao();
            }
        }

        return resultado;
    }
}


class Item {

    private String nome;
    private int bonus;

    public Item(String nome, int bonus) {
        this.nome = nome;
        setBonus(bonus);
    }

    public String getNome() {
        return nome;
    }

    public int getBonus() {
        return bonus;
    }

    public void setBonus(int bonus) {
        if (bonus >= 0) {
            this.bonus = bonus;
        } else {
            System.out.println("Bonus não pode ser negativo.");
        }
    }

    public String descricao() {
        return nome + " (+" + bonus + ")";
    }
}


class Mago extends Personagem {

    private int mana;

    public Mago(String nomePersonagem, int vidaPersonagem, int nivelPersonagem) {

        super(nomePersonagem, vidaPersonagem, nivelPersonagem);

        mana = 50;
    }

    public int getMana() {
        return mana;
    }

    public void setMana(int mana) {
        if (mana >= 0) {
            this.mana = mana;
        } else {
            System.out.println("Mana não pode ser negativa.");
        }
    }

    @Override
    public String habilidade() {
        return "transmutação";
    }

    @Override
    public String ficha() {
        return super.ficha() +
                "\nMana: " + mana;
    }
}


class Guerreiro extends Personagem {

    private int defesa;

    public Guerreiro(String nomePersonagem, int vidaPersonagem, int nivelPersonagem) {

        super(nomePersonagem, vidaPersonagem, nivelPersonagem);

        defesa = 5;
    }

    public int getDefesa() {
        return defesa;
    }

    public void setDefesa(int defesa) {
        if (defesa >= 0) {
            this.defesa = defesa;
        } else {
            System.out.println("Defesa não pode ser negativa.");
        }
    }

    @Override
    public String habilidade() {
        return "golpe mortal";
    }

    @Override
    public void receberDano(int dano) {

        int danoEfetivo = Math.max(0, dano - defesa);

        super.receberDano(danoEfetivo);
    }

    @Override
    public String ficha() {
        return super.ficha() +
                "\nDefesa: " + defesa;
    }
}

class Chefe extends Personagem {

    private int forca;

    public Chefe(String nomePersonagem, int vidaPersonagem, int nivelPersonagem) {

        super(nomePersonagem, 200, 1);
        
        forca = 20;
    }

    public int getForca() {
        return forca;
    }

    public void setForca(int forca) {
        if (forca >= 0) {
            this.forca = forca;
        } else {
            System.out.println("Força não pode ser negativa.");
        }
    }

    @Override
    public String habilidade() {
        return "telecinese - força fenix";
    }

    @Override
    public String ficha() {
        return "[CHEFE] " + getNome() +
                " (vida: " + getVida() +
                ", forca: " + forca + ")";
    }
}
