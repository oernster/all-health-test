import requests
import json


class RetrieveData(object):
    def __init__(self):
        self.API_CALL_LIMIT = 5
        self.output = []
        self.timeout = 0
        self.local_url = 'http://127.0.0.1:8000/ingest/'
        self.fixer_list_url = "https://api.apilayer.com/exchangerates_data/symbols"
        self.fixer_payload = {}
        self.fixer_headers= {
            "apikey": "U1tZzqShS1kOXPMINwXZ7VdvcIBXsl61"
        }
        self.get_data()
        self.timeout = 0
        self.process_data()
        self.timeout = 0

    def get_data(self):
        try:
            response = requests.get(url=self.fixer_list_url, headers=self.fixer_headers, data=self.fixer_payload)
            status_code = response.status_code
            if status_code == 200:
                result = response.json()
                symbols = result['symbols']
                for cnt, symbol in enumerate(symbols.keys()):
                    pre_symbols = list(symbols.keys())
                    pre_symbols.remove(symbol)
                    post_symbols = ','.join(pre_symbols)
                    self.exchangerates_url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={post_symbols}&base={symbol}"
                    response = requests.get(url=self.exchangerates_url, headers=self.fixer_headers, data=self.fixer_payload)
                    status_code = response.status_code
                    if status_code == 200:
                        result = response.json()
                        result.pop('success', None) # 200 is enough for success indication for this test
                        self.output.append(result)
                    if cnt == (self.API_CALL_LIMIT - 1): # Free 3rd Party API is limited to 100 calls a day so limit to 5 calls for now.
                        break
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            if self.timeout < 3:
                self.timeout += 1
                self.get_data()
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            print("Too many redirects; possible bad URL?")
        except requests.exceptions.RequestException as e:
            # Disaster.
            print("Requests failure.")
            raise SystemExit(e)

    def process_data(self):
        try:        
            for cnt, item in enumerate(self.output):
                rates = str(item['rates']).replace('{', '').replace('}', '')
                currency_data = {
                    'timestamp': item['timestamp'],
                    'base': item['base'].replace("'", '"'),
                    'date': item['date'].replace("'", '"'),
                    'rates': rates.replace("'", ''),
                }
                response = requests.post(url=self.local_url, data=json.dumps(currency_data))
                status_code = response.status_code
                if status_code == 200:
                    print(f"Successfully ingested currency data item no. {cnt+1} from fixer.io API")
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            if self.timeout < 3:
                self.timeout += 1
                self.process_data()
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            print("Too many redirects; possible bad URL?")
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)

if __name__ == '__main__':
    rd = RetrieveData()
