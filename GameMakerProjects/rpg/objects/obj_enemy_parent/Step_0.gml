if (global.show_final_screen) 
{
    image_speed = 0;
    exit;
}

if (instance_exists(obj_dialog))
{
    image_speed = 0;
    exit;
}

if (image_speed == 0)
{
    image_speed = 1;
}

var _player_exists = instance_exists(obj_player);
var _dist = distance_to_object(obj_player);

var _should_follow_player = (_player_exists && _dist < distance_to_player);

if (_should_follow_player) 
{
    if (array_length(global.player_history) >= global.player_history_size)
    {
        var _delay_index = global.player_history_size - 1; 
                
        var _past_x = global.player_history[_delay_index][0];
        var _past_y = global.player_history[_delay_index][1];

        if (_dist > approach_distance)
        {
            target_x = _past_x; 
            target_y = _past_y;
        }
        else
        {
            target_x = x; 
            target_y = y;
        }
    }
}

if (_player_exists && _dist <= attack_range && alarm[2] < 0)
{
    if (obj_player.alarm[0] < 0)
    {
        obj_player.hp -= damage;
        obj_player.alarm[0] = 50;
        obj_player.image_blend = c_red;
    }
    
    alarm[2] = 60;
}

if (alarm[1] >= 0)
{
    target_x = x + kb_x;
    target_y = y + kb_y;
}

var _dir = point_direction(x, y, target_x, target_y);
var _len_raw = point_distance(x, y, target_x, target_y);

var _len = (_len_raw > 0) ? 1 : 0; 

var _hor = lengthdir_x(_len, _dir);
var _ver = lengthdir_y(_len, _dir);

var _collision_list = [tilemap, obj_enemy_parent, obj_player];
move_and_collide(_hor * move_speed, _ver * move_speed, _collision_list);
