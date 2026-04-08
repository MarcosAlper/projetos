#include <stdio.h>

int main() {
    int N, C; // N: leituras, C: capacidade
    int S, E; // S: saíram, E: entraram
    int atual = 0; // Passageiros no momento
    int excedeu = 0; // 0 para Não, 1 para Sim

    // 1. Ler N e C
    if (scanf("%d %d", &N, &C) != 2) return 0;

    // 2. Processar cada uma das N leituras
    for (int i = 0; i < N; i++) {
        scanf("%d %d", &S, &E);

        // Atualiza a quantidade de pessoas: saem primeiro, depois entram
        atual = atual - S + E;

        // Verifica se em algum momento a capacidade foi ultrapassada
        if (atual > C) {
            excedeu = 1;
        }
    }

    // 3. Saída final
    if (excedeu) {
        printf("S\n");
    } else {
        printf("N\n");
    }

    return 0;
}