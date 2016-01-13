Crafty.init(750, 500, document.getElementById('game'));
//use a div with id="game", first two numbers are pixel dimensions
Crafty.sprite(128, "sprite.png", {
  grass: [0,0,1,1],
  stone: [1,0,1,1]
});


var iso = Crafty.isometric.size(128);

for(var i = 5; i >= 0; i--) {
	for(var y = 0; y < 5; y++) {
		var gTile = Crafty.e("2D, DOM, grass, Mouse")
		.attr('z',i+1 * y+1)//makes things look pretty
		.areaMap([64,0],[128,32],[128,96],[64,128],[0,96],[0,32])
		.bind("MouseOver", function(){
			this.sprite(0,1,1,1);//select sprite
		}).bind("MouseOut", function(){
			this.sprite(0,0,1,1);//regular sprite
		}).bind("Click", function(){
		  //place click function here
		});
		iso.place(i,y,0, gTile);
	}
}