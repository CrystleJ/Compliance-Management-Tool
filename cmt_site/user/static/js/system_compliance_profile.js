function change_per() {
    if(document.getElementById("compliance_status").value == "NR") {
        document.getElementById("ctr_compliant").innerHTML = '0';
        document.getElementById("ctr_not_compliant").innerHTML = '0';
        document.getElementById("ctr_not_applicable").innerHTML = '0';
        document.getElementById("ctr_not_reviewed").innerHTML = '1189';

        document.getElementById("AC-10_status").innerHTML = "Not Reviewed";

    } else if(document.getElementById("compliance_status").value == "C") {
        document.getElementById("ctr_compliant").innerHTML = '13/20 (65%)';
        document.getElementById("ctr_not_compliant").innerHTML = '3/20 (15%)';
        document.getElementById("ctr_not_applicable").innerHTML = '2/20 (10%)';
        document.getElementById("ctr_not_reviewed").innerHTML = '2/20 (10%)';

        document.getElementById("AC-10_status").innerHTML = "Compliant";

    } else if(document.getElementById("compliance_status").value == "NC") {
        document.getElementById("ctr_compliant").innerHTML = '0';
        document.getElementById("ctr_not_compliant").innerHTML = '1';
        document.getElementById("ctr_not_applicable").innerHTML = '0';
        document.getElementById("ctr_not_reviewed").innerHTML = '1179';

        document.getElementById("AC-10_status").innerHTML = "Not Compliant";
    } else {
        document.getElementById("ctr_compliant").innerHTML = '0';
        document.getElementById("ctr_not_compliant").innerHTML = '0';
        document.getElementById("ctr_not_applicable").innerHTML = '1';
        document.getElementById("ctr_not_reviewed").innerHTML = '1179';

        document.getElementById("AC-10_status").innerHTML = "Not Applicable";
    }
}

function control_select(control_id) {
    if(control_id == "AC-1") {
        document.getElementById(control_id).style.display = 'block';      
        document.getElementById("AC-10").style.display = 'none';
    } else {
        document.getElementById(control_id).style.display = 'block';      
        document.getElementById("AC-1").style.display = 'none';
    }
}