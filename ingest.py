import requests
import json


class RetrieveData(object):
    def __init__(self):
        self.output = []
        self.local_url = 'http://127.0.0.1/ingest/'
        self.fixer_list_url = "https://api.apilayer.com/exchangerates_data/symbols"
        self.fixer_payload = {}
        self.fixer_headers= {
            "apikey": "U1tZzqShS1kOXPMINwXZ7VdvcIBXsl61"
        }
        self.get_data()
        self.process_data()

    def get_data(self):
        response = requests.get(url=self.fixer_list_url, headers=self.fixer_headers, data=self.fixer_payload)
        status_code = response.status_code
        if status_code == 200:
            result = response.json()
            symbols = result['symbols']
            for symbol in symbols.keys():
                pre_symbols = list(symbols.keys())
                pre_symbols.remove(symbol)
                symbols = ','.join(pre_symbols)
                self.exchangerates_url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base=EUR"
                response = requests.get(url=self.exchangerates_url, headers=self.fixer_headers, data=self.fixer_payload)
                status_code = response.status_code
                if status_code == 200:
                    result = response.json()
                    result.pop('success', None) # 200 is enough for success indication for this test
                    self.output.append(result)
                print(self.output)
                break

    def process_data(self):
        pass
        #print(json.loads(str(self.output)))
        # response = requests.request("POST", self.local_url, data=json.loads(self.output))
        # status_code = response.status_code
        # if status_code == 200:
        #     print("Successfully ingested currency data from fixer.io API")


if __name__ == '__main__':
    rd = RetrieveData()
