console.log("These are the settings");

var makeOptions = function makeOptions(){
    $("#options").mouseover(function(){
	$(".btn-group-vertical button").each(function(i){
	    console.log(this);
	    if (i > 0){
		$(this).fadeIn();
	    }
	});
    });

    $("#sideoptions").mouseleave(function(){
	$(".btn-group-vertical button").each(function(i){
	    console.log(this);
	    if (i > 0){
		$(this).fadeOut();
	    }
	});
    });
};

makeOptions();
