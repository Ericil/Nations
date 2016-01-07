console.log("These are the settings");

var settings = function settings(){
		var button = document.getElementById("settings");
		button.addEventListener("click", function(e){
				console.log(this);
				this.children[1].classList.toggle("show");
		});
		
		window.addEventListener("click", function(e){
				if (!e.target.matches('.dropbtn')){
						var options = document.getElementsByClassName("dropdown-content");
						for (var i = 0; i < options.length; i++){
								if (options[i].classList.contains('show'))
										options[i].classList.remove('show');
						}
				}
		});
};



settings();
