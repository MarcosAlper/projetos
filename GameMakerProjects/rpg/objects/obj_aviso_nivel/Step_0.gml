if (global.show_final_screen) 
{
    exit;
}
if (duracao > 0 && image_alpha < 1)
{
    image_alpha = min(1, image_alpha + fade_rate_in);
    exit;
}
// Lógica de espera (Hold)
if (image_alpha >= 1 && duracao > 0)
{
    duracao--;
}

// Controle do Fade Out
if (duracao <= 0)
{
    image_alpha = max(0, image_alpha - fade_rate_out);
}

// Destruição
if (image_alpha <= 0)
{
    instance_destroy();
}
