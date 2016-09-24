app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
    $routeProvider.when('/', {
            templateUrl: '/public/app/loans/loan.html'
        })
        .otherwise({
            templateUrl: '/public/app/loans/loan.html'
        });

    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    })
}])
