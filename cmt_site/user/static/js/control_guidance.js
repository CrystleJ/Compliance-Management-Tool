function set_values(control) {
    var control_id = control.getAttribute("data-control-id");
    var control_txt = control.getAttribute("data-control-txt");
    var discussion = control.getAttribute("data-discussion");
    console.log(control_id);
    
    document.getElementById('modal_control_id').innerHTML = control_id;
    document.getElementById('modal_control_txt').innerHTML = control_txt;
    document.getElementById('modal_discussion').innerHTML = discussion;
  }