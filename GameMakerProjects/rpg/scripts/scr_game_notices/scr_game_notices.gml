function create_game_notice(_message){
    var _notice = instance_create_layer(0, 0, "Instances", obj_aviso_nivel);
    
    _notice.titulo = _message.titulo;
    _notice.msg = _message.msg;
    _notice.image_alpha = 0;
    
    _notice.duracao = game_get_speed(gamespeed_fps) * 2;
    
    return _notice;
}