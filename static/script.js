var show = document.getElementById("male");
show.addEventListener("click", hide_preg);

var hide = document.getElementById("female");
hide.addEventListener("click", display_preg);

function display_preg() {
    var preg = document.getElementById("no_preg");
    preg.style.display = "inline";
    var preg_label = document.getElementById("preg_label");
    preg_label.style.display = "inline";
}

function hide_preg() {
    var preg = document.getElementById("no_preg");
    preg.style.display = "none";
    var preg_label = document.getElementById("preg_label");
    preg_label.style.display = "none";
}

function hide_on_run() {
    var executed = false;
    if (!executed) {
        executed = true;
        hide_preg();
    }
}

hide_on_run()
