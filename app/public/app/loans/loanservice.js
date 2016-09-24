app.factory("Loan", function($http){
    return{
        all : function(){
            return $http({
                method: 'GET',
                url: '/api/items'
            })
        }
    }
})
