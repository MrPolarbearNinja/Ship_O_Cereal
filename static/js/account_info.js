window.onload = function() {
    if (window.location.pathname === "/account/profile") {
        display_save_msg();
    }
}

function display_save_msg() {
    var load = localStorage.getItem("load")
    if (load == "true") {
        let resetAttr = () => {
            document.getElementById("myacc-success").style.display = "none";
        }
        setTimeout(resetAttr, 3000);
        document.getElementById("myacc-success").style.display = "inline-flex";
    }
    load = "false";
    localStorage.setItem("load", load);
}

function save_changes_acc() {
    /* setItem only takes in strings */
    var load = "true";
    localStorage.setItem("load", load);
}