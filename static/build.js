console.log("Here is the build");

var pos = 0;


var build = function build(){
		$("#build-bar").animate({
				width: 'toggle'
		});
};

var disable = function disable(name){
		var button = document.getElementById(name);
		button.classList.add("disabled");
		button.disabled = true;
};

var enable = function enable(name){
		var button = document.getElementById(name);
		button.classList.remove("disabled");
		button.disabled = false;
};


var slidePrevious = function slidePrevious(){
		pos -= 6;
		var panels = document.getElementsByClassName("build-panel");
		for (var i = pos; i >= 0; i--){
				panels[i].classList.remove("next");
		}
		
		if (pos <= 6){
				pos = 0;
				disable("build-previous");
				enable("build-next");
		}
};


var slideNext = function slideNext(){
		pos += 6;
		var panels = document.getElementsByClassName("build-panel");
		for (var i = 0; i < panels.length && i < pos; i++){
				panels[i].classList.add("next");
		}
		
		if (pos + 6 >= panels.length){
				pos = panels.length;
				disable("build-next");
				enable("build-previous");
		}
};


var buildSetup = function buildSetup(){
		var previous = document.getElementById("build-previous");
		previous.addEventListener("click", slidePrevious);
		previous.disabled = true;
		
		var next = document.getElementById("build-next");
		next.addEventListener("click", slideNext);
}



