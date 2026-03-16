package JavaUnicamp.JavaRPG;

public class Personagem {
    // Atributos (Estado)
    String nome; // String é objeto
    boolean vivo;
    int vida;
    int ataque;
    static int contadorPersonagens = 0; // conta qnts personagens existem
    // Atributo static pertence à Classe, não ao Objeto

    // Construtor
    Personagem(String nome) {
        this.nome = nome; // "this" diferencia o atributo do parâmetro
        this.vivo = true;
        this.vida = 100;
        this.ataque = 10;
        contadorPersonagens++; // Incrementa toda vez que um "new" é chamado
    }

    // Método (Comportamento)
    void receberDano(int dano) {
        this.vida -= dano;
        if (this.vida < 0) {
            this.vida = 0;
            this.vivo = false;
        }
    }

    static void exibirContador() {
        System.out.printf("Total de personagens: %d%n", contadorPersonagens);
    }
}
