Crafty.init(750, 300, document.getElementById('game'));
//use a div with id="game", first two numbers are pixel dimensions
Crafty.sprite(128, "sprite.png", {
  grass: [0,0,1,1],
  stone: [1,0,1,1]
});


var iso = Crafty.diamondIso.init(128,128,32,32);

var gTile = Crafty.e("2D, DOM, grass, Mouse")
.attr({xCord: 0, yCord: 0})
.areaMap([64,0],[128,32],[128,96],[64,128],[0,96],[0,32])
.bind("MouseOver", function(){
	this.sprite(0,1,1,1);//select sprite
}).bind("MouseOut", function(){
	this.sprite(0,0,1,1);//regular sprite
}).bind("Click", function(){
  //
});
iso.place(gTile,1,1,0);

/*
var gTile2 = Crafty.e("2D, DOM, stone, Mouse")
.attr({xCord: 0, yCord: 0})
.areaMap([64,0],[128,32],[128,96],[64,128],[0,96],[0,32])
.bind("MouseOver", function(){
	this.sprite(1,1,1,1);//select sprite
}).bind("MouseOut", function(){
	this.sprite(1,0,1,1);//regular sprite
}).bind("Click", function(){
  //
});
iso.place(gTile2,-1,-1,0);
*/