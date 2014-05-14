angular.module('pipescan', ['ui.bootstrap']);

//-----------------------------------------------------------------------------
// Draw on a Canvas

var path = 'None'
var board_width  = 3000;
var board_height = 300;
var grid_step  = 15;
var view_width  = board_width;
var view_height = board_height;
var draw_step = 1;
var max_height = 100;
var vertical_offset = 0;
 
colors = [ '#ff0000', '#00ff00',  '#00ffff', '#ffff00' ];


// Select the correct canvas
function getContext(canvas) {
    return document.getElementById(canvas).getContext('2d');
}


// Draw the background
function drawGrid(context) {
    context.save();
    context.clearRect(0, 0, view_width, view_height);
    context.fillStyle = 'black';
    context.fillRect(0, view_height, view_width, view_height);
    context.strokeStyle = 'aqua';
    context.lineWidth = 0.5;

    for (var i=0; i<view_height; i+=grid_step) {
        context.beginPath();
        context.moveTo(view_width,i);
        context.lineTo(0,i);
        context.stroke();
    }
    context.restore();
}

// Draw one line on the graph
function drawSamples(context, data, channel, draw_step){
    context.beginPath();
    context.lineWidth = 1;
    context.strokeStyle =  colors[channel%4];
    context.moveTo(0, view_height);
    
    var scale_width  = draw_step;
    var scale_height = (view_height/max_height);
    for (var x=0; x<data.length; x++){
        var y =  data[x][channel];
        y =  view_height-(scale_height*y) + vertical_offset;
        context.lineTo (x*scale_width, y);
    }

    context.stroke();
    context.closePath();
}

// Draw one cell
function drawRect(context,x,y,value) {
    var cell_width   = 10;
    var cell_height  = 10;
    context.fillStyle = color_of(value);
    context.fillRect(x*cell_width, y*cell_height, cell_width, cell_height);
    context.stroke();
}

// Color of the square cell
function color_of(color) {
    if (color=="r") { return "red" };
    if (color=="y") { return "yellow" };
    if (color=="b") { return "blue" };
    if (color=="g") { return "green" };
    if (color=="x") { return "black" };
    return 'Unknown';
}


//-----------------------------------------------------------------------------
// Wall sensor drawing

// Draw the wall shift indicator
function drawWallShift(x) {
    var context = getContext('canvas-wall');
    var cell_width   = 10;
    var cell_height  = 10;
    context.save();
    context.fillStyle = 'black';
    context.fillRect(cell_width, 0, cell_width, 30*cell_height)
    context.fillStyle = 'aqua';
    context.fillRect(cell_width, (15-x)*cell_height, cell_width, cell_height);
    context.stroke();
    context.restore();
}

// Draw walls
function drawWallView(data){
    var context = getContext('canvas-wall');
    drawGrid(context);
    for (var channel=0; channel<4; channel++){
        var draw_step = 2;
        drawSamples(context,data, channel, draw_step)
    }
}

//-----------------------------------------------------------------------------
// Flaw sensor drawing

// Draw flaws
function drawFlawView(data){
    var context = getContext('canvas-flaw');
    drawGrid(context);
    for (var channel=4; channel<12; channel++){
        drawSamples(context, data, channel, 2)
    }
}

//-----------------------------------------------------------------------------
// Wall grade drawing

// Draw Wall Grades
function drawWallGraph(gradeGraph){
    var context = document.getElementById('canvas-wall-summary').getContext('2d');
    for (var x=0; x<gradeGraph.length; x++) {
        for (var y=0; y<4; y++) {
            z = 'x';
            z = gradeGraph[x].charAt(y)
            drawRect(context, x, y, z); 
        }
    }
}

//-----------------------------------------------------------------------------
// Flaw grade drawing

// Draw Flaw Grades
function drawFlawGraph(gradeGraph){
    var context = document.getElementById('canvas-flaw-summary').getContext('2d');
    for (var x=0; x<gradeGraph.length; x++) {
        for (var y=4; y<12; y++) {
            z = 'x';
            z = gradeGraph[x].charAt(y)
            drawRect(context, x, y-4, z); 
        }
    }
}

//-----------------------------------------------------------------------------
// OScope drawing

// Draw one line on the graph
function drawCandles(data,channel){
    context.beginPath();
    context.lineWidth = 1;
    context.strokeStyle =  colors[channel%4];
    num_samples = data.length;
    for (var x=0; x<num_samples; x++){
        var offset = psuedo_jitter*(channel);
        var y1 = data[x][channel][0] + offset;
        var y2 = data[x][channel][1] + offset;
        context.moveTo (x, view_height-(scale_height*y1));
        context.lineTo (x, view_height-(scale_height*y2))
    }
    context.stroke();
    context.closePath();
}

