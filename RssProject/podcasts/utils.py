import requests
import xmltodict
from rest_framework.exceptions import APIException



class RequestConnectionError(APIException):
    status_code = 502
    default_detail = 'Request connection error.'
    default_code = '403'



def universal_rss_parser(url):

    response = requests.get(url)
    t_data = response.text

    xml_data = xmltodict.parse(t_data)
    return xml_data

    