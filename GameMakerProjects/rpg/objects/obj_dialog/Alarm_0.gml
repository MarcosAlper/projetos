instance_destroy();

if (final_npc_type != 0)
{
    if (instance_exists(obj_player))
    {
        with (obj_player)
        {
            global.transfer_level = level;
            global.transfer_xp = xp;
            global.transfer_xp_require = xp_require;
            global.transfer_hp = hp;
            global.transfer_hp_total = hp_total;
            global.transfer_damage = damage;
        }
    }
    
    switch (final_npc_type)
    {  
    	case 1:
            room_goto(Room2);
            break;
            
    	case 2:
            room_goto(Room3);
            break;
            
    	case 3:
            global.show_final_screen = true;
            break;
        }
}
