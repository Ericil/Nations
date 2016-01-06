console.log("These are the settings");




var logout = function logout(){
    $.get("/logout", function(data){
	console.log("Successfully logged out");
    });
};

var accountSettings = function accountSettings(){
    

};
