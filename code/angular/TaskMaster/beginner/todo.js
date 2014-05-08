function ToDoCtrl($scope) {

    $scope.getCount = function() {
        return $scope.todoList.length;
    }

    $scope.todoList = [ 
        { text:'Watch video', done:false}, 
        { text:'Do more', done:true}
    ]

    $scope.clearDone = function() {
        $scope.todoList = _.filter($scope.todoList, function(t) { return !t.done; });
    }

    $scope.addTodo = function() {
        $scope.todoList.push({text:$scope.formTodoText, done:false});
        $scope.formTodoText = ''
    }

    $scope.listString = function() {
        s = ''
        var i=0;
        while ($scope.todoList[i])
        {
            s+=$scope.todoList[i].text + " & ";
            i++;
        }
        alert("Tasks: "+s);
    }

}
