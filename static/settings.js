console.log("These are the settings");

var currentMap = "smallMap";
var cityDictionaries;

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

var toggle_visible = function toggle_visible(id){
		var el = document.getElementById(id);
		if (el.style.visibility == "hidden")
				el.style.visibility = "visible";
		else
				el.style.visibility = "hidden";
};

var switchMap = function switchMap(){
		console.log(currentMap);
		if (currentMap == "smallMap"){
				$("chatbox").hide();
				$("#chat-select").hide();
				currentMap = "bigMap";
				$.get("/get_functions", {type: "get_map", a: cityname}, function(data){
						console.log(data);
						cityDictionaries = JSON.parse(data);
						change(currentMap);
				});
		}
		else {
				currentMap = "smallMap";
				change(currentMap);
				$.get("/get_functions", {type: "get_city_buildings", a: cityname}, function(data){
						setupBuildings(data);
						overviewBuildings(data);
				});
		}
		toggle_visible("build-bar");
		toggle_visible("sideoptions");
};



var updateInterval;
$(document).ready(function(){
		console.log("ready");
		hoverOptions();
		clickOptions();
		setupChat();
		setupBuild();
		setupInfo();

		var map = document.getElementById("map-icon");
		map.addEventListener("click", switchMap);

		updateInterval = setInterval(updateInfo, 5000);
		
});
