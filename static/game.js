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
Crafty.sprite(136,260, "http://i.imgur.com/m0zz0uW.png", {
    tile: [0,0,1,1],
    tileS: [0,1,1,1],
    cityHall:[1,0,1,1],
    cityHallS:[1,1,1,1],
    mine:[2,0,1,1],
    mineS:[2,1,1,1],
    house:[3,0,1,1],
    houseS:[3,1,1,1],
    woodmill:[4,0,1,1], 
    woodmillS:[4,1,1,1], 
    mall:[5,0,1,1], 
    mallS:[5,1,1,1], 
    farm:[6,0,1,1], 
    farmS:[6,1,1,1], 
    hospital:[7,0,1,1], 
    hospitalS:[7,1,1,1], 
    park:[8,0,1,1], 
    parkS:[8,1,1,1], 
    barracks:[9,0,1,1], 
    barracksS:[9,1,1,1]
});
var iso = Crafty.isometric.size(136);
//var asdf = document.getElementById("potato");

/****Components****/
Crafty.c("tileC", {
    init: function(){
        this.areaMap([68,0],[136,32],[136,48],[68,84],[0,48],[0,32])
						.addComponent("tile")
						.bind("MouseOver", function(){
								this.removeComponent("tile");
								this.addComponent("tileS");//select sprite
						}).bind("MouseOut", function(){
								this.removeComponent("tileS");
								this.addComponent("tile");//regular sprite
						});
    }
});
Crafty.c("cityhallC", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])
						.addComponent("cityHall")
						.bind("MouseOver", function(){
								this.removeComponent("cityHall");
								this.addComponent("cityHallS");//select sprite
						}).bind("MouseOut", function(){
								this.removeComponent("cityHallS");
								this.addComponent("cityHall");//regular sprite
						});
    }
});
Crafty.c("mineC", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .addComponent("mine")
        .bind("MouseOver", function(){
		    this.removeComponent("mine");
		    this.addComponent("mineS");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("mineS");
		    this.addComponent("mine");//regular sprite
	    });
    }
});
Crafty.c("houseC", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .addComponent("house")
        .bind("MouseOver", function(){
		    this.removeComponent("house");
		    this.addComponent("houseS");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("houseS");
		    this.addComponent("house");//regular sprite
	    });
    }
});
Crafty.c("woodmillC", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .addComponent("woodmill")
        .bind("MouseOver", function(){
		    this.removeComponent("woodmill");
		    this.addComponent("woodmillS");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("woodmillS");
		    this.addComponent("woodmill");//regular sprite
	    });
    }
});
Crafty.c("mallC", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .addComponent("mall")
        .bind("MouseOver", function(){
		    this.removeComponent("mall");
		    this.addComponent("mallS");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("mallS");
		    this.addComponent("mall");//regular sprite
	    });
    }
});
Crafty.c("farmC", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .addComponent("farm")
        .bind("MouseOver", function(){
		    this.removeComponent("farm");
		    this.addComponent("farmS");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("farmS");
		    this.addComponent("farm");//regular sprite
	    });
    }
});
Crafty.c("hospitalC", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .addComponent("hospital")
        .bind("MouseOver", function(){
		    this.removeComponent("hospital");
		    this.addComponent("hospitalS");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("hospitalS");
		    this.addComponent("hospital");//regular sprite
	    });
    }
});
Crafty.c("parkC", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .addComponent("park")
        .bind("MouseOver", function(){
		    this.removeComponent("park");
		    this.addComponent("parkS");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("parkS");
		    this.addComponent("park");//regular sprite
	    });
    }
});
Crafty.c("barracksC", {
    init: function(){
        this.areaMap([21,52],[116,52],[118,232],[21,232])//change area map
        .addComponent("barracks")
        .bind("MouseOver", function(){
		    this.removeComponent("barracks");
		    this.addComponent("barracksS");//select sprite
	    }).bind("MouseOut", function(){
		    this.removeComponent("barracksS");
		    this.addComponent("barracks");//regular sprite
	    });
    }
});



/****Scenes****/
Crafty.defineScene("smallMap", function(){
    for(var i = 8; i >= 0; i--) {
        for(var y = 0; y < 16; y++) {
    	var gTile = Crafty.e("2D, DOM, Mouse, tileC")
    	    .attr('z', (i+2 * y+1))//makes things look pretty
    	    .attr({xCord: i, yCord: y})
    	    .bind("Click", function(){
							addBuilding(this);
    			});
    				iso.place(i+2,y+1,0, gTile);
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
function change(name){
    Crafty.enterScene(name); //either bigMap or smallMap
}

/****Extra Functions****/
function generate(thingy){
    var tile = Crafty.e("2D, DOM, cityHall, Mouse, cityHallC")
	.attr('z', (thingy.xCord+2 * thingy.yCord+1))
    .bind("Click", function(){
        //place click function here
    });
    iso.place(thingy.xCord,thingy.yCord,5,tile);
}

function generate1(floor, building, lvl, prc){
		var final = Crafty.e("2D, DOM, Mouse")
				.attr('z', (floor.xCord+2 * floor.yCord+1))//Z coordinate perspective
				.attr({xCord: floor.xCord, yCord: floor.yCord})
				.attr({level: lvl, food: prc["food"],
							 gold: prc["gold"], wood: prc["wood"],
							 iron: prc["iron"]})//Level and price //Can be retreived with this.attr("level")
				.bind("Click", function(){
						console.log("hello");
				});
		final.addComponent("" + building + "C");//Check out the components section to find the name
		iso.place(floor.xCord + 2, floor.yCord + 1, 5, final);//place the building
}

function generate2(x, y, building, lvl, prc){
		var final = Crafty.e("2D, DOM, Mouse")
				.attr('z', (x+2 * y+1))//Z coordinate perspective
				.attr({xCord: x, yCord: y})
				.attr({level: lvl, food: prc["food"],
							 gold: prc["gold"], wood: prc["wood"],
							 iron: prc["iron"]})//Level and price //Can be retreived with this.attr("level")
				.bind("Click", function(){
						console.log("hello");
				});
		final.addComponent("" + building + "C");//Check out the components section to find the name
		iso.place(x + 2, y + 1, 5, final);//place the building
}


function addBuilding(floor){
		if (isBuilding && typeof currentBuilding != 'undefined'){
				$.get("/set_functions", {
						type: "add_building",
						a: cityname, b: floor.xCord,
						c: floor.yCord, d: currentBuilding},
							function(data){
									if (data)
											getBuilding(floor);
									else
											$(".alert").show();
							});
		}
}

function getBuilding(floor){
		$.get("/get_functions", {
				type: "get_specific_building_stat",
				a: cityname, b: floor.xCord,
				c: floor.yCord},
					function(data){
							makeBuilding(JSON.parse(data));
					});
}
