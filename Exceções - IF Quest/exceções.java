import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        try {

            Mago magoTeste = new Mago("Laine", 100, 2);

            System.out.println("Criação do Mago bem sucedida!");

            Mago magoInvalido = new Mago("Laine", -100, 2);

            System.out.println("Criação do Mago bem sucedida!");

        } catch (IllegalArgumentException e) {

            System.out.println("Erro ao criar personagem: " + e.getMessage());
        }

        Item espada = new Item("machado", 4);

        Mago mago = new Mago("Laine", 100, 2);

        mago.pegar(espada);

        System.out.println("\n----- MAGO -----");
        System.out.println(mago.ficha());
        System.out.println("Habilidade: " + mago.habilidade());

        Guerreiro guerreiro = new Guerreiro("Naju", 100, 2);

        try {

            guerreiro.golpeEspecial();

        } catch (ForcaInsuficienteException e) {

            System.out.println(e.getMessage());
            System.out.println("O Guerreiro não conseguiu realizar o golpe especial.");
        }

        guerreiro.receberDano(8);

        System.out.println("\n----- GUERREIRO -----");
        System.out.println(guerreiro.ficha());
        System.out.println("Habilidade: " + guerreiro.habilidade());

        System.out.println("\nVida restante: " + guerreiro.getVida());

        System.out.println("\n----- TESTANDO MANA -----");

        mago.setMana(20);

        System.out.println("Mana atual do Mago: " + mago.getMana());

        System.out.println("\n===== BATALHA FINAL =====");

        List<Personagem> herois = new ArrayList<>();

        herois.add(mago);
        herois.add(guerreiro);

        Chefe chefe = new Chefe("João", 200, 1);

        for (Personagem heroi : herois) {

            System.out.println("\n----- HERÓI -----");
            System.out.println(heroi.ficha());

            try {

                if (heroi instanceof Mago) {

                    Mago m = (Mago) heroi;

                    System.out.println("Habilidade: " + m.getNome() + " usa " + m.habilidade());

                    m.lancarFeitico();

                    chefe.receberDano(20);

                    System.out.println("O Mago atacou o Chefe causando 20 de dano.");

                } else if (heroi instanceof Guerreiro) {

                    Guerreiro g = (Guerreiro) heroi;

                    System.out.println("Habilidade: " + g.getNome() + " usa " + g.habilidade());

                    g.golpeEspecial();
                    chefe.receberDano(20);

                    System.out.println("O Guerreiro atacou o Chefe causando 20 de dano.");
                }

            } catch (Mago.SemManaException e) {

                System.out.println("\n" + e.getMessage());
                System.out.println("O Mago perdeu o turno.");

                chefe.receberDano(20);

                System.out.println("O Guerreiro atacou no lugar do Mago causando 20 de dano!");

            }catch (ForcaInsuficienteException e) {

                System.out.println("\n" + e.getMessage());

                System.out.println("O Guerreiro não conseguiu realizar o golpe especial.");
            }
            finally{
                System.out.println("Fim de turno");
            
            }
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

    public Personagem(
            String nomePersonagem,
            int vidaPersonagem,
            int nivelPersonagem) {

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
            throw new IllegalArgumentException(
                    "Nome não pode ser vazio."
            );
        }
    }

    public int getVida() {
        return vida;
    }

    public void setVida(int vida) {

        if (vida >= 0 && vida <= 200) {
            this.vida = vida;
        } else {
            throw new IllegalArgumentException(
                    "Vida inválida: " + vida
            );
        }
    }

    public int getNivel() {
        return nivel;
    }

    public void setNivel(int nivel) {

        if (nivel >= 1) {
            this.nivel = nivel;
        } else {
            throw new IllegalArgumentException(
                    "Nível deve ser maior ou igual a 1."
            );
        }
    }

    public void pegar(Item item) {

        if (quantidadeItens < inventario.length) {

            inventario[quantidadeItens] = item;
            quantidadeItens++;

        } else {

            System.out.println("Inventário cheio.");
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
                "\nNível: " + nivel +
                "\nInventário:";

        if (quantidadeItens == 0) {

            resultado += "\nNenhum item";

        } else {

            for (int i = 0; i < quantidadeItens; i++) {

                resultado +=
                        "\n- " + inventario[i].descricao();
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

            throw new IllegalArgumentException(
                    "Bônus não pode ser negativo."
            );
        }
    }

    public String descricao() {

        return nome + " (+" + bonus + ")";
    }
}

class Mago extends Personagem {

    private int mana;

    public Mago(
            String nomePersonagem,
            int vidaPersonagem,
            int nivelPersonagem) {

        super(nomePersonagem, vidaPersonagem, nivelPersonagem);

        mana = 50;
    }

    public int getMana() {
        return mana;
    }

    public void setMana(int mana) {

        if (mana < 0) {

            throw new IllegalArgumentException(
                    "Mana inválida: " + mana
            );
        }

        this.mana = mana;
    }

    class SemManaException extends Exception {

        public SemManaException(int mana) {

            super("Mana insuficiente: " + mana);
        }
    }

    public void lancarFeitico() throws SemManaException {

        if (mana < 10) {

            throw new SemManaException(mana);
        }

        mana -= 10;

        System.out.println(
                "O Mago lançou um feitiço!"
        );
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

class ForcaInsuficienteException extends Exception {

    public ForcaInsuficienteException(int forca) {

        super("Força insuficiente: " + forca);
    }
}

class Guerreiro extends Personagem {

    private int defesa;
    private int forca;

    public Guerreiro(
            String nomePersonagem,
            int vidaPersonagem,
            int nivelPersonagem) {

        super(nomePersonagem, vidaPersonagem, nivelPersonagem);

        defesa = 5;
        forca = 5;
    }

    public int getDefesa() {
        return defesa;
    }

    public void setDefesa(int defesa) {

        if (defesa < 0) {

            throw new IllegalArgumentException(
                    "Defesa inválida: " + defesa
            );
        }

        this.defesa = defesa;
    }

    public int getForca() {
        return forca;
    }

    public void setForca(int forca) {

        if (forca < 0) {

            throw new IllegalArgumentException(
                    "Força inválida: " + forca
            );
        }

        this.forca = forca;
    }

    public void golpeEspecial()
            throws ForcaInsuficienteException {

        if (forca < 10) {

            throw new ForcaInsuficienteException(forca);
        }

        System.out.println(
                "O Guerreiro realizou um golpe especial!"
        );
    }

    @Override
    public String habilidade() {

        return "golpe mortal";
    }

    @Override
    public void receberDano(int dano) {

        int danoEfetivo =
                Math.max(0, dano - defesa);

        super.receberDano(danoEfetivo);
    }

    @Override
    public String ficha() {

        return super.ficha() +
                "\nDefesa: " + defesa +
                "\nForça: " + forca;
    }
}

class Chefe extends Personagem {

    private int forca;

    public Chefe(
            String nomePersonagem,
            int vidaPersonagem,
            int nivelPersonagem) {

        super(nomePersonagem, vidaPersonagem, nivelPersonagem);

        forca = 20;
    }

    public int getForca() {
        return forca;
    }

    public void setForca(int forca) {

        if (forca < 0) {

            throw new IllegalArgumentException(
                    "Força inválida: " + forca
            );
        }

        this.forca = forca;
    }

    @Override
    public String habilidade() {

        return "telecinese - força fênix";
    }

    @Override
    public String ficha() {

        return "[CHEFE] " + getNome() + " (vida: " + getVida() + ", força: " + forca + ")";
    }
}
