#include <iostream>
#include <string>

class Pessoa {
    private:
        // Atributos privados, apenas a própria pessoa pode mexer
        std::string nome;
        std::string trabalho;
        double saldo;
        double fome; // 100 a 0

    public:
        // Construtor para inicializar os atributos
        Pessoa(std::string p_nome, std::string p_trabalho, double p_saldo) {
            nome = p_nome;
            trabalho = p_trabalho;
            saldo = p_saldo;
            fome = 100; // Começa sem fome (100 - satisfeito, 0 - fome)
        }

        void fome() {
            fome -= 10.0;
            std::cout << nome << " está com " << fome << "% de fome." << std::endl;
        }

        void comer() {
            if (fome < 100) {
                fome += 20.0;
                if (fome > 0) fome = 100; // 100 é o valor máximo
                std::cout << nome << " comeu e agora tem " << fome << "% de fome." << std::endl;
            } else {
                std::cout << nome << " não está com fome!" << std::endl;
            }
        }

        void trabalhar() {
            if (fome > 10) {
                saldo += 2.0;
                std::cout << nome << " trabalhou como " << trabalho << " e ganhou R$2,00." << std::endl;
                } else {
                    std::cout << nome << " está fraco demais para trabalhar!" << std::endl;
                }
        }
};
