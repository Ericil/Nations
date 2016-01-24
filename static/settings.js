console.log("These are the settings");

/*Adds mouseover events to buttons
	Mouse over and out on options button to view options
	Mouse over options to view descriptions
*/
var hoverOptions = function hoverOptions(){
    $("#options").mouseover(function(){
				$(".btn-option").each(function(i){
						if (i > 0)
								$(this).fadeIn();
				});
    });

    $("#sideoptions").mouseleave(function(){
				$(".btn-option").each(function(i){
						if (i > 0)
								$(this).fadeOut();	
				});
    });
    
    $('[data-toggle="tooltip"]').tooltip();
};



/*Adds click events to buttons
  Run a different function depending on the button
*/
var clickOptions = function clickOptions(){
    var options = document.getElementById("sideoptions");
    options.addEventListener("click", function(e){
				console.log(e.target.id);
				switch(e.target.id) {
				case "overview":
						overview();
						break;
				case "message":
						message();
						break;
				case "build":
						build();
						break;
				}
    });
};

var updateInterval;

$(document).ready(function(){
		console.log("ready");
		hoverOptions();
		clickOptions();
		setupChat();
		setupBuild();
		setupInfo();

		//updateInterval = setInterval(updateInfo, 5000);
		
});
