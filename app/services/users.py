from app.adapters.country import CountryRequest
from app.adapters.aws import AwsRequest
from datetime import datetime
from geopy.distance import geodesic
from app.constants import AR_LATITUDE, AR_LONGITUDE


class Users():
    def __init__(self, request_data):
        self.request_data = request_data

    def get_user_data(self):
        data = {}
        data['ip'] = self.request_data['ip']
        data['user_id'] = self.request_data['user_id']
        data['iso_code'], data['country_name'] = self.__get_country_ip(data['ip'])
        data['timestamp'] = self.__get_timestamp()
        data['distance'] = self.__calculate_distance(data['iso_code'])
        data['aws_ip'] = self.__is_aws_ip(data['ip'])
        return data

    def __get_country_ip(self, ip):
        country = CountryRequest()
        data = country.get_country_by_ip(ip)
        iso_code = data.get("countryCode")
        country_name = data.get("countryName")
        return iso_code, country_name

    def __get_timestamp(self):
        return datetime.utcnow()

    def __calculate_distance(self, iso_code):
        distance = None
        latitude_longitude = self.__get_latitude_longitude(iso_code)
        if latitude_longitude is not None:
            latitude, longitude = latitude_longitude[0], latitude_longitude[1]
            origin = (AR_LATITUDE, AR_LONGITUDE)
            dist = (latitude, longitude)
            distance = geodesic(origin, dist).kilometers
        return round(distance)

    def __get_latitude_longitude(self, iso_code):
        country = CountryRequest()
        data = country.get_info(iso_code)
        return data.get("latlng")

    def __is_aws_ip(self, user_ip):
        aws_ip = False
        user_ip = user_ip.split('.')[:2]
        ip_ranges = self.__get_ip_prefixes()
        for item in ip_ranges:
            split = item['ip_prefix'].split('.')
            if split[0] == user_ip[0]:
                aws_ip = True
                break
        return aws_ip

    def __get_ip_prefixes(self):
        #add ipv6
        aws = AwsRequest()
        aws_data = aws.get_ip_prefixs()
        ip_ranges = aws_data['prefixes']
        return ip_ranges