// Oscope 
function drawOscopeView(data){
    var context = getContext('canvas-oscope');
    drawGrid(context);
    for (var channel=0; channel<12; channel++){
        drawSamples(context, data, channel, 2)
    }
}

//-----------------------------------------------------------------------------
// Drawing views

// Convert from text to int table
function csv_to_table(data) {
    var table = []
    var rows = data.slice(0,-1).split('\n')
    for (var r in rows) {
        console.log(rows[r])
        columns = rows[r].split(',')
        if (columns.length>1) {
            var row = []
            for (var c in columns) {
                row.push(parseInt(columns[c]))
            }
            table.push(row);
        }
    }
    return table;
} 

// Draw grades
function drawGradeGraphs(grade) {
    gradeGraph = grade.split('\n');
    drawFlawGraph(gradeGraph);
    drawWallGraph(gradeGraph);
}


// Draw the views
function drawSensorGraphs(data) {
    dataGraph = csv_to_table(data);
    drawFlawView(dataGraph);
    drawWallView(dataGraph);
}



// Fetch and draw the data
function getScanData(http, ok) {
    try {
        http.get('/sensors').success(function(data,status,headers,config) {
            drawSensorGraphs(data)
        });
        http.get('/grade').success(function(data,status,headers,config) {
            drawGradeGraphs(data)
        });
    }
    catch(err) {
        ok = 'Error'
    };
}

//-----------------------------------------------------------------------------
// Wall shift controller

function ChannelsViewCtrl($scope,$http) {

    $scope.amount = 0
    $scope.dataSensors = "No data yet";
    $scope.dataGrade   = "No data yet";

    $scope.get_data_path = function(){
        $scope.scanpath    = $scope.url
        getScanData($http, $scope.url)
    }

    $scope.wall_find = function() {
        source = '/trigger/cal-wall-find'
        $http.get(source).success(function(data,status,headers,config) {
            location='http://localhost:8080/open-scan';
        })
    }

    $scope.wall_save = function() {
        source = '/trigger/cal-wall-save'
        $http.get(source).success(function(data,status,headers,config) {
            alert('system calibration updated')
        })
    }

    $scope.url ='Ready'

    $scope.get_data_path()
}

//-----------------------------------------------------------------------------
// Calibrate controller

function CalibrateCtrl($scope,$http) {

    var x = 0;
    $scope.dataSensors = "No data yet";
    $scope.dataGrade   = "No data yet";
    $scope.status      = 'Press to start scanning';
    $scope.showGood    = true;
    $scope.showBad     = false;
    $scope.goodDone    = false;

    // Draw the data from the server
    var drawGraphView = function() {
        $scope.refreshData();
        if (x>10) {
            clearInterval($scope.autorefresh);
            $scope.recordStop();
        }
        x += 1;
    }

    // Refresh the data in the view
    $scope.refreshData = function () {
        getScanData($http, $scope.status)
    }

    // Begin scanning
    $scope.recordGoodStart = function () {
        source = '/trigger/record-start';
        $http.get(source).success(function(data,status,headers,config) {
            $scope.status      = 'scanning good ...';
            $scope.showGood    = false;
            $scope.autorefresh = setInterval(drawGraphView, 500);        
        });
    };

    // Begin scanning
    $scope.recordBadStart = function () {
        $scope.goodDone    = true
        x = 0
        source = '/trigger/record-start';
        $http.get(source).success(function(data,status,headers,config) {
            $scope.status      = 'scanning good ...';
            $scope.showBad     = false;
            $scope.autorefresh = setInterval(drawGraphView, 500);        
        });
    };

    // Save data from good scan
    $scope.recordGoodStop = function () {
        source = '/trigger/record-good-done'
        $http.get(source).success(function(data,status,headers,config) {
            $scope.showBad     = true
            //alert('record-good-done')
        })
    }

    // Save data from bad scan
    $scope.recordBadStop = function () {
        source = '/trigger/record-bad-done'
        $http.get(source).success(function(data,status,headers,config) {
            //alert('record-good-done')
            location='http://localhost:8080/open-scan'
        })
    }

    // Finish the current scanning operation
    $scope.recordStop = function () {
        $scope.status='stopping...';
        clearInterval($scope.autorefresh);

        if ($scope.goodDone) {
            $scope.recordBadStop()
        }
        else {
            $scope.recordGoodStop()
        }
    }
}


//-----------------------------------------------------------------------------
// Recording controller

var pipe = 'PIPE'

