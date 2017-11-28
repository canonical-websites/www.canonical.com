"""
Django views for www.canonical.com.
"""
from django.views.generic.base import TemplateView
from django_template_finder_view import TemplateFinder

from webapp.templatetags.raw_feeds import get_raw_json_feed


class GreenhouseVacancies(TemplateView):
    template_name = "_vacancies/all-vacancies.html"

    def get_vacancies(self):
        feed = get_raw_json_feed(
            'https://api.greenhouse.io/v1/boards/Canonical/jobs'
        )
        job_departments = {}
        # departments_added = []
        for job in feed['jobs']:
            department = job['metadata'][0]['value']
            # if department not in departments_added:
            #     job_departments.append({
            #         'id': department,
            #         'jobs: [],
            #     })
            #     departments_added.append(department)
            if department not in job_departments.keys():
                job_departments[department] = []

            job_departments[department].append({
                'title': job['title'],
                'url': job['absolute_url'],
                'location': job['location'],
            })
        import pprint
        pprint.pprint(job_departments)
        return job_departments

    def get_context_data(self, **kwargs):
        context = super(GreenhouseVacancies, self).get_context_data(**kwargs)
        context['jobs'] = self.get_vacancies()
        return context


class CanonicalTemplateFinder(TemplateFinder):
    """
    Local customisations of the shared django_template_finder_view.
    """

    def get_context_data(self, **kwargs):
        """
        Get context data fromt the database for the given page.
        """

        # Get any existing context
        context = super(CanonicalTemplateFinder, self).get_context_data(
            **kwargs
        )

        # Add job role
        context['job_id'] = self.request.GET.get('job_id')

        # Add level_* context variables
        clean_path = self.request.path.strip('/')
        for index, path, in enumerate(clean_path.split('/')):
            context["level_" + str(index + 1)] = path

        return context
