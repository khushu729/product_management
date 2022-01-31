//var studentListInstructor = angular.module('studentListInstructor', ['ngCookies', 'ui.bootstrap', 'ngResource', 'ngSanitize', "ui.router", "angularMoment","ui.calendar",])
//    .run(function($rootScope, backend_data) {
//
//    });
//
//studentListInstructor.config(['$httpProvider', '$sceDelegateProvider', function ($httpProvider, $sceDelegateProvider) {
//    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
//    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
//
//    $sceDelegateProvider.resourceUrlWhitelist([
//        'self',
//    ]);
//}]);


var productApp = angular.module('productApp', ['ngCookies', 'ngResource', 'ui.bootstrap']);
productApp.config(['$httpProvider', '$sceDelegateProvider', function ($httpProvider, $sceDelegateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);