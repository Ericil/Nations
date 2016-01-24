console.log("Here is the chat");

var selectInterval;
var chatInterval;

var message = function message(){
		var select = document.getElementById("chat-select");
		select.style.display = "block";
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

var changeToChat = function changeToChat(name){
		document.getElementById("chat-select").style.display = "none";
		document.getElementById("chatbox").style.display = "block";
		document.getElementById("chat-with").innerHTML = name;

		//then update the chat history and set interval to update chat
};

var changeToSelect = function changeToSelect(){
		document.getElementById("chat-select").style.display = "block";
		document.getElementById("chatbox").style.display = "none";

		//update the chat list (players and badges) and clear the interval
};


/*Sets up event listeners
	Adds closing capability
*/
var setupChat = function setupChat(){
		var chatSelect = document.getElementById("chat-select");
		var chatBox = document.getElementById("chatbox");

		/*------------------- Chat Events ---------------------------*/
		
		chatBox.addEventListener("click", function(e){
				e.preventDefault();
				switch(e.target.id){
				case "chat-with":
						changeToSelect();
						break;
				case "chat-close":
						chatBox.style.display = "none";
						//clear interval
						break;
				default:
						break;
				}
		});
		
		var text = document.getElementById("chat-input");
		text.addEventListener("keydown", function(e){
				addText(e);
		})
		
		/*------------------- Select Events ---------------------------*/
		
		chatSelect.children[0].addEventListener("click", function(e){
				e.preventDefault();
				switch(e.target.tagName){
				case "BUTTON":
						chatSelect.style.display = "none";
						break;
				case "A":
						changeToChat(e.target.innerHTML);
						break;
				default:
						break;
				}
		});
};

/*Pulls chat out of database and displays it on an interval
 */
var updateChat = function updateChat(){
		var body = document.getElementById("chatbody");
		$.get("/functions", {type: "friendslist"}, function(data){
				console.log(data);
		});
};


var updateSelect = function updateSelect(data, type){
		var info = JSON.parse(data);
		var list;
		
		if (type == "friends")
				list = document.getElementById("kinda-friends");
		if (type == "others")
				list = document.getElementById("not-friends");
		
		var item;
		for (var i = 0; i < info.length; i++){
				item = document.createElement("a");
				item.className = "list-group-item select-item";
				item.href = "#";
				item.innerHTML = info[i];
				list.appendChild(item);
		}	
};


