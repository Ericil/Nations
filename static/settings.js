console.log("These are the settings");

/*Adds mouseover events to buttons
	Mouse over and out on options button to view options
	Mouse over options to view descriptions
*/
var hoverOptions = function hoverOptions(){
    $("#options").mouseover(function(){
				$(".btn-group-vertical button").each(function(i){
						if (i > 0)
								$(this).fadeIn();
				});
		});

		$("#sideoptions").mouseleave(function(){
				$(".btn-group-vertical button").each(function(i){
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
				switch(e.target.id) {
				case "overview":
						showOverview();
						break;
				case "message":
						message();
						break;
				case "buildinfo":
						showBuildInfo();
						break;
				case "build":
						build();
				}
		});
};


/*Brings up the city overview screen
 */
var showOverview = function showOverview(){
		var form = document.getElementById("overview-popup");
		form.style.display = "block";
};


hoverOptions();
clickOptions();
