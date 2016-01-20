console.log("Here is the build");

var pos = 0;

/*Make the bar appear or disappear
 */
var build = function build(){
		$("#build-bar").animate({
				width: 'toggle'
		});
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
		var panels = document.getElementsByClassName("build-panel");
		for (var i = pos; i >= 0; i--){
				panels[i].classList.remove("next");
				panels[i].children[0].classList.remove("header-next");
		}
		
		if (pos <= 6){
				pos = 0;
				disable("build-previous");
				enable("build-next");
		}
};

/*Show the next 6 choices
 */
var slideNext = function slideNext(){
		pos += 6;
		var panels = document.getElementsByClassName("build-panel");
		for (var i = 0; i < panels.length && i < pos; i++){
				panels[i].classList.add("next");
				panels[i].children[0].classList.add("header-next");
		}
		
		if (pos + 6 >= panels.length){
				pos = panels.length;
				disable("build-next");
				enable("build-previous");
		}
};

/*Add click events listeners to buttons
 */
var buildSetup = function buildSetup(){
		var previous = document.getElementById("build-previous");
		previous.addEventListener("click", slidePrevious);
		previous.disabled = true;
		
		var next = document.getElementById("build-next");
		next.addEventListener("click", slideNext);
}



