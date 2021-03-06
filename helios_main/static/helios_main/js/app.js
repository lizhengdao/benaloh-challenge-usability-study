'use strict';

var heliosStudyMainApp = angular.module(
    "heliosStudyMain",
    [
        "ngAnimate",
        "ngRoute",
        "localization",
        "BackendService"
    ]
).config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
    $routeProvider.
        when('/:id', {templateUrl: '/static/helios_main/partials/introduction.html', controller: 'introductionCtrl'}).
        when('/election/:id', {templateUrl: '/static/helios_main/partials/election.html', controller: 'electionCtrl'}).
        when('/review/:id', {templateUrl: '/static/helios_main/partials/review.html', controller: 'electionCtrl'}).
        when('/print/:ballot_tracker', {templateUrl: '/static/helios_main/partials/printtracker.html', controller: 'printCtrl'}).
        when('/institute/:id', {templateUrl: '/static/helios_main/partials/institute.html', controller: 'electionCtrl'}).
        when('/cast/:id', {templateUrl: '/static/helios_main/partials/cast.html', controller: 'electionCtrl'}).
        when('/final/:id', {templateUrl: '/static/helios_main/partials/finaloverview.html', controller: 'electionCtrl'}).
        when('/audit_bsi/:id', {templateUrl: '/static/helios_main/partials/audit_bsi.html', controller: 'electionCtrl'}).
        when('/audit_osze/:id', {templateUrl: '/static/helios_main/partials/audit_osze.html', controller: 'electionCtrl'}).
         when('/auditdone/:id', {templateUrl: '/static/helios_main/partials/auditdone.html', controller: 'electionCtrl'}).
        when('/error/', {templateUrl: '/static/helios_main/partials/error.html', controller: 'errorCtrl'}).
        otherwise({templateUrl: '/static/helios_main/partials/introduction.html', controller: 'introductionCtrl'});
    // use the HTML5 History API
    $locationProvider.html5Mode(true).hashPrefix('!');
}]);

heliosStudyMainApp.run(function ($rootScope, $window, $document, localize) {
    // root scope functions
    $rootScope.getLanguages = function () {
        return ['en', 'de'];
    };
    $rootScope.$watch('language', function (newLang) {
        localize.setLanguage(newLang);
        $rootScope.$broadcast('langChange', newLang);
    });

    // initialization
    if (!$rootScope.language) {
        $rootScope.language = $window.navigator.userLanguage ||
                              $window.navigator.language ||
                              $document.getElementsByTagName('html')[0].lang;
        if ($rootScope.language && ($rootScope.language.length > 2)) {
            $rootScope.language = $rootScope.language.substr(0, 2);
        }
        //If hard coding a language is desired, do it here, if not delete the following line
        $rootScope.language = "de";
     }
});