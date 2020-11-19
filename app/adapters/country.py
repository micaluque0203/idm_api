from app.settings import API_COUNTRY_INFO, API_COUNTRY_IP
import requests
import sys


class CountryRequest():

    def get_info(self, country):
        url = API_COUNTRY_INFO + country
        try:
            response = requests.get(url)
        except Exception:
            raise ValueError("Unexpected error:", sys.exc_info()[0])

        if response.status_code == 200:
            return response.json()

        if response.status_code == 204:
            return "NOT FOUND"

    def get_country_by_ip(self, ip):
        url = API_COUNTRY_IP + '/ip?{ip}'.format(ip=ip)
        try:
            response = requests.get(url)
        except Exception:
            raise ValueError("Unexpected error:", sys.exc_info()[0])

        if response.status_code == 200:
            return response.json()

        if response.status_code == 204:
            return "NOT FOUND"
