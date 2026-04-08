/*
obj_ui_controller
	Responsabilidades:
		1. Gestão e Exibição de Status (HUD)
		2. Interface de Entrada de Toque (Mobile UI)
		3. Gestão de Telas de Estado Global
		4. Otimização de Performance da UI
		5.Controle de Fluxo de Mensagens
*/
// Configurações de exibição (Substituindo os "Números Mágicos")
gui_width = display_get_gui_width();
gui_height = display_get_gui_height();

// Margens e dimensões das barras
bar_width = 256;
bar_height = 32;
margin_x = 16;
margin_y = 16;

if (!variable_global_exists("show_final_screen"))
{
    global.show_final_screen = false;
}

btn_attack_size = 175;

btn_attack_x = 0;
btn_attack_y = 0;

// Variáveis para a Tela Final (Movidas do Draw do Player)
// Processamos isso aqui UMA VEZ, em vez de todo frame no Draw
final_message_list = [
    "Parabéns!",
        "Você chegou ao fim da versão Alpha do jogo!",
        "Este projeto é um Protótipo Alpha em desenvolvimento ativo. O feedback de vocês é extremamente importante para aprimorar os sistemas de combate e diálogo. Agradecemos a todos por jogar e contribuir com o projeto.",
        "Se você compartilha do nosso interesse em Desenvolvimento de Games, você pode me chamar a qualquer momento para conversarmos sobre.",
        "Contato:",
        "Whatsapp - (11) 9 1478-9089",
        "Email - marcosneto1902@outlook.com",
        "",
        "Créditos:",
        "Marcos Almeida Pereira Neto - 194897: Game Director, Game Designer e Programador",
        "Eike Henrique Souza Da Rocha - 281410: Game Artist e Game Designer",
        "Helio Pereira Dos Santos Junior - 289423: Roteirista e Designer",
        "Gustavo Soares Almeida - 284005: Game Artist",
        "Letícia Lauriano De Oliveira - 173008: Roteirista",
        "Victor Hugo Silva - 253078: Game Artist",
        "Nathan Damico Cardoso - 173537: Game Artist",
        "Matheus Henrique Ramos Da Silva - 281437: Game Artist"
];

// Se houver lógica de animação na UI (ex: barra de vida diminuindo suavemente),
// você inicializaria as variáveis de interpolação aqui.
health_display = 0;