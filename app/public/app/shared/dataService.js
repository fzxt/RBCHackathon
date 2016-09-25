app.service('DataService', function(){
  var selected = null;

  var select_data = function(loan_amount){
    selected = loan_amount
  }

  var get_selected = function(){
    return selected;
  }

  return {
    select: select_data,
    get: get_selected
  };

})
