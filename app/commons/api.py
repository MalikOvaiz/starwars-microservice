import requests


class API:

    @staticmethod
    def get(url):
        return requests.get(url, data={}).json()
