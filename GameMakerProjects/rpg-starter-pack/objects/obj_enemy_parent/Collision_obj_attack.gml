if (alarm[1] < 0)
{
    hp -= other.damage;
    
    image_blend = c_red;
    alarm[3] = 10;
    
    kb_x = sign(x - other.x);
    kb_y = sign(y - other.y);
    alarm[1] = 20;
}
