import urllib.request
import urllib.parse
import json
import ssl


# a = iterator

# limit = data param (set to 1000)
# while a <=  limits count goes up to 39 on completion


def api_getter(url: str, key: str):
    offset_counter = 1
    file_counter = 0

    while file_counter < 39:

        ssl._create_default_https_context = ssl._create_unverified_context
        api_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&' + 'offset='\
            + str(offset_counter)
        headers = {'token': key}
        # endpoint = endpoint
    # limit = lim
        r = urllib.request.Request(api_url, headers = headers)
        file_name = './location_' + str(file_counter) + '.json'
        with urllib.request.urlopen(r) as f:
            data = json.load(f)
            with open(file_name, 'w') as handler:
                json.dump(data, handler)
         # print(data)
        file_counter += 1
        offset_counter += 1000


# offset count = ramps up 1000 each time (+ 1000)


api_getter('https://www.ncdc.noaa.gov/cdo-web/api/v2/',
           'YPfkbkEbwdPHBHLxeFSIJQGPzjLUJYIB')


# import urllib.request
# import urllib.parse
# import json


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