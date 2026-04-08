/*
obj_ui_controller
	Responsabilidades:
		1. Gestão e Exibição de Status (HUD)
		2. Interface de Entrada de Toque (Mobile UI)
		3. Gestão de Telas de Estado Global
		4. Otimização de Performance da UI
		5.Controle de Fluxo de Mensagens
*/

if (!variable_global_exists("show_final_screen"))
{
    global.show_final_screen = false;
}

btn_attack_visible = false;

btn_attack_timer = 0;
btn_attack_timeout = 180;
