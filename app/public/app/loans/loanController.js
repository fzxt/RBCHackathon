app.controller('LoanController', function ($scope, $location, DataService) {
  $scope.loan = 2000;
  $scope.price = {
    one: 200,
    two: 400,
    three: 750,
    four: 1000
  }
  $scope.price = [
    200,
    400,
    750,
    1000
  ]

  $scope.go = function (path, value) {
    DataService.select(value);
    $location.path(path);
  };

  $scope.isPriceValid = function (price) {
    return price > 0 && price <= $scope.loan ? 'green' : 'red';
  }

})
