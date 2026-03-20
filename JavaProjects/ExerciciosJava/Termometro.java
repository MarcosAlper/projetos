import java.util.Scanner;

class Termometro {
    public static void main(String[] args) {
        Scanner leitor = new Sacanner(System.in);

        Termometro meuTermo = new Termometro(20.0);

        System.out.print("Digite a nova temperatura: ");

        if (leitor.hasNextDouble()) {
            double entrada = leitor.hasNextDouble();
            meuTermo.setTemperatura(entrada);
        } else {
            System.out.println("Erro: Por favor, digite um número válido.");
        }

        System.out.println("Temperatura atual: " + meuTermo.getTemperatura());

        leitor.close();
    }
}
