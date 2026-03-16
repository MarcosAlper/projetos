if (global.show_final_screen) 
{
    exit;
}
if (instance_exists(obj_dialog)) 
{
    exit;
}

if(instance_exists(exclamation))
{
    exclamation.x = x - 10;
    exclamation.y = y - 20;
}

if(instance_exists(obj_player) && distance_to_object(obj_player) < 25 && dialog != -1)
{
    can_talk = true;
    
    if (keyboard_check_pressed(input_key))
    {
        scr_npc_interactions(id);
    }
}
else
{
    can_talk = false;
}
