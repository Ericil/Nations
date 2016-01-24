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
								//console.log(info[key]);
								item = document.getElementById("view-" + key);
								if (type == "resources")
										item.children[0].innerHTML = info[key];	
								else
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
		var info = JSON.parse(data);
		var item;
		for (var key in info){
				if (info.hasOwnProperty(key)){
						//console.log(info[key]);
						item = document.getElementById("nav-" + key);
						item.innerHTML = info[key];
				}
		}
		
};



var updateInfo = function updateInfo(){
		$.get("/get_functions", {type: "get_resources", a: cityname}, function(data){
				console.log(data);
				updateOverview(data, "resources");
				updateNavbar(data);
		});
		$.get("/get_functions", {type: "get_multipliers", a: cityname}, function(data){
				console.log(data);
				updateOverview(data, "multipliers");
		});
		$.get("/get_functions", {type: "get_cityNames", a: username}, function(data){
				console.log(data);
				updateOverview(data, "cities");
		});
		$.get("/get_functions", {type: "get_friends", a: username}, function(data){
				console.log(data);
				updateOverview(data, "friends");
		});
};
