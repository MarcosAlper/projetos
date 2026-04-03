if (global.show_final_screen) 
{
    exit;
}

if (instance_exists(obj_dialog))
{
    btn_attack_visible = false;
    joystick.visible = false;
    exit; 
}


var _btn_x = display_get_gui_width() - 200;
var _btn_y = display_get_gui_height() - 150;
var _half_size = btn_attack_size / 2;
var _left = _btn_x - _half_size;
var _top = _btn_y - _half_size;
var _right = _btn_x + _half_size;
var _bottom = _btn_y + _half_size;

var _is_any_touch_active = false;

for (var i = 0; i < 5; i++)
{
    if (device_mouse_check_button(i, mb_left))
    {
        _is_any_touch_active = true;
        break;
    }
}

if (instance_exists(obj_dialog))
{
    btn_attack_visible = false;
    joystick.visible = false;
}
else if (_is_any_touch_active)
{
    btn_attack_visible = true;
    btn_attack_timer = btn_attack_timeout;
    joystick.visible = true;
}
else
{
    if (btn_attack_timer > 0)
    {
        btn_attack_timer--;
    }
    
    if (btn_attack_timer <= 0)
    {
        btn_attack_visible = false;
    }
}

var _final_hor = 0;
var _final_ver = 0;
var _dir = facing;

for (var i = 0; i < 5; i++)
{
    if (device_mouse_check_button_pressed(i, mb_left))
    {
        var fingerx = device_mouse_x_to_gui(i);
        var fingery = device_mouse_y_to_gui(i);
        var touch_world_x = device_mouse_x(i); 
        var touch_world_y = device_mouse_y(i);

        if (dialog_cooldown <= 0)
        {
            var _inst_npc = instance_position(touch_world_x, touch_world_y, obj_npc_parent); 
    
            if (instance_exists(_inst_npc))
            {
                var _dist_to_player = point_distance(x, y, _inst_npc.x, _inst_npc.y);
                var _max_dist = 64; 
    
                if (_dist_to_player <= _max_dist)
                {
                    scr_npc_interactions(_inst_npc);
                    break;
                }
            }
        }
        
        if (btn_attack_finger == -1 && point_in_rectangle(fingerx, fingery, _left, _top, _right, _bottom))
        {
            btn_attack_finger = i;
            break;
        }
        
        if(joystick.finger == -1)
        {
            
            joystick.finger = i;
            joystick.x = fingerx;
            joystick.y = fingery;
            joystick.anchorx = fingerx;
            joystick.anchory = fingery;
            break;
        }
    }

}

if (joystick.finger != -1)
{
    if (!device_mouse_check_button(joystick.finger, mb_left))
    {
        joystick.finger = -1;
    }

    else
    {
        var _curr_x = device_mouse_x_to_gui(joystick.finger);
        var _curr_y = device_mouse_y_to_gui(joystick.finger);
        
        var _dist = point_distance(joystick.anchorx, joystick.anchory, _curr_x, _curr_y);
        
        if (_dist <= joystick.max_distance)
        {
            joystick.x = _curr_x;
            joystick.y = _curr_y;
        }
        else
        {
            var _dir_temp = point_direction(joystick.anchorx, joystick.anchory, _curr_x, _curr_y);
            joystick.x = joystick.anchorx + lengthdir_x(joystick.max_distance, _dir_temp);
            joystick.y = joystick.anchory + lengthdir_y(joystick.max_distance, _dir_temp);
        }
    }
}
    
if (btn_attack_finger != -1)
{
    if (!device_mouse_check_button(btn_attack_finger, mb_left))
    {
        btn_attack_finger = -1;
    }
    else 
    {
        if (alarm[1] < 0) 
        {
            alarm[1] = 20;
            var _inst = instance_create_depth(x, y, depth, obj_attack);
            _inst.image_angle = facing;
            _inst.damage *= damage;
            
            btn_attack_finger = -1;
        }
    }
}

if(joystick.finger != -1)
{
    var _dist = point_distance(joystick.anchorx, joystick.anchory, joystick.x, joystick.y);
    var _len = min(_dist, joystick.max_distance) / joystick.max_distance;
    
    if (_len > 0.05)
    {
        _dir = point_direction(joystick.anchorx, joystick.anchory, joystick.x, joystick.y);
        
        _final_hor = lengthdir_x(_len, _dir);
        _final_ver = lengthdir_y(_len, _dir);
    }
}

if(_final_hor == 0 && _final_ver == 0)
{
    var _hor = keyboard_check(ord("D")) - keyboard_check(ord("A"));
    var _ver = keyboard_check(ord("S")) - keyboard_check(ord("W"));
    
    if(_hor != 0 || _ver != 0)
    {
        var _len = (_hor != 0 || _ver != 0);
        _dir = point_direction(0, 0, _hor, _ver);
    
        _final_hor = lengthdir_x(_len, _dir);
        _final_ver = lengthdir_y(_len, _dir);
    }
    
    if (keyboard_check_pressed(vk_space) && dialog_cooldown <= 0 && !input_block) 
    {
        if (alarm[1] < 0)
        {
            var _inst_npc = instance_nearest(x, y, obj_npc_parent); 
            var _dist = distance_to_object(_inst_npc);
            var _max_dist = 25;
            
            if (instance_exists(_inst_npc) && _dist <= _max_dist)
            {
                if (_inst_npc.dialog != -1)
                {
                scr_npc_interactions(_inst_npc);
                dialog_cooldown = 40;
                }
                else 
                {
                    alarm[1] = 20;
                    var _inst = instance_create_depth(x, y, depth, obj_attack);
                    _inst.image_angle = facing;
                    _inst.damage *= damage;
                }
            }
            else 
            {
                alarm[1] = 20;
                var _inst = instance_create_depth(x, y, depth, obj_attack);
                _inst.image_angle = facing;
                _inst.damage *= damage;
            }
        }
    }
}

var _is_moving = (_final_hor != 0 || _final_ver != 0);

var _collision_list = [tilemap, obj_enemy_parent];
move_and_collide(_final_hor * move_speed, _final_ver * move_speed, _collision_list, undefined, undefined, undefined, move_speed, move_speed);

if (_is_moving)
{
    facing = _dir;
    
    if (_dir >= 45 && _dir <= 135) 
    {
        sprite_index = spr_player_walk_up;
    } 
    else if (_dir > 135 && _dir < 225) 
    {
        sprite_index = spr_player_walk_left;
    } 
    else if (_dir >= 225 && _dir <= 315) 
    {
        sprite_index = spr_player_walk_down;
    } 
    else 
    {
        sprite_index = spr_player_walk_right;
    }
}
else
{
	if (sprite_index == spr_player_walk_right) sprite_index = spr_player_idle_right;
    else if (sprite_index == spr_player_walk_left) sprite_index = spr_player_idle_left;
    else if (sprite_index == spr_player_walk_up) sprite_index = spr_player_idle_up
    else if (sprite_index == spr_player_walk_down) sprite_index = spr_player_idle_down
}

if (hp <= 0)
{
    room_restart();
    exit;
}




with (all)
{
    depth = -bbox_bottom;
}

var _cam = view_camera[0];
var _cam_width = camera_get_view_width(_cam);
var _cam_height = camera_get_view_height(_cam);

var _cam_x = x - _cam_width / 2;
var _cam_y = y - _cam_height / 2;

_cam_x = clamp(_cam_x, 0, room_width - _cam_width);
_cam_y = clamp(_cam_y, 0, room_height - _cam_height);

camera_set_view_pos(_cam, _cam_x, _cam_y);
