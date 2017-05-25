'''
Created on 12.05.2017

@author: FF
'''
# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin, 
                       octoprint.plugin.TemplatePlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!")
        
__plugin_name__ = "Hello World"
__plugin_version__ = "1.0.0"
__plugin_description__ = "A quick \"Hello World\" example plugin for OctoPrint"
__plugin_implementation__ = HelloWorldPlugin()