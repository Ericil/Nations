console.log("Here is the build");

var len;
var pos = 6;
var isBuilding = false;

/*Make the bar appear or disappear
 */
var build = function build(){
		var bar = document.getElementById("build-bar");
		bar.classList.toggle("slidein");
		isBuilding = !isBuilding;
		console.log(building);
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

/*Add click events listeners to buttons
 */
var setupBuild = function setupBuild(){
		var previous = document.getElementById("build-previous");
		previous.addEventListener("click", slidePrevious);
		previous.disabled = true;
    
		var next = document.getElementById("build-next");
		next.addEventListener("click", slideNext);

		var buildGroup = document.getElementsByClassName("build-group")[0];
		len = 12;
		for (var i = 0; i < len; i++){
				var panel = document.createElement("div");
				setAttributes(panel,{
						"class": "build-panel",
						"title": "House",
						"data-toggle": "popover",
						"data-placement": "left",
						"data-trigger": "hover",
						"data-content": "" + i
				});
				buildGroup.appendChild(panel);
		}
		$('[data-toggle="popover"]').popover();
    
};



