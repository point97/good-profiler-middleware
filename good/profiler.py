"""
Good Profiler Middleware

Based on http://www.djangosnippets.org/snippets/186 et. al. 

Installation: 

pip install good-profiler-middleware

Add the middleware to MIDDLEWARE_CLASSES like so:

    MIDDLEWARE_CLASSES = (
        'good.profiler.Middleware',
        ...
    )

It is often convenient to place it first in the middleware stack.

Add the following to settings.py (optional):

# Profiler output goes in this directory. Make sure the web server has write 
# permissions. If not specified, uses /tmp
PROFILER_DUMP_PATH = '/path/to/some/dir'

See README.md for details. 
"""
 
import os
import datetime
import cProfile
import StringIO
from django.conf import settings

class Middleware(object):
    def should_profile(self, request):
        return ((settings.DEBUG or request.user.is_superuser) 
                and not request.META.get('HTTP_REFERER'))

    def process_request(self, request):
        if self.should_profile(request):
            self.prof = cProfile.Profile()
 
    def process_view(self, request, callback, callback_args, callback_kwargs):
        if self.should_profile(request):
            return self.prof.runcall(callback, request, *callback_args, 
                                     **callback_kwargs)
 
    def process_response(self, request, response):
        if self.should_profile(request):
            stamp = datetime.datetime.strftime(datetime.datetime.now(), 
                                               '%d-%h-%Y_%H-%M-%S.%s')
            path = getattr(settings, 'PROFILER_DUMP_PATH', '/tmp')
            path = os.path.join(path, '%s_%s.stats' % (stamp, request.method))
            self.prof.dump_stats(path)
            
        return response
