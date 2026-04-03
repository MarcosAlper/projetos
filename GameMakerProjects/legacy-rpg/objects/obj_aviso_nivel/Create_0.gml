texto_aviso = "";

duracao = game_get_speed(gamespeed_fps) * 3 // Segundos

gui_w = display_get_gui_width();
gui_h = display_get_gui_height();

x_pos = gui_w / 2;
y_pos = gui_h - 100;

// fade
fade_rate_in = 0.0333 // 1/2 seg
fade_rate_out = 0.166; // 1 seg
image_alpha = 0;
