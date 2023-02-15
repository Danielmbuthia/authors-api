from rest_framework.views import exception_handler

def common_exceptions_handler(exception,context):
    
    response = exception_handler(exception,context)
    
    handlers = {
        "NOT_FOUND": _handle_not_found_exception,
        "ValidationError": _handle_validation_error
    }
    
    exception_class = exception.__class__.__name__
    
    if exception_class in handlers:
        return handlers[exception_class](exception,context,response)
    return response

def _handle_not_found_exception(exception,context,response):
    view = context.get_view("view",None)
    if view and hasattr(view, "queryset") and view.queryset is not None:
        status_code = response.status_code
        error_key = view.queryset.model._meta_verbose_name
        response.data = {"status_code":status_code,"errors":{error_key: response.data['details']}}
    else:
        response = _handle_validation_error(exception,context)
    return response
        

def _handle_validation_error(exception,context,response):
    status_code = response.status_code
    response.data = {"status_code":status_code,"errors":response.data}
    return response