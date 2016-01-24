console.log("Here is the build");

var len;
var pos = 6;
var isBuilding = false;
var currentBuilding;
var proTypes = ["housed", "soldiers",
								"food", "iron", "wood", "gold", "happiness"];
var priceTypes = ["gold", "iron", "food", "wood"];


String.prototype.format = function(){
		var i = 0;
		var args = arguments;
		return this.replace(/{}/g, function(){
				return typeof args[i] != 'undefined' ? args[i++] : '';
		});
};


/*Make the bar appear or disappear
 */
var build = function build(){
		var bar = document.getElementById("build-bar");
		bar.classList.toggle("slidein");
		isBuilding = !isBuilding;
};


/*Disable a button by id
 */
var disable = function disable(name){
		var button = document.getElementById(name);
		button.classList.add("disabled");
		button.disabled = true;
};


/*Enable a button by id
 */
var enable = function enable(name){
		var button = document.getElementById(name);
		button.classList.remove("disabled");
		button.disabled = false;
};

/*Show the previous 6 choices
 */
var slidePrevious = function slidePrevious(){
		pos -= 6;
		if (pos <= 0){
				pos = 0;
				disable("build-previous");
				enable("build-next");
		}
		var buttonHeight = $("#build-previous").height();
		var elTop = $(".build-panel").eq(pos).offset().top + buttonHeight;
		$(".build-group").animate({scrollTop: elTop}, 500);
};

/*Show the next 6 choices
 */
var slideNext = function slideNext(){
		if (pos == 0) {pos += 6;}
		
		var buttonHeight = $("#build-previous").height();
		var elTop = $(".build-panel").eq(pos).offset().top + buttonHeight;
		$(".build-group").animate({scrollTop: elTop}, 500);
		
		if (pos + 6 >= len){
				disable("build-next");
				enable("build-previous");
		}
		else {pos += 6;}
};


/*Set multiple attributes for an element at once
 */
function setAttributes(element, attributes){
		Object.keys(attributes).forEach(function(name){
				element.setAttribute(name, attributes[name]);
		});
}

var buildOptions = function buildOptions(e){
		e.preventDefault();
		if (e.target.className == "build-panel"){
				currentBuilding = e.target.id;
				//console.log(currentBuilding);
				$(".build-panel").css("border-color", "white");
				e.target.style.borderColor = "red";
		}
};


/*Make a single panel, setting base stats and price in the popover
	building - object with building stats
	price - object with prices corresponding to building 
	destination - the DOM element to append to
*/
var makePanel = function makePanel(building, price, destination){
		var panel = document.createElement("div");
		
		var content = "<div>Production Values</div><ul>";
		var key, value;
		for (var i = 0; i < proTypes.length; i++){
				key = proTypes[i];
				if (building.hasOwnProperty(key)){
						value = building[key];
						content += "<li>{}: {}</li>".format(key, String(value));
				} 
		}
		content += "</ul>";
		content += "<div>Prices</div><ul>";
		for (var i = 0; i < priceTypes.length; i++){
				key = priceTypes[i];
				if (price.hasOwnProperty(key)){
						value = price[key];
						content += "<li>{}: {}</li>".format(key, String(value));
				} 
		}
		content += "</ul>";
		setAttributes(panel,{
				"class": "build-panel",
				"id": building["name"],
				"title": building["name"],
				"data-toggle": "popover",
				"data-placement": "left",
				"data-trigger": "hover",
				"data-html": "true",
				"data-container": "body",
				"data-content": content
		});
		destination.appendChild(panel);
};

/*Make all panels*/
var makePanels = function makePanels(data){
		var buildGroup = document.getElementsByClassName("build-group")[0];
		var info = JSON.parse(data);
		var buildData = info["buildings"];
		var buildPrice = info["prices"];
		len = buildData.length;
		
		var building;
		var price;
		for (var i = 0; i < len; i++){
				building = buildData[i];
				price = buildPrice[i];
				makePanel(building, price, buildGroup);
		}
		buildGroup.addEventListener("click", function(e){
				buildOptions(e);
		});
		$('[data-toggle="popover"]').popover();
};

/*Add click events listeners to buttons
 */
var setupBuild = function setupBuild(){
		var previous = document.getElementById("build-previous");
		previous.addEventListener("click", slidePrevious);
		previous.disabled = true;
    
		var next = document.getElementById("build-next");
		next.addEventListener("click", slideNext);

		$.get("/get_functions", {type: "base_building_stats"}, function(data){
				makePanels(data);
		});
};



