from pyramid.config import Configurator

from .settings import SettingsFactory


class Application(object):

    def __init__(self, module):
        self.module = module

    def run_uwsgi(self, settings={}):
        self._create_app(settings, 'uwsgi')
        return self._return_wsgi_app()

    def run_tests(self, settings={}):
        self._create_app(settings, 'tests')

    def run_shell(self, settings={}):
        self._create_app(settings, 'shell')

    def run_command(self, settings={}):
        self._create_app(settings, 'command')

    def _create_app(self, settings={}, settings_name='uwsgi'):
        self._generate_settings(settings, settings_name)
        self._create_config()
        self._generate_registry(self.config.registry)
        self._generate_routes()

    def _generate_settings(self, settings, endpoint, factory=SettingsFactory):
        settings_module = self._get_settings_module()
        settings, paths = factory(settings_module).get_for(endpoint)
        self.settings = settings
        self.paths = paths

    def _get_settings_module(self):
        return '%s.application.settings' % (self.module, )

    def _create_config(self):
        kwargs = self._get_config_kwargs()
        self.config = Configurator(**kwargs)

    def _get_config_kwargs(self):
        return {
            'settings': self.settings.to_dict(),
        }

    def _generate_registry(self, registry):
        registry['settings'] = self.settings
        registry['paths'] = self.paths

    def _generate_routes(self):
        pass

    def _return_wsgi_app(self):
        return self.config.make_wsgi_app()
