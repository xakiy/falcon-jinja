import falcon
from falcon.response import Response
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound

__all__ = ['FalconTemplate']


class FalconTemplateNotFound(Exception):
    pass


class FalconTemplate:
    """
        Keyword arguments:
            path(str): Where HTML files are defined

        Attributes:
            _env(jinja2.Environment): Class which loaded all HTML files
            _ctx(dict): An context for HTML
    """

    BASE_FOLDER = 'test_templates'

    def __init__(self, path: str = None):
        self.template_path = path or self.BASE_FOLDER
        self.loader = FileSystemLoader(self.template_path)
        self._env = Environment(loader=self.loader)
        self._ctx = {}

    def _get_jinja_context(self, response):
        return getattr(response, 'jinja_ctx', None)

    def _get_response(self, objects):
        for response in objects:
            if isinstance(response, Response):
                return response
        return False

    def _make_template(self, template: str, ctx: dict):
        try:
            template = self._env.get_template(template)
        except TemplateNotFound:
            raise FalconTemplateNotFound(
                'Template {} not found '
                'in {} folder'.format(template, self.template_path)
            )
        return template.render(**ctx)

    def render(self, template: str):
        def render(func):
            def wrapper(*args, **kwargs):
                resp = self._get_response(args)
                func(*args, **kwargs)
                jinja_ctx = self._get_jinja_context(resp)

                if jinja_ctx:
                    self._ctx = jinja_ctx

                resp.content_type = falcon.MEDIA_HTML
                resp.status = falcon.HTTP_200
                resp.body = self._make_template(template, self._ctx)
                return func(*args, **kwargs)
            return wrapper
        return render
