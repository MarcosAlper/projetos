function create_dialog(_messages){
    if (instance_exists(obj_dialog)) return;
    
    if (instance_exists(obj_player))
    {
        if (obj_player.sprite_index == spr_player_walk_right)
        {
            obj_player.sprite_index = spr_player_idle_right;
        } else if (obj_player.sprite_index == spr_player_walk_left)
        {
            obj_player.sprite_index = spr_player_idle_left;
        } else if (obj_player.sprite_index == spr_player_walk_up)
        {
            obj_player.sprite_index = spr_player_idle_up;
        } else if (obj_player.sprite_index == spr_player_walk_down)
        {
            obj_player.sprite_index = spr_player_idle_down
        }
        
        obj_player.image_index = 0;
    }
    
    var _inst = instance_create_depth(0, 0, 0, obj_dialog);
    _inst.messages = _messages;
    _inst.current_message = 0;
}

char_colors = {
    "Desconhecido": c_yellow,
    "Eike": c_yellow,
    "Marcos": c_aqua,
    "Helio": c_orange
}

room1_end = [
{
    name: "Eike",
    msg: "Foi bem difícil chegar aqui sem ser visto pelos monstros..."
},
{
    name: "Eike",
    msg: "Tem um caminho mais para baixo da masmorra, mas parece que tem monstros lá também..."
},
{
    name: "Eike",
    msg: "Nos vemos no próximo andar."
}
]

room2_end = [
{
    name: "Eike",
    msg: "A ponte está quebrada e eu não acho que conseguimos pular para o outro lado."
},
{
    name: "Eike",
    msg: "Por sorte, encontramos uma passagem secreta em uma parede falsa."
},
{
    name: "Eike",
    msg: "Vamos ter que descer de novo."
},
{
    name: "Helio",
    msg: "Acho que ouvi o farfalhar de um morcego vindo do andar de baixo..."
},
{
    name: "Helio",
    msg: "Não que eu esteja com medo, mas... Você não prefere ir na frente?..."
},
]

room3_end = [
{
    name: "Eike",
    msg: "É bom te ver de novo."
},
{
    name: "Eike",
    msg: "Fiquei com medo que você se perdesse no labirinto..."
},
{
    name: "Eike",
    msg: "Será que alguém já viveu nesse lugar?..."
},
{
    name: "Helio",
    msg: "Tem mais um andar para baixo."
},
{
    name: "Helio",
    msg: "Será que a saída está próxima?..."
},
]

dialogo_eike1 = [
{
    name: "Desconhecido",
    msg: "Olá, estranho."
},
{
    name: "Desconhecido",
    msg: "Você também não sabe como veio parar aqui?"
},
{
    name: "Desconhecido",
    msg: "Já procuramos por toda a parte... Não tem saída."
},
{
    name: "Desconhecido",
    msg: "Talvez tenha algo no fim da masmorra."
},
{
    name: "Desconhecido",
    msg: "Eu sou o Eike. Aquele ali é Helio."
},
{
    name: "Eike",
    msg: "Ele parece amedrontado demais para conversar, mas você pode tentar falar com ele se quiser..."
}
]

dialogo_helio1 = [
{
    name: "Helio",
    msg: "Oi..."
},
{
    name: "Helio",
    msg: "Você vai tirar a gente daqui... não é?..."
},
{
    name: "Helio",
    msg: "Por favor, nos salve!"
},
{
    name: "Helio",
    msg: "Eu não quero morrer aqui!"
}
]