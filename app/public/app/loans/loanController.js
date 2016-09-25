app.controller('LoanController', function($scope) {
  $scope.loan = 2000;
  $scope.price = {
    one: 200,
    two: 400,
    three: 750,
    four: 1000
  }

  $scope.isPriceValid = function(price){
    return price > 0 && price <= $scope.loan ? 'green' : 'red';
  }

})
