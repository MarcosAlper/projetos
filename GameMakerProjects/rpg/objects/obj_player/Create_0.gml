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

// Atalho para o obj_ui_controller
ui = instance_find(obj_ui_controller, 0);

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
