import urllib.request
import urllib.parse
import json
import ssl


def api_getter(key: str, url: str):
    offset_counter = 1
    file_counter = 0
    # file_counter += 1
    # offset_counter += 1000
    # ssl._create_default_https_context = ssl._create_unverified_context
    api_url = url + 'offset=' + str(offset_counter)
    headers = {'token': key}
    r = urllib.request.Request(api_url, headers=headers)
    return r


def load_json(r: str, file_counter: int):
    while file_counter < 39:
        file_name = './location_' + str(file_counter) + '.json'
        with urllib.request.urlopen(r) as f:
            data = json.load(f)
        with open(file_name, 'w') as handler:
            json.dump(data, handler)


api_getter('YPfkbkEbwdPHBHLxeFSIJQGPzjLUJYIB', 'https://www.ncdc.noaa.gov/cdo-web/api/v2/')
# import urllib.request
# import urllib.parse
# import json


# api_getter('https://www.ncdc.noaa.gov/cdo-web/api/v2/',
#            'YPfkbkEbwdPHBHLxeFSIJQGPzjLUJYIB')



    # url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limt=1000&' + 'offset=' + str(offset_counter)
    # headers = {'token': '#my token'}
    # req = urllib.request.Request(url, headers=headers)
    # file_name = './location_' + str(file_counter) + '.json'
    # with urllib.request.urlopen(req) as f:
    #     data = json.load(f)
    #     with open(file_name, 'w') as handler:
    #         json.dump(data, handler)
    # file_counter += 1
    # offset_counter += 1000