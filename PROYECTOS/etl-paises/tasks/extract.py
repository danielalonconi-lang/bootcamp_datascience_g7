import requests

def extract():
    """
    extraer data de randomuser
    """
    URL = "https://restcountries.com/v3.1/region/America"
    response = requests.get(URL)
    
    if response.status_code == 200:
        return response.json()
    return []