function RecordCtrl($scope,$http) {

    var x = 0;
    $scope.dataSensors = "No data yet";
    $scope.dataGrade   = "No data yet";
    $scope.status      = 'Press to start scanning';
    $scope.showStart   = true;
    $scope.showStop    = false;
    $scope.showResume  = false;
    $scope.showPause   = false;
    $scope.pipe        = pipe;

    function post_to_url(path, params, method) {
        method = method || "post"; // Set method to post by default if not specified.

        // The rest of this code assumes you are not using a library.
        // It can be made less wordy if you use one.
        var form = document.createElement("form");
        form.setAttribute("method", method);
        form.setAttribute("action", path);
        
        for(var key in params) {
            if(params.hasOwnProperty(key)) {
                var hiddenField = document.createElement("input");
                hiddenField.setAttribute("type", "hidden");
                hiddenField.setAttribute("name", key);
                hiddenField.setAttribute("value", params[key]);
                form.appendChild(hiddenField);
            }
        }
        document.body.appendChild(form);
        form.submit();
    }


    var setPipe = function(p){
        $http.post(source).success(function(data,status,headers,config) {
            $scope.pipe        = p
    }

    // Draw the data from the server
    var drawGraphView = function() {
        $scope.refreshData();
        if ($scope.dataGrade != "No data yet") {
        }
        if ($scope.dataSensors != "No data yet") {
        }
        if (x>40) {
            clearInterval($scope.autorefresh);
            $scope.recordStop();
        }
        x += 1;
    }

    // Refresh the data in the view
    $scope.refreshData = function () {
        getScanData($http, $scope.status)
    }

    // Begin scanning
    $scope.recordStart = function () {
        source = '/trigger/record-start';
        $http.get(source).success(function(data,status,headers,config) {
            $scope.status      = 'scanning...';
            $scope.showStart   = false;
            $scope.showStop    = true;
            $scope.showPause   = true;
            $scope.autorefresh = setInterval(drawGraphView, 500);        
        });
    };

    // Pause after scan is started
    $scope.recordPause = function () {
        $scope.showResume  = true;
        $scope.showPause   = false;
        clearInterval($scope.autorefresh);
        source = '/trigger/record-pause';
        $http.get(source).success(function(data,status,headers,config) {
        });
    }

    // Resume scanning after pause
    $scope.recordResume = function () {
        $scope.showResume  = false;
        $scope.showPause   = true;
        $scope.autorefresh = setInterval(drawGraphView, 500);        
        source = '/trigger/record-resume';
        $http.get(source).success(function(data,status,headers,config) {
        });
    }

    // Finish the current scanning operation
    $scope.recordStop = function () {
        $scope.showResume  = false;
        $scope.showPause   = false;
        $scope.showPause   = false;
        $scope.status='stopping...';
        clearInterval($scope.autorefresh);
        source = '/trigger/record-stop';
        $http.get(source).success(function(data,status,headers,config) {
            location='http://localhost:8080/open-scan';
        });
    }
}


//-----------------------------------------------------------------------------
// Switches for Oscope channels

activeChannels = [];


function SwitchesCtrl($scope) {

    $scope.switchesList = [
        { channel: 1, show: true, color: 'aqua'},
        { channel: 2, show: true, color: 'red'},
        { channel: 3, show: true, color: 'lightgreen'},
        { channel: 4, show: true, color: 'yellow'},
        { channel: 5, show: true, color: 'aqua'},
        { channel: 6, show: true, color: 'red'},
        { channel: 7, show: true, color: 'lightgreen'},
        { channel: 8, show: true, color: 'yellow'},
        { channel: 9, show: true, color: 'aqua'},
        { channel: 10, show: true, color: 'red'},
        { channel: 11, show: true, color: 'lightgreen'},
        { channel: 12, show: true, color: 'yellow'},
    ];

    $scope.channels = [ ];

    $scope.getCount = function () {
        return $scope.channels.length;
    };

    $scope.allOn = function() {
        for (var c in $scope.switchesList) {
            $scope.switchesList[c].show = true;
        }
        $scope.selectChannels();
    }

    $scope.allOff = function() {
        for (var c in $scope.switchesList) {
            $scope.switchesList[c].show = false;
        }
        $scope.selectChannels();
    }

    $scope.selectChannels = function() {
        $scope.channels = _.filter($scope.switchesList, function(t) {
            return t.show;
        });
        activeChannels = [];
        for (var c in $scope.channels) {
            activeChannels.push($scope.channels[c].channel)
        }
        drawOscopeView($scope.data)
    };


    try {
        http.get('/sensors').success(function(data,status,headers,config) {
            $scope.data = csv_to_table(data)
            drawOscopeView($scope.data)
        });
    }
    catch(err) {
        ok = 'Error'
    };

    $scope.selectChannels()
}


