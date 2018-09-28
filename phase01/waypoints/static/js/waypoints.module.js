angular.module('waypointsApp', [
    'mapModule'
]);

waypointsApp.controller('waypointsAppController', ['$scope', function($scope) {
    $scope.fromAddress = 'hooga';
    $scope.toAddress = 'booga';
}]);