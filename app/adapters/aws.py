from app.settings import API_AWS_IP
import requests
import sys


class AwsRequest:

    def get_ip_prefixs(self):
        try:
            response = requests.get(API_AWS_IP)
        except Exception:
            raise ValueError("Unexpected error:", sys.exc_info()[0])

        if response.status_code == 200:
            return response.json()

        if response.status_code == 204:
            return "NOT FOUND"
