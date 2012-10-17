function DataListCtrl($scope, $http) {
  $http.get('/api/personal').success(function(data) {
    $scope.items = data;
  });
}