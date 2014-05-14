/*
 * Draw on a Canvas
 */ 

var context = document.getElementById('canvas').getContext('2d');
var board_width  = 1500
var board_height = 900

// Functions..........................................................

// Draw the background
function drawBoard() {
    context.save()
    context.clearRect(0, 0, context.canvas.width, context.canvas.height)
    context.strokeStyle = 'blue';
    context.fillStyle = '#ffffff';
    context.lineWidth = 0.5;
    context.fillRect(0, 0, context.canvas.width, context.canvas.height/2);
    context.fillStyle = 'black'
    context.fillRect(0,  context.canvas.height/3, context.canvas.width, context.canvas.height);

    grid_step = 50
    for (var i=0; i<context.canvas.height; i+=grid_step) {
        context.beginPath();
        context.moveTo(context.canvas.width,i)
        context.lineTo(0,i)
        context.stroke();
    }
    for (var j=0; j<context.canvas.width; j+=grid_step) {
        context.beginPath();
        context.moveTo(j, context.canvas.height)
        context.lineTo(j, 0)
        context.stroke();
    }
    context.restore();
}

// Apply a drop shadow
function dropShadow(){
    context.shadowColor = 'rgba(100, 100, 100, 0.5)';
    context.shadowOffsetX = 5;
    context.shadowOffsetY = 5;
    context.shadowBlur = 25;
}

// Draw one piece
function drawGraph(){
    dropShadow();
    context.strokeStyle = 'rgba(0,0,0,0.7)';
    context.fillStyle   = 'lightgreen'

    var samples = graph.length
    var height = 0
    for (var x=0; x<graph.length; x++) { if (height<graph[x]) { height=graph[x] } }

    var scale_width  = board_width/samples
    var scale_height = board_height/height

    context.beginPath();
    context.moveTo(0,board_height)
    for (var x=0; x<graph.length; x++){
        context.lineTo (x*scale_width, board_height-(scale_height*graph[x]) )
    }
    context.lineTo(x*scale_width, board_height);
    context.closePath()

    context.fill(); 
    context.stroke();
}

// Initialization.....................................................

drawBoard();
drawGraph()
