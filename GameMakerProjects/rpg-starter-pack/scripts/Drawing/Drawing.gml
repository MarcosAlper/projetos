function draw_shadow(_offsetx=0, _offsety=0)
{
    draw_sprite_ext(spr_shadow, 0, x + _offsetx, y + _offsety, 1, 1, 0, -1, 0.4);
}
