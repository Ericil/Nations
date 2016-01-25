console.log("Here is the overview");

var username = document.getElementById("username").innerHTML;
var cityname = document.getElementById("cityname").innerHTML;


/*Brings up the city overview screen
 */
var overview = function overview(){
		$('#overview-form').modal();
};

var updateOverview = function updatOverview(data, type){
		var info = JSON.parse(data);
		switch (type){
		case "resources":
		case "multipliers":
				var item;
				for (var key in info){
						if (info.hasOwnProperty(key)){
								item = document.getElementById("view-" + key);
								if (type == "resources")
										item.children[0].innerHTML = info[key];	
								else
										item.children[0].innerHTML += " (" + info[key] + ")";
						}
				}
				break;
		case "cities":
		case "friends":
				var list = document.getElementById(type);
				var entry;
				for (var i = 0; i < info.length; i++){
						entry = document.createElement("li");
						entry.innerHTML = info[i];
						list.appendChild(entry);
				}
				break;
		default:
				break;
		}
};


var updateNavbar = function updateNavbar(data){
		var info = JSON.parse(data);
		var item;
		for (var key in info){
				if (info.hasOwnProperty(key)){
						item = document.getElementById("nav-" + key);
						item.innerHTML = " " + info[key];
				}
		}		
};

var getResources = function getResources(){
		$.get("/get_functions", {type: "get_resources", a: cityname}, function(data){
				//console.log(data);
				updateOverview(data, "resources");
				updateNavbar(data);
		});
};

var getMultipliers = function getMultipliers(){
		$.get("/get_functions", {type: "get_multipliers", a: cityname}, function(data){
				console.log(data);
				updateOverview(data, "multipliers");
		});
};

var getCityNames = function getCityNames(){
$.get("/get_functions", {type: "get_cityNames", a: username}, function(data){
updateOverview(data, "cities");
});
};

var getFriends = function getFriends(){
$.get("/get_functions", {type: "get_friends", a: username}, function(data){
updateOverview(data, "friends");
updateSelect(data, "friends");
});
};

var setupInfo = function setupInfo(){
getResources();
getMultipliers();
getCityNames();
getFriends();
};


var updateInfo = function updateInfo(){
$.get("/set_functions", {type: "update_resources", a: cityname}, function(){
getResources();
getMultipliers();
});
}


