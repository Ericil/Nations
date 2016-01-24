//dev-test
console.log("Hello");

Crafty.init(750,350, document.getElementById('game'));
//use a div with id="game", first two numbers are pixel dimensions
Crafty.sprite(136,260, "http://i.imgur.com/rCTBOJK.png", {
    tile: [0,0,1,1],
    tileS: [0,1,1,1],
    building1:[1,0,1,1],
    building1S:[1,1,1,1],
    building2:[2,0,1,1],
    building2S:[2,1,1,1],
    building3:[3,0,1,1],
    building3S:[3,1,1,1],
    building4:[4,0,1,1], 
    building4S:[4,1,1,1] 
});
var iso = Crafty.isometric.size(136);
//var asdf = document.getElementById("potato");

/****Components****/
Crafty.c("tileC", {
    init: function(){
        this.areaMap([68,0],[136,32],[136,48],[68,84],[0,48],[0,32])
        .bind("MouseOver", function(){
		    this.removeComponent("tile");
		    this.addComponent("tileS");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("tileS");
		    this.addComponent("tile");//regular sprite
	    });
    }
});
Crafty.c("building1C", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])
        .bind("MouseOver", function(){
		    this.removeComponent("building1");
		    this.addComponent("building1S");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("building1S");
		    this.addComponent("building1");//regular sprite
	    });
    }
});
Crafty.c("building2C", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .bind("MouseOver", function(){
		    this.removeComponent("building2");
		    this.addComponent("building2S");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("building2S");
		    this.addComponent("building2");//regular sprite
	    });
    }
});
Crafty.c("building3C", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .bind("MouseOver", function(){
		    this.removeComponent("building3");
		    this.addComponent("building3S");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("building3S");
		    this.addComponent("building3");//regular sprite
	    });
    }
});
Crafty.c("building4C", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .bind("MouseOver", function(){
		    this.removeComponent("building4");
		    this.addComponent("building4S");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("building4S");
		    this.addComponent("building4");//regular sprite
	    });
    }
});



/****Scenes****/
Crafty.defineScene("smallMap", function(){
    for(var i = 8; i >= 0; i--) {
        for(var y = 0; y < 16; y++) {
    	var gTile = Crafty.e("2D, DOM, tile, Mouse, tileC")
    	    .attr('z', (i+2 * y+1))//makes things look pretty
    	    .attr({xCord: i, yCord: y})
    	    .bind("Click", function(){
        		generate(this);
    	    });
    	iso.place(i,y,0, gTile);
        }
    }
});
Crafty.defineScene("smallMap2", function(){
    for(var i = 8; i >= 0; i--) {
        for(var y = 0; y < 16; y++) {
    	var gTile = Crafty.e("2D, DOM, tile, Mouse, tileC")
    	    .attr('z', (i+2 * y+1))//makes things look pretty
    	    .attr({xCord: i, yCord: y})
    	    .bind("Click", function(){
        		generate(this);
    	    });
    	iso.place(i,y,0, gTile);
        }
    }
});
Crafty.defineScene("bigMap", function(){
    for(var i = 4; i >= 0; i--) {
        for(var y = 0; y < 4; y++) {
    	var gTile = Crafty.e("2D, DOM, tile, Mouse, tileC")
    	    .attr('z', (i+2 * y+1))//makes things look pretty
    	    .attr({xCord: i, yCord: y});
    	iso.place(i,y,0, gTile);
        }
    }
});

Crafty.enterScene("smallMap");//Starts off in the small map
function change(){
    Crafty.enterScene("bigMap");
}

/****Extra Functions****/
function generate(thingy){
    var tile = Crafty.e("2D, DOM, building1, Mouse, building1C")
	.attr('z', (thingy.xCord+2 * thingy.yCord+1))
    .bind("Click", function(){
        //place click function here
    });
    iso.place(thingy.xCord,thingy.yCord,5,tile);
}

function generate1(floor, building, lvl){
    var final = Crafty.e("2D, DOM, Mouse")
    .attr('z', (floor.xCord + 2 * floor.yCord+1))//Z coordinate perspective
    .attr({level:lvl})//Level
    .bind("Click", function(){
        //place click function here
    });
    final.addComponent(building);//Check out the components section to find the name
    iso.place(floor.xCord, floor.yCord, 5, final);//place the building
}


