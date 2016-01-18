console.log("Here is the chat");

var message = function message(){
		var chatbox = document.getElementById("chatbox");
		chatbox.style.display = "block";
};

/*Adds text input to chat body
 */
var addText = function addText(e){
		if (e.keyCode == 13){
				e.preventDefault();
				var input = document.getElementById("chat-input");
				console.log(input.value);
				if (input.value && input.value.trim()){	
						var body = document.getElementById("chatbody");
						body.innerHTML += input.value.trim() + "<br/>";
						input.value = "";
						body.scrollTop = body.scrollHeight - body.clientHeight;
				}
		}
};

/*Sets up event listeners
	Adds closing capability
*/
var chatSetup = function chatSetup(){
		$("#chat-close").click(function(e){
				$("#chatbox").css("display", "none");
		});
    
		var text = document.getElementById("chat-input");
		text.addEventListener("keydown", function(e){
				addText(e);
		})
};
