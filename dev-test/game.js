Crafty.init(750, 350, document.getElementById('game'));
//use a div with id="game", first two numbers are pixel dimensions
Crafty.sprite(128, "sprite.png", {
  grass: [0,0,1,1],
  stone: [1,0,1,1],
  build: [2,0,1,1]
});


var iso = Crafty.isometric.size(128);
for(var i = 5; i >= 0; i--) {
	for(var y = 0; y < 5; y++) {
		var gTile = Crafty.e("2D, DOM, grass, Mouse")
		.attr('z', (i+1 * y+1))//makes things look pretty
		.attr({xCord: i, yCord: y})
		.areaMap([64,0],[128,32],[128,96],[64,128],[0,96],[0,32])
		.bind("MouseOver", function(){
			this.sprite(0,1,1,1);//select sprite
			bugtest(this);
		}).bind("MouseOut", function(){
			this.sprite(0,0,1,1);//regular sprite
			document.getElementById("potato").innerHTML = "shhhh"
		}).bind("Click", function(){
			generate(this);
		});
		iso.place(i,y,0, gTile);
	}
}

function generate(thingy){
	var tile = Crafty.e("2D, DOM, build, Mouse")
	.attr('z', (thingy.xCord+1 * thingy.yCord+1))
	.areaMap([64,0],[128,32],[128,96],[64,128],[0,96],[0,32])
	.bind("MouseOver", function(){
		this.sprite(2,1,1,1);//select sprite
		bugtest(this);
	}).bind("MouseOut", function(){
		this.sprite(2,0,1,1);//regular sprite
		document.getElementById("potato").innerHTML = "shhhh"
	}).bind("Click", function(){
		  bugtest(this);
	});
	var zed = thingy.xCord+1 * thingy.yCord+1;
	iso.place(thingy.xCord,thingy.yCord,2,tile);
}

function bugtest(thingy){
	var l = document.getElementById("potato");
	l.innerHTML = " " + thingy.xCord + " "
	+ thingy.yCord + " " + thingy.z;
}
