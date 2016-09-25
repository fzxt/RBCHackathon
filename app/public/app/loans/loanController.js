app.controller('LoanController', function ($scope, $location, DataService) {
  $scope.loan = 2000;

  $scope.price = [
    200,
    400,
    750,
    1000
  ]

  $scope.go = function (path, value) {
    DataService.select_loan_amount(value);
    $location.path(path);
  };

  $scope.isPriceValid = function (price) {
    return price > 0 && price <= $scope.loan ? 'green' : 'red';
  }

})
