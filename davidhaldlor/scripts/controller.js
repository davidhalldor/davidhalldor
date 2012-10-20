function DataListCtrl($scope, $http) {
  $http.get('/api/person').success(function(data) {
    $scope.items = data;
  });
}