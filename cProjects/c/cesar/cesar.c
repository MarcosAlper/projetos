#include <stdio.h>
#include <string.h>

// Protótipos das funções
void limparBuffer();
void lerString(char *string, int tamanho);
void obterMensagem(char *mensagem, int tamanhoMensagem, int *chave);
void codificarMensagem(char *mensagem, int chave);
void decodificarMensagem(char *mensagem, int chave);

int main() {
    int tamanho = 50;
    char mensagem[tamanho];
    int chave;

    obterMensagem(mensagem, tamanho, &chave);

    codificarMensagem(mensagem, chave);
    
    printf("Mensagem Codificada: %s\n", mensagem);

    decodificarMensagem(mensagem, chave);
    
    printf("Mensagem Decodificada: %s\n", mensagem);

    return 0;
}

void limparBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

void lerString(char *string, int tamanho) {
    if (fgets(string, tamanho, stdin)) {
        size_t len = strlen(string);
        if (len > 0 && string[len - 1] == '\n') {
            string[len - 1] = '\0';
        } else {
            limparBuffer();
        }
    }
}

void obterMensagem(char *mensagem, int tamanhoMensagem, int *chave) {
    printf("Mensagem: ");
    lerString(mensagem, tamanhoMensagem);
    
    printf("Chave (numero): ");
    scanf("%d", chave);
    limparBuffer();
}

void codificarMensagem(char *mensagem, int chave) {
    for (int c = 0; c < strlen(mensagem); c++) {
        if (mensagem[c] >= 'a' && mensagem[c] <= 'z') {
            mensagem[c] = mensagem[c] + chave;
            if (mensagem[c] > 'z') {
                mensagem[c] = mensagem[c] - 26;
            }
        } else if (mensagem[c] >= 'A' && mensagem[c] <= 'Z') {
            mensagem[c] = mensagem[c] + chave;
            if (mensagem[c] > 'Z') {
                mensagem[c] = mensagem[c] - 26;
            }
        }
    }
}

void decodificarMensagem(char *mensagem, int chave) {
    for (int c = 0; c < strlen(mensagem); c++) {
        if (mensagem[c] >= 'a' && mensagem[c] <= 'z') {
            mensagem[c] = mensagem[c] - chave;
            if (mensagem[c] < 'a') {
                mensagem[c] = mensagem[c] + 26;
            }
        } else if (mensagem[c] >= 'A' && mensagem[c] <= 'Z') {
            mensagem[c] = mensagem[c] - chave;
            if (mensagem[c] < 'A') {
                mensagem[c] = mensagem[c] + 26;
            }
        }
    }
}
