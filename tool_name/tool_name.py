import requests

def lambda_handler(event, context):
    url = "https://data.nationalgrideso.com/ancillary-services/dynamic-containment-data/datapackage.json"

    response = requests.get(url)
    print(f'Received response code {response.status_code}')



if __name__=="__main__":
    lambda_handler(None, None)