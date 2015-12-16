from django_template_finder_view import TemplateFinder
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponse
from django.template import RequestContext, loader, Context

class CanonicalTemplateFinder(TemplateFinder):
    def get_context_data(self, **kwargs):
        """
        Get context data fromt the database for the given page
        """

        # Get any existing context
        context = super(CanonicalTemplateFinder, self).get_context_data(**kwargs)

        # Add level_* context variables
        clean_path = self.request.path.strip('/')
        for index, path, in enumerate(clean_path.split('/')):
            context["level_" + str(index + 1)] = path

        return context


def custom_404(request):
    t = loader.get_template('templates/404.html')
    context = RequestContext(request, {'request_path': request.path})
    return HttpResponseNotFound(t.render(context))

def custom_500(request):
    t = loader.get_template('templates/500.html')
    return HttpResponseServerError(t.render(Context({})))
