angular.module('plunker', ['ui.bootstrap']);


var food =  { appetizers: 
              [
                  { text:'crab puffs', done:false}, 
                  { text:'crackers', done:true},
                  { text:'veggies', done:true} 
              ],
              main_course:
              [
                  { text:'lamb', done:false}, 
                  { text:'fish', done:true},
                  { text:'beef', done:true} 
              ]
            }

function Food_Select_Ctrl($scope) {
    $scope.appetizers  = food.appetizers;
    $scope.main_course = food.main_course;
}
