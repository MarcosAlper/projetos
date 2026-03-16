if (!variable_global_exists("show_final_screen"))
{
    global.show_final_screen = false;
}

dialog_cooldown = 0;
input_block = false;

btn_attack_visible = false;
btn_attack_timer = 0;
btn_attack_timeout = 180;

joystick = {
    finger: -1,
    anchorx: 0,
    anchory: 0,
    x: 0,
    y: 0,
    max_distance: 80
};

btn_attack_finger = -1
btn_attack_size = 175;

btn_attack_x = 0;
btn_attack_y = 0;

move_speed = 1;
global.player_history_size = 40;
global.player_history = array_create(global.player_history_size, [0, 0]); 
attack_cooldown_duration = 10;

tilemap = layer_tilemap_get_id("Tiles_Col");

hp = 10;
hp_total = hp;
damage = 1;

facing = 0;

level = 1;
xp = 0;
xp_require = 100;

function add_xp(_xp_to_add)
{
    xp += _xp_to_add;
    if (xp >= xp_require)
    {
        level++;
        xp -= xp_require;
        xp_require *= 1.4;
        
        hp_total += 5;
        hp = hp_total;
        damage += 0.8;
        
        create_game_notice({
            titulo: "Evolução de Nível",
            msg: $"Nível: {self.level}\nVida: {self.hp_total}\nAtaque: {self.damage}"
        })
    }
}
