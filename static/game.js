console.log("Hello");

var width;
var height;

var calculateSize = function calculateSize(){
    var navHeight = document.getElementsByTagName("nav")[0].clientHeight;
    width = window.innerWidth;
    height = window.innerHeight - navHeight;
};

calculateSize();

Crafty.init(width, height, document.getElementById('game'));
//use a div with id="game", first two numbers are pixel dimensions
Crafty.sprite(136,260, "http://i.imgur.com/AmfVJyH.png", {
    tile: [0,0,1,1],
    building:[1,0,1,1]
});
var iso = Crafty.isometric.size(136);
for(var i = 8; i >= 0; i--) {
    for(var y = 0; y < 16; y++) {
	var gTile = Crafty.e("2D, DOM, tile, Mouse")
	    .attr('z', (i+2 * y+1))//makes things look pretty
	    .attr({xCord: i+1, yCord: y+2})
	    .areaMap([68,0],[136,32],[136,48],[68,84],[0,48],[0,32])
	    .bind("MouseOver", function(){
		this.sprite(0,1,1,1);//select sprite
	    }).bind("MouseOut", function(){
		this.sprite(0,0,1,1);//regular sprite
	    }).bind("Click", function(){
		generate(this);
	    });
	iso.place(i+1,y+2,0, gTile);
    }
}
function generate(thingy){
    var tile = Crafty.e("2D, DOM, building, Mouse")
	.attr('z', (thingy.xCord+2 * thingy.yCord+1))
	.areaMap([21,52],[116,52],[118,232],[21,232])
	.bind("MouseOver", function(){
	  this.sprite(1,1,1,1);//select sprite
	}).bind("MouseOut", function(){
	    this.sprite(1,0,1,1);//regular sprite
	});
    iso.place(thingy.xCord,thingy.yCord,5,tile);
}
