/* ENVIADO PARA obj_ui_controller /
if (!variable_global_exists("show_final_screen"))
{
    global.show_final_screen = false;
}*/

tilemap = layer_tilemap_get_id("Tiles_Col");

facing = 0;

hp = 10;
hp_total = hp;
move_speed = 1;
attack_cooldown_duration = 10;
level = 1;
xp = 0;
damage = 1;

/* ENVIADO PARA obj_ui_controller /
btn_attack_visible = false;*/

/* ENVIADO PARA obj_ui_controller /
btn_attack_timer = 0;
btn_attack_timeout = 180;*/

global.player_history_size = 40;
global.player_history = array_create(global.player_history_size, [0, 0]);

/* ENVIADO PARA scr_input_manager /
dialog_cooldown = 0;
input_block = false;*/

/* ENVIADO PARA scr_input_managaer /
joystick = {
    finger: -1,
    anchorx: 0,
    anchory: 0,
    x: 0,
    y: 0,
    max_distance: 80
};*/

/* ENVIADO PARA scr_input_managaer /
btn_attack_finger = -1
btn_attack_size = 175;
btn_attack_x = 0;
btn_attack_y = 0;*/

/* ENVIADO PARA scr_progression_system
xp_require = 100;*/

/* ENVIADO PARA scr_progression_system
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
}*/
