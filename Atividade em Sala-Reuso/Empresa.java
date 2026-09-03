abstract class Funcionario {
    protected String nome;
    protected int tempo;

    public Funcionario(String nome, int tempo) {
        this.nome = nome;
        this.tempo = tempo;
    }

    public abstract void cumprirUmaDemanda();

    public void mostrar() {
        System.out.println("Nome: " + nome);
        System.out.println("Tempo de empresa: " + tempo + " anos");
    }
}

class Empregado extends Funcionario {
    private int codfun;

    public Empregado(String nome, int tempo, int codfun) {
        super(nome, tempo);
        this.codfun = codfun;
    }

    @Override
    public void cumprirUmaDemanda() {
        System.out.println("O empregado está trabalhando.");
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("Código: " + codfun);
    }
}
class Gerente extends Funcionario {
    private String setor;

    public Gerente(String nome, int tempo, String setor) {
        super(nome, tempo);
        this.setor = setor;
    }

    @Override
    public void cumprirUmaDemanda() {
        System.out.println("O gerente está organizando as atividades da equipe.");
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("Setor: " + setor);
    }
}

public class Main {
    public static void main(String[] args) {

        Funcionario[] funcionarios = {
            new Empregado("Laine", 5, 202603),
            new Gerente("Naju", 10, "Programação")
        };

        for (Funcionario funcionario : funcionarios) {
            funcionario.cumprirUmaDemanda();
            funcionario.mostrar();
            System.out.println();
        }
    }
}

