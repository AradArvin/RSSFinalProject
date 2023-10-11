from datetime import datetime
from typing import Any
from elasticsearch import Elasticsearch



class ElasticsearchAPIMiddleWare:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.es = Elasticsearch("http://elasticsearch:9200")


    def __call__(self, request) -> Any:
        ip_address = get_client_ip_address(request)

        response = self.get_response(request)
        user = request.user if hasattr(request, "user") else None

        log_data = {
        'timestamp': datetime.now(),
        'request_method': request.method,
        'request_path': request.path,
        'request_ip': ip_address,
        'request_user_agent': request.META.get('HTTP_USER_AGENT', 'null'),
        'event': "api_req",
        'user': user.id if user else None,
        'status_code': response.status_code,
        }
        
        self.es.index(index='api_logs', document=log_data)
        
        return response
    

    def process_exception(self, request, exception):
        ip_address = get_client_ip_address(request)

        log_data = {
            'timestamp': datetime.now(),
            'request_method': request.method,
            'request_path': request.path,
            'request_ip': ip_address,
            'request_user_agent': request.META.get('HTTP_USER_AGENT', 'null'),
            'exception_type': exception.__class__.__name__,
            'exception_message': exception.message if hasattr(exception, "message") else str(exception),
            'event': "api_exc",
        }

        self.es.index(index='request_exception_logs', document=log_data)
        



def get_client_ip_address(request):
    request_headers = request.META
    x_forwarded_for = request_headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_addr = x_forwarded_for.split(',')[0]
    else:
        ip_addr = request_headers.get('REMOTE_ADDR')
    return ip_addr

