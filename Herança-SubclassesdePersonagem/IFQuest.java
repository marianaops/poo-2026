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
class Personagem {

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
        if (!nome.isEmpty()) {
            this.nome = nome;
        } else {
            System.out.println("Nome não pode ser vazio.");
        }
    }

    public int getVida() {
        return vida;
    }

    public void setVida(int vida) {
        if (vida >= 0 && vida <= 100) {
            this.vida = vida;
        } else {
            System.out.println("Vida deve estar entre 0 e 100.");
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

    String ficha() {

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
    String ficha() {

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
    public void receberDano(int dano) {

        int danoEfetivo = Math.max(0, dano - defesa);

        super.receberDano(danoEfetivo);
    }

    @Override
    String ficha() {

        return super.ficha() +
                "\nDefesa: " + defesa;
    }
}
public class Main {

    public static void main(String[] args) {

        Item espada = new Item("Espada de Aço", 3);

        Mago mago = new Mago("Elara", 100, 1);

        mago.pegar(espada);

        System.out.println("----- MAGO -----");
        System.out.println(mago.ficha());

        Guerreiro guerreiro = new Guerreiro("Bran", 100, 1);

        guerreiro.receberDano(8);

        System.out.println("\n----- GUERREIRO -----");
        System.out.println(guerreiro.ficha());

        System.out.println("\nVida restante: " + guerreiro.getVida());

        System.out.println("\n----- TESTANDO MANA -----");

        mago.setMana(-10);

        System.out.println("Mana atual do Mago: " + mago.getMana());
    }
}
