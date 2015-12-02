from django.http import HttpResponse

class WWWRedirectMiddleware(object):

    def process_request(self, request):
        if not request.META['HTTP_HOST'].startswith('www.'):
            return
        response = HttpResponse(status=301)
        response['Location'] = 'http://pachydermpublishing.com' + request.path
        return response
