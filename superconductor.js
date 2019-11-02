// superconductor simulator in JavaScript with p5.js

// declaration of variables
var slider;

var xCanvas = 600
var yCanvas = 600

var xSize = 25;
var ySize = 25;
var N = xSize*ySize;

// Populating the arrays
// setup x and y arrays
var xArr = new Array(N);
var yArr = new Array(N);
// init x and y position of nth item
for (var i = 0; i < N; i++) {
  xArr[i] = i%xSize;
  yArr[i] = (i - i%xSize) / xSize;
}

// setup theta array with random values
var thetaArr = new Array(N);
for(var i = 0; i < N; i++) {
  var r = 2*Math.PI*Math.random();
  thetaArr[i] = r;
}

// setup array to hold relative energies of rotors
var colorArr = new Array(N);
colorArr.fill(0)

// init 2d array of nearest neighbours
nnArr = new Array(N);
for (var i = 0; i < N; i++) {
  // init array for 4 neighbours
  nnArr[i] = new Array(4);

  // determine n of right neighbour
  if (xArr[i] != xSize - 1) {
    nnArr[i][0] = i + 1;
  }
  else {
    nnArr[i][0] = i + 1 - xSize;
  }
  // determine n of up neighbour
  if (yArr[i] != ySize - 1) {
    nnArr[i][1] = i + xSize;
  }
  else {
    nnArr[i][1] = i + xSize - N;
  }
  // determine n of the left neighbour
  if (xArr[i] != 0) {
    nnArr[i][2] = i - 1;
  }
  else {
    nnArr[i][2] = i - 1 + xSize;
  }
  // determine th n of the right neighbour
  if (yArr[i] != 0) {
    nnArr[i][3] = i - xSize;
  }
  else {
    nnArr[i][3] = i - xSize + N;
  }
}


function mcStep(temp) {
  for (var i = 0; i < N; i++) {
    // make N random changes
    var s = Math.floor(Math.random()*N)
    var thetaOld = thetaArr[s];
    var thetaNew = thetaOld + (Math.random() - 0.5)

    // determine wether to accept change
    var eDiff = 0;
    for (var j = 0; j < 4; j++) {
      var nnSite = nnArr[s][j]
      var cosOld = Math.cos(thetaOld - thetaArr[nnSite])
      var cosNew = Math.cos(thetaNew - thetaArr[nnSite])
      eDiff = eDiff - (cosNew - cosOld)
    }

    // if criteria fulfilled accept change
    if((eDiff <= 0) || (Math.random() < Math.exp(-eDiff*5/temp))) {
      thetaArr[s] = thetaNew;
      colorArr[s] = Math.abs(eDiff) * 200 // update color for relative energy
    }
  }

  // draw all arrows and determine color
  for(var i =0; i < N; i++) {
    var colortest = colorArr[i]
    var xPos = xArr[i]*(xCanvas/xSize)*0.95 + xCanvas*0.05
    var yPos = yArr[i]*(yCanvas/ySize)*0.95 + yCanvas*0.05
    var length = Math.min(xCanvas, yCanvas)/min(xSize, ySize)/2.5
    var color = 'rgb(' + Math.floor(colorArr[i]) + ', 0, 0)'
    drawArrowCentered(xPos, yPos, length, thetaArr[i], color)
  }
}

function drawArrowCentered(x, y, length, theta, color) {
  // setup drawing environment
  push();
  stroke(color);
  strokeWeight(2);
  fill(color);

  // create line
  line(x-length*Math.cos(theta)/2, y-length*Math.sin(theta)/2, x+length*Math.cos(theta)/2, y+length*Math.sin(theta)/2);

  // create triangle
  let arrowSize = 4;
  translate(x, y);
  translate(length*Math.cos(theta)/2, length*Math.sin(theta)/2);
  rotate(theta);
  triangle(0, arrowSize / 2, 0, -arrowSize / 2, arrowSize, 0);

  // return original drawing status
  pop();
}

function setup() {
  createCanvas(xCanvas, yCanvas);
  slider = createSlider(0, 10, 5, 0.0001);
  slider.position(10, 6);
  textSize(20);
}

function draw() {
  // init
  background(100);
  fill(255);

  // get value
  var temp = slider.value();
  text("temp: " + temp + "K", 150, 17);
  mcStep(temp)
}