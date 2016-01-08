console.log("These are the settings");

var makeOptions = function makeOptions(){
    var button = document.createElement("button");
    button.type = "button";
    button.className = "btn btn-primary btn-circle";
    var icon = document.createElement("span");
    icon.className = "glyphicon glyphicon-list";

    button.appendChild(icon);
    document.getElementById("sideoptions").appendChild(button);

};


$("#options").mouseover(function(){
		$(".btn-group-vertical button").each(function(i){
				console.log(this);
				if (i > 0){
						$(this).fadeIn();
				}
		});
});

$("#sideoptions").mouseleave(function(){
		$(".btn-group-vertical button").each(function(i){
				console.log(this);
				if (i > 0){
						$(this).fadeOut();
				}
		});
});
