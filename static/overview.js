console.log("Here is the overview");

/*Brings up the city overview screen
 */
var overview = function overview(){
    $('#overview-form').modal();
};

var updateOverview = function updatOverview(data, type){
    console.log("This will do something eventually");
		/*
			switch (type){
			case "resources":
			break;
			case "modifiers":
			break;
			default:
			break;
			}
		*/
};


var updateNavbar = function updateNavbar(data){
    console.log("This will do something eventually");
};

var updateInfo = function updateInfo(){
    $.get("/get_functions", {type: "get_resources"}, function(data){
				console.log(data);
				updateOverview(data, "resources");
				updateNavbar(data);
    });
    $.get("/get_functions", {type: "get_multipliers"}, function(data){
				console.log(data);
				updateOverview(data, "multipliers");
    });	
};
