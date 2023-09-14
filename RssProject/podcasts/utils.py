import requests
import json
import xmltodict


def universal_rss_parser(url):
    response = requests.get(url)
    t_data = response.text

    format_st = url.replace("/", "_")
    list_adress_url = list(format_st.split("."))
    file_name = list_adress_url[-1]

    with open(f'rss_files/{file_name}.xml', "w") as file:
        file.write(t_data)
    
    with open(f'rss_files/{file_name}.xml') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        json_data = json.dumps(data_dict)

        with open(f'rss_files/{file_name}.json', 'w') as json_file:
            json_file.write(json_data)
    

url = ""

universal_rss_parser(url)