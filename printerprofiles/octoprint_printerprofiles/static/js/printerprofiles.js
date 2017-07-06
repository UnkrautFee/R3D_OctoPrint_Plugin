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
        
        self.testObjects = ko.observableArray([
        	{name: 'Eins'}, 
        	{name: 'Zwei'}, 
        	{name: 'Drei'}
        ]);
        
        OctoPrint.slicing.listProfilesForSlicer("cura", {}).done(function(n) {
        	self.curaProfiles = n;
        	console.log(n);
        	console.log(self.curaProfiles);
        });
        
        
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
        
        self.setProfileFast = function(profile) {
        OctoPrint.settings.savePluginSettings("printerprofiles", {file_name_fast: profile.name}, {});
        console.log("(Not implemented)Set fast profile to: " + profile.name);
        return true;
        };
        
        self.setProfileMedium = function(profile) {
        OctoPrint.settings.savePluginSettings("printerprofiles", {file_name_medium: profile.name}, {});
        	console.log("(Not implemented)Set medium profile to: " + profile.name);
        	return true;
        };
        
        self.setProfileSlow = function(profile) {
        OctoPrint.settings.savePluginSettings("printerprofiles", {file_name_slow: profile.name}, {});
        	console.log("(Not implemented)Set slow profile to: " + profile.name);
        	return true;
        };
       
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        PrinterprofilesViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        ["settingsViewModel"],

        // e.g. #settings_plugin_printerprofiles, #tab_plugin_printerprofiles, ...
        ["#sidebar_plugin_printerprofiles", "#settings_plugin_printerprofiles"]
    ]);
});
