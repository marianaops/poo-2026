/*
 * Domínio: Empresa
 *
 * Superclasse abstrata: Funcionario
 *
 * Subclasses: Empregado e Gerente
 *
 * Funcionario possui os atributos:
 * - nome
 * - tempo
 *
 * Empregado possui como atributo próprio:
 * - codfun (código/matrícula do funcionário)
 *
 * Gerente possui como atributo próprio:
 * - setor
 *
 * Método abstrato: cumprirUmaDemanda()
 *
 * Método sobrescrito: mostrar()
 *
 * Utilizei IA para ajudar na estrutura e compreensão do código.
 */

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

/*
 * CRITÉRIOS
 *
 * Atingi os critérios de classe abstrata, herança, método abstrato,
 * sobrescrita e polimorfismo. Não ficou nenhum critério principal sem atender.
 *
 * A parte mais difícil foi adaptar Pessoa, Aluno e Professor para
 * Funcionario, Empregado e Gerente. Resolvi reorganizando as classes
 * e corrigindo os erros do código.
 *
 * A IA ajudou na organização, correção e compreensão do código.
 * Atrapalhou um pouco quando sugeriu mudanças que não estavam totalmente
 * de acordo com o que foi pedido, sendo necessário revisar e adaptar.
 link: https://chatgpt.com/share/6a997429-ded4-83e9-a905-38476e8463e7
 */
