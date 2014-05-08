angular.module('plunker', ['ui.bootstrap']);
function AccordionDemoCtrl($scope) {

  $scope.groups = [
    {title: "Test 1", content: "List #1", items: []},
    {title: "Test 2", content: "List #2", items: []},
    {title: "Test 3", content: "List #3", items: []},
    {title: "Test 4", content: "List #4", items: []}
  ];

  $scope.addItem = function(items) {
    var newItemNo = items.length + 1;
    items.push('Item ' + newItemNo);
  };
}
