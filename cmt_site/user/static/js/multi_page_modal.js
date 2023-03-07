function show_field(fieldset, btn) {
    document.getElementById('set_1').style.display = 'none';
    document.getElementById('set_2').style.display = 'none';    
    document.getElementById('set_3').style.display = 'none';
    document.getElementById(fieldset).style.display = 'block';

    document.getElementById('btn_back').style.display = 'block';
    document.getElementById('btn_remove').style.display = 'none';
    
    document.getElementById('btn_next_1').style.display = 'none';
    document.getElementById('btn_next_2').style.display = 'none';    
    document.getElementById('btn_save').style.display = 'none';
    document.getElementById(btn).style.display = 'block';
}