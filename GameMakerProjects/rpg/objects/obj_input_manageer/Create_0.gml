// Este objeto será persistente e cuidará de toda a matemática chata
// de dedos e coordenadas

// Dados do Joystick (movidos para cá)
joystick = {
    finger: -1,
    anchorx: 0,
    anchory: 0,
    x: 0,
    y: 0,
    max_distance: 80
};

// Dados do Botão de Ataque
btn_attack_visible = false;
btn_attack_timer = 0;
btn_attack_timeout = 180;

btn_attack_finger = -1

// Direção final que o Player vai ler
input_x = 0;
input_y = 0;
input_dir = 0;
input_active = false;

dialog_cooldown = 0;
input_block = false;