angular.module('productApp')
.controller("ProductListController", ["$scope", "backend_data", "productsListResource", "$uibModal", function ($scope, backend_data, productsListResource, $uibModal) {
    $scope.is_admin = backend_data.is_admin;
    $scope.categories = JSON.parse(backend_data.categories);

    productsListResource.get().$promise
        .then(function(data){
            $scope.products = data.results;
        });

    $scope.add_product = function () {
        $scope.AddProductPopUp = $uibModal.open({
            backdrop: 'static',
            size: 'lg',
            templateUrl: 'addProductModal.html',
            windowClass: 'add-product',
            controller: function () {
                return $scope;
            },
            bindToController: true,
            keyboard: false,
            controllerAs: "vm"
        });

    }
    $scope.cancel = function () {
        $scope.AddProductPopUp.close();
    };

    $scope.submit_new_product = function(product_details){
        var data = product_details;
        data['user'] = backend_data.user_id;
        data['category'] = JSON.parse(data['category']);
        productsListResource.submit(data).$promise
        .then(function(data){
            productsListResource.get().$promise
                .then(function(data){
                    $scope.products = data.results;
                });
            $scope.AddProductPopUp.close();
        })
        .catch(function(e) {
            if (e.status == 400){
                alert("Please enter correct details!!!");
            }
            console.log('Error: ', e);
        })

    }

    $scope.delete_product = function(product_id){
        if(confirm("Are you sure??")) {
            productsListResource.delete({id:product_id}).$promise
                .then(function(data){
                    productsListResource.get().$promise
                        .then(function(data){
                            $scope.products = data.results;
                        });
                })
                .catch(function(e) {
                    if (e.status == 403){
                        alert(e.data.detail);
                    }
                    console.log('Error: ', e);
                })
        }
    }

    $scope.search = function(search_value){
        productsListResource.get({search: search_value}).$promise
        .then(function(data){
            $scope.products = data.results;
        });
    }

    $scope.filter_by_category = function(){
        var cat_value = JSON.parse($scope.category_filter_value)[0];
        productsListResource.get({filter_by_category: cat_value}).$promise
        .then(function(data){
            $scope.products = data.results;
        });
    }

    $scope.clear = function(){
        productsListResource.get().$promise
        .then(function(data){
            $scope.products = data.results;
            $scope.category_filter_value = "";
            $scope.search_value = "";
        });
    }

    $scope.update_product_modal = function (product) {
        $scope.UpdateProductPopUp = $uibModal.open({
            backdrop: 'static',
            size: 'lg',
            templateUrl: 'updateProductModal.html',
            windowClass: 'update-product',
            controller: function () {
                $scope.update_details = product;
                $scope.update_details['manufacture_date'] = new Date(product['manufacture_date']);
                $scope.update_details['expiry_date'] = new Date(product['expiry_date']);
                $scope.update_details['category'][0] = product['category'][0].toString();
                return $scope;
            },
            bindToController: true,
            keyboard: false,
            controllerAs: "vm"
        });

    }
    $scope.cancel_update_modal = function () {
        $scope.UpdateProductPopUp.close();
    };

    $scope.update_product = function(data){
        productsListResource.update({id:data.id}, data).$promise
        .then(function(data){
            productsListResource.get().$promise
                .then(function(data){
                    $scope.products = data.results;
                });
            $scope.UpdateProductPopUp.close();
        })
        .catch(function(e, response) {
            if (e.status == 400){
                for(var key in e.data) {
                     alert(e.data[key]);
                }
            }else if(e.status == 403){
                alert('You do not have permission to perform this action.');
            }
            console.log('Error: ', e);
        })
    }

//.controller('addProductModalController', ['$scope', function($scope){
//
//}]);

}]);