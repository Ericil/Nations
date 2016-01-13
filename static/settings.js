console.log("These are the settings");

/*Adds mouseover events to buttons
	Mouse over and out on options button to view options
	Mouse over options to view descriptions
*/
var hoverOptions = function hoverOptions(){
    $("#options").mouseover(function(){
				$(".btn-group-vertical button").each(function(i){
						if (i > 0)
								$(this).fadeIn();
				});
		});

		$("#sideoptions").mouseleave(function(){
				$(".btn-group-vertical button").each(function(i){
						if (i > 0)
								$(this).fadeOut();	
				});
		});
		
		$('[data-toggle="tooltip"]').tooltip();
};

/*Adds closing capability
	Adds text input to chat body
*/
var chatSetUp = function chatSetUp(){
		$("#chat-close").click(function(e){
				$("#chatbox").css("display", "none");
		});
		
		var text = document.getElementById("chat-input");
		text.addEventListener("keydown", function(e){
				if (e.keyCode == 13){
						e.preventDefault();
						if (this.value && this.value.trim()){	
								var body = document.getElementById("chat-body");
								body.innerHTML += this.value.trim()  + '<br>';
								this.value = "";
								body.scrollTop = body.scrollHeight - body.clientHeight;
						}
				}
		})
};

/*Adds click events to buttons
	Run a different function depending on the button
*/
var clickOptions = function clickOptions(){
		var options = document.getElementById("sideoptions");
		options.addEventListener("click", function(e){
				switch(e.target.id) {
				case "overview":
						showOverview();
						break;
				case "message":
						message();
						break;
				case "buildinfo":
						showBuildInfo();
						break;
				case "build":
						build();
				}
		});
};


/*Brings up the city overview screen
 */
var showOverview = function showOverview(){
		$('#overview-form').modal();
};


var message = function message(){
		var chatbox = document.getElementById("chatbox");
		chatbox.style.display = "block";
};


hoverOptions();
clickOptions();
chatSetUp();
