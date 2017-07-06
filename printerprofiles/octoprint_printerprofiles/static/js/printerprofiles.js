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
        	OctoPrint.slicing.updateProfileForSlicer("cura", self.settings.settings.plugins.printerprofiles.file_name_fast(), {default: true}, {});
        	console.log("selectProfileFast: " + self.settings.settings.plugins.printerprofiles.file_name_fast());
        	return true;
        };
        
        self.selectProfileMedium = function() {
        	OctoPrint.slicing.updateProfileForSlicer("cura", self.settings.settings.plugins.printerprofiles.file_name_medium(), {default: true}, {});
        	console.log("selectProfileMedium: " + self.settings.settings.plugins.printerprofiles.file_name_medium());
        	return true;
        };
        
        self.selectProfileSlow = function() {
        	OctoPrint.slicing.updateProfileForSlicer("cura", self.settings.settings.plugins.printerprofiles.file_name_slow(), {default: true}, {});
        	console.log("selectProfileSlow: " + self.settings.settings.plugins.printerprofiles.file_name_slow());
        	return true;
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
        ["#sidebar_plugin_printerprofiles"]
    ]);
});
