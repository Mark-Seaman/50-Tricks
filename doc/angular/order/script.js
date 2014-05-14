function food($scope){

    $scope.items = [
        { title: 'coffee', price: 2},
        { title: 'tea', price: 2},
        { title: 'milk', price: 1},
        { title: 'pepsi', price: 4}
    ];


    $scope.total = function() {
        var t = 0
        angular.forEach($scope.items, function(s) {
            if(s.selected) t+=s.price
        })
        return t
    };


    $scope.selected = function() {
        var t = 0
        var sel = []
        angular.forEach($scope.items, function(s) {
            if(s.selected) sel.push(s)
        })
        return sel
    };
}
