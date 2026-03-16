var _dx = 16;
var _dy = 16;
var _barw = 256;
var _barh = 32;

// Propriedades
draw_set_font(Font1);
draw_set_halign(fa_center);
draw_set_valign(fa_middle);

// Healthbar
var _health_barw = _barw * (hp / hp_total);

draw_sprite_stretched(spr_box, 0, _dx, _dy, _barw, _barh);
draw_sprite_stretched_ext(spr_box, 1, _dx, _dy, _health_barw,_barh, c_red, 0.6);

draw_text(_dx + _barw / 2, _dy + _barh / 2, "Vida");

// XP
var _xp_barw = _barw * (xp / xp_require);
_dy += _barh + 8

draw_sprite_stretched(spr_box, 0, _dx, _dy, _barw, _barh);
draw_sprite_stretched_ext(spr_box, 1, _dx, _dy, _xp_barw, _barh, c_blue, 0.6);

draw_text(_dx + _barw / 2, _dy + _barh / 2, $"Nível {level}");

// Resetar propriedades
draw_set_halign(fa_left);
draw_set_valign(fa_top);

// Joystick
if(joystick.finger != -1)
{
    draw_sprite(spr_joystick, 0, joystick.x, joystick.y);
}

var _btn_x = display_get_gui_width() - 200;
var _btn_y = display_get_gui_height() - 150;

var _spr_w = sprite_get_width(spr_attack_button);

var _scale_factor = btn_attack_size / _spr_w;

var _sub_img = (btn_attack_finger != -1) ? 1 : 0;

if(joystick.finger != -1)
{
    draw_sprite(spr_joystick, 0, joystick.x, joystick.y);
}

var _btn_x = display_get_gui_width() - 200;
var _btn_y = display_get_gui_height() - 150;

var _spr_w = sprite_get_width(spr_attack_button);

var _scale_factor = btn_attack_size / _spr_w;

var _sub_img = (btn_attack_finger != -1) ? 1 : 0;

if (btn_attack_visible)
{
    draw_sprite_ext(spr_attack_button, _sub_img, _btn_x, _btn_y, _scale_factor, _scale_factor, 0, c_white, 1);
}
if (global.show_final_screen)
{
    var _margin = 50;
    var _gw = display_get_gui_width();
    var _gh = display_get_gui_height();
    
    var _box_x1 = _margin;
    var _box_y1 = _margin;
    var _box_x2 = _gw - _margin;
    var _box_y2 = _gh - _margin;
    var _box_width = _box_x2 - _box_x1;
    var _box_height = _box_y2 - _box_y1;
    
    var _inner_margin = 50; 
    
    var _draw_start_x = _box_x1 + _inner_margin; 
    
    var _wrap_limit_x = _box_x2 - _inner_margin; 
    
    var _wrap_width = _wrap_limit_x - _draw_start_x; 

    var _box_sprite = spr_box;
    var _box_alpha = 0.95;
    var _box_color = c_black;
    
    draw_sprite_stretched_ext(_box_sprite, 0, _box_x1, _box_y1, _box_width, _box_height, _box_color, _box_alpha);

    draw_set_font(Font2);
    draw_set_halign(fa_left);
    draw_set_color(c_white);
    
    var _final_message = [
        "Parabéns!",
        "Você chegou ao fim da versão Alpha do jogo!",
        "Este projeto é um Protótipo Alpha em desenvolvimento ativo. O feedback de vocês é extremamente importante para aprimorar os sistemas de combate e diálogo. Agradecemos a todos por jogar e contribuir com o projeto.",
        "Se você compartilha do nosso interesse em Desenvolvimento de Games, você pode me chamar a qualquer momento para conversarmos sobre.",
        "Contato:",
        "Whatsapp - (11) 9 1478-9089",
        "Email - marcosneto1902@outlook.com",
        "",
        "Créditos:",
        "Marcos Almeida Pereira Neto - 194897: Game Director, Game Designer e Programador",
        "Eike Henrique Souza Da Rocha - 281410: Game Artist e Game Designer",
        "Helio Pereira Dos Santos Junior - 289423: Roteirista e Designer",
        "Gustavo Soares Almeida - 284005: Game Artist",
        "Letícia Lauriano De Oliveira - 173008: Roteirista",
        "Victor Hugo Silva - 253078: Game Artist",
        "Nathan Damico Cardoso - 173537: Game Artist",
        "Matheus Henrique Ramos Da Silva - 281437: Game Artist"
    ];

    var _wrapped_text = [];
    var _line_height = 22;
    
    for (var i = 0; i < array_length(_final_message); i++)
    {
        var _text = _final_message[i];
        
        if (_text == "")
        {
            array_push(_wrapped_text, "");
            continue;
        }
        
        var _words = string_split(_text, " ");
        var _current_line = "";

        for (var j = 0; j < array_length(_words); j++)
        {
            var _word = _words[j];
            
            var _test_line = _current_line + (string_length(_current_line) == 0 ? "" : " ") + _word;
            
            if (string_width(_test_line) > _wrap_width)
            {
                array_push(_wrapped_text, _current_line);
                _current_line = _word;
            }
            else
            {
                _current_line = _test_line;
            }
        }
        
        array_push(_wrapped_text, _current_line);
    }

    draw_set_valign(fa_top);
    
    var _draw_start_y = _box_y1 + _inner_margin; 
    
    for (var i = 0; i < array_length(_wrapped_text); i++)
    {
        if (i == 1 || i == 2 || i == 6 || i == 9 || i == 10 || i > 12)
        {
            draw_text(_draw_start_x, _draw_start_y + (i * _line_height), "   " + _wrapped_text[i]);
        }
        else
        {
            draw_text(_draw_start_x, _draw_start_y + (i * _line_height), _wrapped_text[i]);
        }
    }
}
