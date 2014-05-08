'use strict';

angular.module('angularjsProjectApp')
    .controller('MainCtrl', function ($scope) {

        $scope.topics = [];

        $scope.add = function(){
            $scope.topics.push($scope.name)
            $scope.name = ''
        }

    });
