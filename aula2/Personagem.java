public class Personagem {
    
    String nome;
    int vida;
    int forca;
    
    public Personagem(String nome,int vida,int forca){
        this.nome = nome;
        this.vida = vida;
        this.forca = forca;
    }
    
    void receberDano(int dano) {
        vida = vida - dano;
        System.out.println(nome + " sofreu " + dano + " de dano");
    }

    boolean estaVivo(){
        if(vida > 0){
            return true;
        } else {
            return false;
        }
    
    }
    
    String ficha() {
    return nome + "vida: " + vida + "força: " + forca;
    }
    
    void atacar(Personagem alvo) {
    System.out.println(nome + " ataca " + alvo.nome);
    alvo.receberDano(forca);
    }
    
}

public class Main {
    public static void main(String[] args) {
        
        Personagem heroi = new Personagem("Mulan", 200, 40);
        Personagem chefe = new Personagem("Thanos", 200, 5);
        
        while (heroi.estaVivo() && chefe.estaVivo()) {
            heroi.atacar(chefe);
            System.out.println(heroi.nome + " atacou " + chefe.nome + ". Vida do chefe: " + chefe.vida);

            if (!chefe.estaVivo()) {
                System.out.println(chefe.nome + " foi derrotado! " + heroi.nome + " venceu!");
                break;
            }

            chefe.atacar(heroi);
            System.out.println(chefe.nome + " atacou " + heroi.nome + ". Vida do herói: " + heroi.vida);

            if (!heroi.estaVivo()) {
                System.out.println(heroi.nome + " foi derrotado! " + chefe.nome + " venceu!");
                break;
            }
        }
    }
}
