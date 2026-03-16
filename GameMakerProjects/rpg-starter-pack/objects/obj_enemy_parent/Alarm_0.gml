var _player_exists = instance_exists(obj_player);
var _dist = distance_to_object(obj_player);

if (!(_player_exists && _dist < distance_to_player)) 
{
    target_x = random_range(xstart - 100, xstart + 100);
    target_y = random_range(ystart - 100, ystart + 100);
}

alarm[0] = 50;
