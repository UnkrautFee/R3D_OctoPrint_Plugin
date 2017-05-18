'''
Created on 12.05.2017

@author: FF
'''
# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin, 
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))
        
    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")
    
    def get_template_vars(self):
        return dict(url=self._settings.get(["url"]))
        
__plugin_name__ = "Hello World"
__plugin_implementation__ = HelloWorldPlugin()