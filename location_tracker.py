import requests
import argparse
import json


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--ipaddress", help="IP address to track")

    args = parser.parse_args()

    ip = args.ipaddress

    url = "http://ip-api.com/json/"+ip

    # http://ip-api/json/192.168.0.1

    response  = requests.get(url)

    data = json.loads(response.content)
    print(data)

