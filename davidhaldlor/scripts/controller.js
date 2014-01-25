function PersonListCtrl($scope, $http) {
  $http.get('/api/person').success(function(data) {
    $scope.items = data;
  });
}

function EmployeeListCtrl($scope, $http) {
  $http.get('/api/employee').success(function(data) {
    $scope.items = data;
  });
}