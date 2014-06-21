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

function InterestListCtrl($scope, $http) {
  $http.get('/api/interest').success(function(data) {
    $scope.items = data;
  });
}

function EducationListCtrl($scope, $http) {
  $http.get('/api/education').success(function(data) {
    $scope.items = data;
  });
}

function SkillListCtrl($scope, $http) {
  $http.get('/api/skill').success(function(data) {
    $scope.items = data;
  });
}

function CodeListCtrl($scope, $http) {
  $http.get('/api/code').success(function(data) {
    $scope.items = data;
  });
}

function SocialListCtrl($scope, $http) {
  $http.get('/api/social').success(function(data) {
    $scope.items = data;
  });
}