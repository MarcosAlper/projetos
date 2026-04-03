draw_set_alpha(image_alpha);

var _boxw = 400;
var _boxh = 125;
var _dx = x_pos - (_boxw / 2);
var _dy = y_pos - 50;

// Painel de fundo
draw_sprite_stretched(spr_box, 0, _dx, _dy, _boxw, _boxh);

// Texto
draw_set_font(Font1);
draw_set_valign(fa_top);

var _padding_y = 10;
var _msg_margin_x = 20;
var _titulo_msg_space = 10;

draw_set_color(c_yellow);

var _titulo_y = _dy + _padding_y;

// Desenha o texto centralizado na caixa
draw_set_halign(fa_center);
draw_text(_dx + (_boxw / 2), _titulo_y, titulo);
draw_set_halign(fa_left);

draw_set_color(c_white);

var _altura_titulo = string_height(titulo);
var _msg_y = _titulo_y + _altura_titulo + _titulo_msg_space;

var _msg_x_start = _dx + _msg_margin_x;
var _msg_max_w = _boxw - (_msg_margin_x * 2);

draw_text_ext(_msg_x_start, _msg_y, msg, -1, _msg_max_w);

// Restaura as configs.
draw_set_valign(fa_top);
draw_set_alpha(1);
draw_set_color(c_white);
