/*
 * View model for printerprofiles
 *
 * Author: You
 * License: AGPLv3
 */
$(function() {
    function PrinterprofilesViewModel(parameters) {
        var self = this;
        
        self.settings = parameters[0];
        
        self.selectProfileFast = function() {
        	console.log("selectProfileFast");
        };
        
        self.selectProfileMedium = function() {
        	console.log("selectProfileMedium");
        };
        
        self.selectProfileSlow = function() {
        	console.log("selectProfileSlow");
        };

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        PrinterprofilesViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        ["settingsViewModel"],

        // e.g. #settings_plugin_printerprofiles, #tab_plugin_printerprofiles, ...
        [ /* ... */ ]
    ]);
});
