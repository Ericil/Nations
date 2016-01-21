console.log("Here is the overview");

/*Brings up the city overview screen
 */
var overview = function overview(){
		$('#overview-form').modal();
};

var updateOverview = function updatOverview(data){
		console.log("This will do something eventually");
};

var updateNavbar = function updateNavbar(data){
		console.log("This will do something eventually");
};

var updateInfo = function updateInfo(){
		$.get("/functions", {type: "resources"}, function(data){
				console.log(data);
				updateOverview(data);
				updateNavbar(data);
		});	
};
