import requests


def tracker_data(event, tier):

    url = 'https://bestdori.com/api/tracker/data?server=0&event=' + event + '&tier=' + tier
    response = requests.get(url, verify=False)
    # response = requests.get('http://www.baidu.com')
    return response.json()
