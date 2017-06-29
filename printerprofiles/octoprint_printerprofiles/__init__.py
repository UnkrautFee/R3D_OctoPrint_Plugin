# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin
#from jinja2 import Environment, PackageLoader
import flask
import logging
import logging.handlers

class PrinterprofilesPlugin(octoprint.plugin.StartupPlugin,
							octoprint.plugin.SettingsPlugin,
                            octoprint.plugin.AssetPlugin,
                            octoprint.plugin.TemplatePlugin):

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			# put your plugin's default settings here
			file_name_fast="config_blue",
			file_name_medium="config_gold",
			file_name_slow="config_blue"
		)

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/printerprofiles.js"],
			css=["css/printerprofiles.css"],
			less=["less/printerprofiles.less"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			printerprofiles=dict(
				displayName="Printerprofiles Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="you",
				repo="printerprofiles",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/you/printerprofiles/archive/{target_version}.zip"
			)
		)

    ##~~ Test

	#def get_template_configs(self):
	#	return [
	#		dict(type="sidebar", custom_bindings=True, template_header="printerprofiles_header.jinja2")
	#	]
		
	def on_after_startup(self):
		self._logger.info("PrinterProfiles Loaded; file_name_fast = %s" % self._settings.get(["file_name_fast"]))
		
	#wahrscheinlich unnötig, weil das cura plugin diese funktion ja schon hat.
	#def get_slicer_profile(self, path):
	#	profile_dict = self._load_profile(path)
	#	display_name = None
	#	description = None
	#	if "_display_name" in profile_dict:
	#		display_name = profile_dict["_display_name"]
	#		del profile_dict["_display_name"]
	#	if "_description" in profile_dict:
	#		description = profile_dict["_description"]
	#		del profile_dict["_description"]
	#	properties = self.get_slicer_properties()
	#	return octoprint.slicing.SlicingProfile(properties["type"], "unknown", profile_dict, display_name=display_name, description=description)
		
	#wahrscheinlich unnötig, weil das cura plugin diese funktion ja schon hat.
# 	def _load_profile(self, path):
# 		import yaml
# 		logging.warning("_load_profile was called.")
# 		profile_dict = dict()
# 		with open(path, "r") as f:
# 			logging.warning("Trying to read profile from {path}".format(path=path))
# 			try:
# 				profile_dict = yaml.safe_load(f)
# 			except:
# 				logging.warning("Couldn't read profile from {path}".format(path=path))
# 				raise IOError("Couldn't read profile from {path}".format(path=path))
# 		if "gcode_flavor" in profile_dict and not isinstance(profile_dict["gcode_flavor"], (list, tuple)):
# 			profile_dict["gcode_flavor"] = parse_gcode_flavor(profile_dict["gcode_flavor"])
# 			self._save_profile(path, profile_dict)
# 		return profile_dict
	
	
	#wahrscheinlich unnötig, weil das cura plugin diese funktion ja schon hat.
# 	def _save_profile(self, path, profile, allow_overwrite=True):
# 		import yaml
# 		with octoprint.util.atomic_write(path, "wb", max_permissions=0o666) as f:
# 			yaml.safe_dump(profile, f, default_flow_style=False, indent="  ", allow_unicode=True)
			
    
# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Print Speed"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = PrinterprofilesPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

