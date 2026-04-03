if (global.show_final_screen) 
{
    exit;
}

array_insert(global.player_history, 0, [x, y]);

if (array_length(global.player_history) > global.player_history_size)
{
    array_delete(global.player_history, global.player_history_size, 1);
}

if (dialog_cooldown > 0)
{
    dialog_cooldown--;
}

if (input_block)
{
    input_block = false;
}
