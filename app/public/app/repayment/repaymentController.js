app.controller('RepaymentController', function($scope, DataService) {
  $scope.data = DataService.get_loan_amount();
  // $scope.data = 300;

  $scope.entries = [];

  $scope.selected_option = null;


  function init(){
  var interest_rate = 0.10;
    for (var i=4; i < 17; i+=4){
      var interest_amount = $scope.data*interest_rate;
      var total = $scope.data + interest_amount;
      $scope.entries.push({
        'length': i,
        'interest_amount': interest_amount,
        'total': total,
        'interest_rate': interest_rate * 100,
        'monthly_rate': total/i
      })
      interest_rate += 0.02;
    }
    console.log($scope.entries);
  }
  init();

  $scope.entry_is_selected = function(){
    return $scope.selected_option != null;
  }

  $scope.select_repayment = function(value){
    $scope.selected_option = value;
    DataService.select_plan(value);
  }

})
