import requests
import json


class RetrieveData(object):
    def __init__(self):
        self.output = []
        self.local_url = 'http://127.0.0.1/ingest/'
        self.fixer_list_url = "https://api.apilayer.com/currency_data/list/"
        self.fixer_payload = {}
        self.fixer_headers= {
            "apikey": "NlS3YrjhSRlgrviJ468BoD0u5jhbivjH"
        }
        self.get_data()
        self.process_data()

    def get_data(self):
        response = requests.request("GET", self.fixer_list_url, headers=self.fixer_headers, data=self.fixer_payload)
        status_code = response.status_code
        if status_code == 200:
            result = response.text
            self.in_json = json.loads(result)
            if self.in_json['success'] == 'true':
                symbols = self.in_json['symbols']
                for symbol in symbols.keys():
                    self.fixer_currency_url = "https://api.apilayer.com/currency_data/live/?base={symbol_source}&symbols={','.join(symbols.keys())}}"
                    response = requests.request("GET", self.fixer_currency_url, headers=self.fixer_headers, data=self.fixer_payload)
                    status_code = response.status_code
                    if status_code == 200:
                        result = response.text
                        self.output.append(json.loads(result))

    def process_data(self):
        response = requests.request("POST", self.local_url, data=json.loads(self.output))
        status_code = response.status_code
        if status_code == 200:
            print("Successfully ingested currency data from fixer.io API")
