// // // The program is used to to predict diabetes occurance.

// // // Copyright (C) 2022  Syed Salman Habeeb Quadri

// // // This program is free software: you can redistribute it and/or modify
// // // it under the terms of the GNU General Public License as published by
// // // the Free Software Foundation, either version 3 of the License, or
// // // (at your option) any later version.

// // // This program is distributed in the hope that it will be useful,
// // // but WITHOUT ANY WARRANTY; without even the implied warranty of
// // // MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// // // GNU General Public License for more details.

// // // The GNU General Public License does not permit incorporating this program
// // // into proprietary programs.

// // // You should have received a copy of the GNU General Public License
// // // along with this program.  
// // // If not, see [GNU General Public License](https://www.gnu.org/licenses/).

var show = document.getElementById("male");
show.addEventListener("click", hide_preg);

var hide = document.getElementById("female");
hide.addEventListener("click", display_preg);

function display_preg() {
    var preg = document.getElementById("no_preg");
    var preg_label = document.getElementById("preg_label");
    var width = window.innerWidth;
    if (width <= 800) {
        preg.style = "text-align: center; align-items: flex-start;";
        preg_label.style.display = "flex";
    }
    else {
        preg.style.display = "inline";
        preg_label.style.display = "inline";
    }
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
