angular.module('productApp')
.factory("productsListResource", ["$resource", function($resource){
    return $resource("/api/products/:id", {id: '@_id'},{
        query:{
            method: "GET",
            isArray: false
        },
        submit:{
            method: "POST",
        },
        delete:{
            method: "DELETE",
        },
        update:{
            method: "PUT",
        }
    })
}]);