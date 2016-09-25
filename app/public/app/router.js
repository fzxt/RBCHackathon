app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
  $routeProvider.when('/', {
    templateUrl: '/public/app/loans/loan.html',
    controller: 'LoanController'
    })
    .when('/repayment', {
      templateUrl: '/public/app/repayment/repayment.html',
      controller: 'RepaymentController'
    })
    .otherwise({
      templateUrl: '/public/app/loans/loan.html'
    });

  $locationProvider.html5Mode({
    enabled: true,
    requireBase: false
  })
}])
