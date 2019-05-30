import os

from flask import abort, current_app, render_template, request
from flask.views import View
from jinja2.exceptions import TemplateNotFound

class TemplateFinder(View):
    """
    A TemplateView that guesses the template name based on the
    url path or redirects if defined in redirects.txt.
    """
    def dispatch_request(self, *args, **kwargs):
        """
        This is called when TemplateFinder is run as a view
        It tries to find the template for the request path
        and then passes that template name to TemplateView to render
        """
        path = request.path.lstrip("/")
        matching_template = self._get_template(path)

        if not matching_template:
            abort(404, f"Can't find page for: {path}")

        return render_template(matching_template, **self._get_context(path))

    def _get_template(self, url_path):
        """
        Given a basic path, find an HTML or Markdown file
        """

        # Try to match HTML or Markdown files
        if self._template_exists(url_path + ".html"):
            return url_path + ".html"
        elif self._template_exists(os.path.join(url_path, "index.html")):
            return os.path.join(url_path, "index.html")
        elif self._template_exists(url_path + ".md"):
            return url_path + ".md"
        elif self._template_exists(os.path.join(url_path, "index.md")):
            return os.path.join(url_path, "index.md")

        return None

    def _template_exists(self, path):
        """
        Check if a template exists
        without raising an exception
        """
        try:
            loader = current_app.jinja_loader
            loader.get_source({}, template=path)
        except TemplateNotFound:
            return False

        return True

    def _get_context(self, clean_path, **kwargs):
        """
        Get context data fromt the database for the given page.
        """
        context = {}

        # Add job role
        context['job_id'] = request.args.get('job_id')

        # Add level_* context variables
        for index, path, in enumerate(clean_path.split('/')):
            context["level_" + str(index + 1)] = path

        return context