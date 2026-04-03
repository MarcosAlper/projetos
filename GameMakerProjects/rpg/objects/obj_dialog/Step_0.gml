if (global.show_final_screen) 
{
    exit;
}
if (dialogo_finalizado) 
{
    exit;
}
var _input_is_active = keyboard_check(input_key);

for (var i = 0; i < 5; i++)
{
    if (device_mouse_check_button(i, mb_left))
    {
        _input_is_active = true;
    }
}

is_dialog_input_active = _input_is_active;

if (dialog_cooldown > 0)
{
    dialog_cooldown--;
}
else
{
    var _should_advance = keyboard_check_pressed(input_key);
    
    for (var i = 0; i < 5; i++)
    {
        if (device_mouse_check_button_pressed(i, mb_left))
        {
            _should_advance = true;
            break;
        }
    }
    
    if (_should_advance)
    {
        if (current_message >= array_length(messages))
        {
            if (instance_exists(obj_player))
            {
                obj_player.dialog_cooldown = 40;
                obj_player.input_block = true; 
            }
            alarm[0] = 1; 
            exit;
        }
    
        var _str_len = string_length(messages[current_message].msg);

        if (current_char < _str_len)
        {
            current_char = _str_len;
        }
        else
        {
            current_message++;
            
            if (current_message >= array_length(messages))
            {
                dialogo_finalizado = true; 

                if (instance_exists(obj_player))
                {
                    obj_player.dialog_cooldown = 40;
                    obj_player.input_block = true; 
                }
                
                alarm[0] = 1;
                exit;
            }
            else
            {
                current_char = 0;
                dialog_cooldown = 40;
            }
        }
    }
}

if (!dialogo_finalizado && current_message >= 0 && current_message < array_length(messages))
{
    var _str = messages[current_message].msg;

    if (current_char < string_length(_str))
    {
        var _acceleration_factor = 1 + real(is_dialog_input_active); 
        
        current_char += char_speed * (2 * _acceleration_factor);
        draw_message = string_copy(_str, 0, current_char);
    }
}
