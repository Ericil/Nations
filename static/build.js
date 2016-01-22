console.log("Here is the build");

var len = 14;
var pos = 0;

/*Make the bar appear or disappear
 */
var build = function build(){
		var bar = document.getElementById("build-bar");
		bar.classList.toggle("slidein");
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
		var button = document.getElementById("build-previous");
		
		if (pos < 0) {
				pos = 0;
				disable("build-previous");
				enable("build-next");
		}
		var elTop = $(".build-panel").eq(pos).position().top + button.style.height;
		$(".build-group").animate({scrollTop: elTop}, 500);
};

/*Show the next 6 choices
 */
var slideNext = function slideNext(){
		pos += 6;
		var diff = len - pos;
		var button = document.getElementById("build-previous");
		
		if (diff < 6) {
				pos = pos - (6 - diff);
				disable("build-next");
				enable("build-previous");
		}
		var elTop = $(".build-panel").eq(2).offset().top + button.style.height;
		$(".build-group").animate({scrollTop: elTop}, 500);
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
		for (var i = 0; i < 14; i++){
				var panel = document.createElement("div");
				setAttributes(panel,{
						"class": "build-panel",
						"title": "House",
						"data-toggle": "popover",
						"data-placement": "left",
						"data-trigger": "hover",
						"data-content": "$100,000"
				});
				buildGroup.appendChild(panel);
		}
		$('[data-toggle="popover"]').popover();
		
};



