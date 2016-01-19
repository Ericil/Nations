Crafty.init(750, 350, document.getElementById('game'));
//use a div with id="game", first two numbers are pixel dimensions

Crafty.sprite(136,260, "sprites2.png", {
  tile: [0,0,1,1],
  building:[1,0,1,1]
});


var iso = Crafty.isometric.size(136);
for(var i = 5; i >= 0; i--) {
	for(var y = 0; y < 5; y++) {
		var gTile = Crafty.e("2D, DOM, tile, Mouse")
		.attr('z', (i+1 * y+1))//makes things look pretty
		.attr({xCord: i, yCord: y})
		.areaMap([68,0],[136,32],[136,48],[68,84],[0,48],[0,32])
		.bind("MouseOver", function(){
			//this.sprite(0,84,136,84);//select sprite
		}).bind("MouseOut", function(){
			//this.sprite(0,0,136,84);//regular sprite
		}).bind("Click", function(){
			generate(this);
		});
		iso.place(i,y,0, gTile);
	}
}

function generate(thingy){
	var tile = Crafty.e("2D, DOM, building, Mouse")
	.attr('z', (thingy.xCord+1 * thingy.yCord+1))
	.areaMap([21,52],[116,52],[118,232],[21,232]);
	/*
	.bind("MouseOver", function(){
		this.sprite(2,1,1,1);//select sprite
	}).bind("MouseOut", function(){
		this.sprite(2,0,1,1);//regular sprite
	})
	*/
	iso.place(thingy.xCord,thingy.yCord,5,tile);
}
