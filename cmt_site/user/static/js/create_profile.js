function display_group_input() {
    if(document.getElementById("group").value == "Yes") {
        document.getElementById("group_input").style.display = 'block';
    
    } else {
        document.getElementById("group_input").style.display = 'none';
    
    }
}

function add_system() {
    document.getElementById('add_sys').style.display = 'block';
}