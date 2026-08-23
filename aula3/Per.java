class Personagem {

    private String nome;
    private int vida;
    private int nivel;

 
    public Personagem() {
        this.nome = "Thanos";
        this.vida = 100;
        this.nivel = 1;
    }


    public Personagem(String nome, int vida, int nivel) {
        setNome(nome);
        setVida(vida);
        setNivel(nivel);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        if (nome != null && !nome.trim().isEmpty()) {
            this.nome = nome;
        } else {
            System.out.println("Erro: o nome não pode ser vazio!");
        }
    }

 
    public int getVida() {
        return vida;
    }

    public void setVida(int vida) {
        if (vida >= 0 && vida <= 100) {
            this.vida = vida;
        } else {
            System.out.println("Erro: a vida deve estar entre 0 e 100!");
        }
    }


    public int getNivel() {
        return nivel;
    }

    public void setNivel(int nivel) {
        if (nivel >= 1) {
            this.nivel = nivel;
        } else {
            System.out.println("Erro: o nível deve ser no mínimo 1!");
        }
    }


    public void atacar() {
        System.out.println(nome + " realizou um ataque padrão de 10 de dano!");
    }


    public void atacar(int dano) {
        System.out.println(nome + " realizou um ataque de " + dano + " de dano!");
    }
}

public class Main {
    public static void main(String[] args) {


        Personagem personagem1 = new Personagem();

        Personagem personagem2 = new Personagem("Mulan", 80, 5);


        System.out.println("Nome: " + personagem1.getNome());
        System.out.println("Vida: " + personagem1.getVida());
        System.out.println("Nível: " + personagem1.getNivel());


        System.out.println("Nome: " + personagem2.getNome());
        System.out.println("Vida: " + personagem2.getVida());
        System.out.println("Nível: " + personagem2.getNivel());

        personagem1.atacar();

        personagem2.atacar(50);
    }
}
 
