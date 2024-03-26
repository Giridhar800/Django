from django.http import HttpResponse

# class SiteUnderConstruction:
#     def __init__(self,get_response):
#         self.get_response = get_response
#     def __call__(self, request):
#         return HttpResponse('Site is under contstruction pls visite some time')

class ErrorMessageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        return self.get_response(request)
    def process_exception(self, request,exception):
        return HttpResponse('currently we are facing some technical issues')
