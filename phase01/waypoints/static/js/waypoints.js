angular.module('waypointsApp', []);

waypointsApp.controller('waypointsAppController', ['$scope', function($scope) {
    $scope.fromAddress = '';
    $scope.toAddress = '';
}]);