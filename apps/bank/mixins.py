# from django.core.exceptions import ValidationError
# from rest_framework import exceptions as rest_exceptions

# from apps.bank.utils import get_error_message

# class ServiceExcrptionHandleMixin:
#     excepted_exception = {
#         ValueError: rest_exceptions.ValidationError, 
#         ValidationError: rest_exceptions.ValidationError,
#         PermissionError: rest_exceptions.PermissionDenied
#     }

#     def handle_exception(self, exc):
#         print('handle exception was called')
#         if isinstance(exc, tuple(self.excepted_exception.kyes())):
#             drf_exception_class = self.excepted_exception[exc.__class__]
#             drf_exception = drf_exception_class(get_error_message(exc))

#             return super().handle_exception(drf_exception)
   
#         return super().handle_exception(exc)