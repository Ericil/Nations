console.log("These are the settings");

var makeOptions = function makeOptions(){
    var button = document.createElement("button");
    button.type = "button";
    button.className = "btn btn-primary btn-circle btn-lg";
    var icon = document.createElement("span");
    icon.className = "glyphicon glyphicon-list";

    button.appendChild(icon);
    document.getElementById("sideoptions").appendChild(button);

};


makeOptions();
