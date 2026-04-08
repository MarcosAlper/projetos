function scr_progression_system(){
	xp_require = 100;
}

function add_xp(_xp_to_add)
{
    xp += _xp_to_add;
    if (xp >= xp_require)
    {
        level++;
        xp -= xp_require;
        xp_require *= 1.4;
        
        hp_total += 5;
        hp = hp_total;
        damage += 0.8;
        
        create_game_notice({
            titulo: "Evolução de Nível",
            msg: $"Nível: {self.level}\nVida: {self.hp_total}\nAtaque: {self.damage}"
        })
    }
}
