from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

MODULE_NAME = "Foundation 6"

class Foundation6Rowlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "foundation6/row_plugin.html"
    cache = False
    allow_children = True
    module = MODULE_NAME
    name = "Row"

plugin_pool.register_plugin(Foundation6Rowlugin)

class Foundation6Columnlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "foundation6/column_plugin.html"
    cache = False
    allow_children = True
    module = MODULE_NAME
    name = "Column"

plugin_pool.register_plugin(Foundation6Columnlugin)