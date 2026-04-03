function scr_npc_interactions(_inst)
{
    if(instance_exists(_inst.exclamation))
    {
        instance_destroy(_inst.exclamation);
        _inst.exclamation = noone;
    }
    
    create_dialog(_inst.dialog);
    
    if (instance_exists(obj_player))
    {
        obj_player.dialog_cooldown = 40;
        obj_player.input_block = true; 
    }
    
    if (instance_exists(obj_dialog))
    {
        if (_inst.final_fase1)
        {
            obj_dialog.final_npc_type = 1;
        }
        else if (_inst.final_fase2)
        {
            obj_dialog.final_npc_type = 2;
        }
        else if (_inst.final_fase3)
        {
            obj_dialog.final_npc_type = 3;
        }
    }
}

