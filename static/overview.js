console.log("Here is the overview");

var username = document.getElementById("username").innerHTML;
var cityname;


/*Brings up the city overview screen
 */
var overview = function overview(){
    $('#overview-form').modal();
};


var updateOverview = function updatOverview(data, type){
		var info = JSON.parse(data);
		switch (type){
		case "resources":
				var item;
				for (var key in info){
						if (info.hasOwnProperty(key)){
								console.log(info[key]);
								item = document.getElementById("view-" + key);
								item.children[0].innerHTML = info[key];
						}
				}
				break;
				
		case "multipliers":
				var item;
				var text;
				for (var key in info){
						if (info.hasOwnProperty(key)){
								console.log(info[key]);
								item = document.getElementById("view-" + key);
								item.children[0].innerHTML += " (" + info[key] + ")";
						}
				}
				break;
				
		case "cities":
		case "friendslist":
				var list = document.getElementById(type);
				var entry;
				for (var i = 0; i < info.length; i++){
						entry = document.createElement("li");
						entry.innerHTML = info[i];
						friendslist.appendChild(entry);
				}
				break;
		default:
				break;
		}
		
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
		$.get("/get_functions", {type: "get_cityNames"}, function(data){
				console.log(data);
				updateOverview(data, "cities");
		});
		$.get("/get_functions", {type: "get_friends", a: username}, function(data){
				console.log(data);
				updateOverview(data, "friends");
		});
};
