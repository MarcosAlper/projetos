input_key = vk_space;
can_talk = false;

exclamation = noone;

if (dialog != -1)
{
    exclamation = instance_create_depth(x - 10, y - 20, depth - 1, obj_exclamation);
    
    exclamation.image_xscale = 0.8
    exclamation.image_yscale = 0.8
    
    exclamation.depth = depth - 1;
}
