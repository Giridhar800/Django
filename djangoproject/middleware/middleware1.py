from django.http import HttpResponse

# def demo_middleware(get_response):
#     print("one time initialization")
#     def fun_middleware(request):
#         print('This is before view calling')
#         response = get_response(request)
#         print("This is after view calling")
#         return response
#     return fun_middleware

# class FirstMiddleWare:
#     def __int__(self, get_response):
#         self.get_response = get_response
#         print('One time firstmiddleware intialization')
#
#     def __call__(self, request):
#         print("First middleware before view")
#         response =HttpResponse('response come from first middleware')
#         print("First middleware after view")
#         return response
#
# class SecondMiddleWare:
#     def __int__(self, get_response):
#         self.get_response = get_response
#         print('One time secondmiddleware intialization')
#
#     def __call__(self, request):
#         print("First middleware before view")
#         response = self.get_response(request)
#         print("This second middleware afterview")
#         return response
#
#
# class ThirdMiddleWare:
#     def __int__(self, get_response):
#         self.get_response = get_response
#         print('One time thirdmiddleware intialization')
#
#     def __call__(self, request):
#         print("First middleware before view")
#         response = self.get_response(request)
#         print("This third middleware afterview")
#         return response

class SiteUnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        return HttpResponse('<h1> Currently site is under construction please visite after few days</h1>')

