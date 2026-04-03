final_npc_type = 0;

messages = [];
current_message = -1
current_char = 0;
draw_message = "";

char_speed = 0.7;
is_dialog_input_active = false;
input_key = vk_space;
dialog_cooldown = 0;
dialogo_finalizado = false;

alarm[0] = -1;

gui_w = display_get_gui_width();
gui_h = display_get_gui_height();

next_room = false;
