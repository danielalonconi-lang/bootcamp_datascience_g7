from datetime import datetime

def transform(data):
    """
    transformamos la data de randomuser
    """
    transform_data = []
    for country in data:
        nombre = country.get('name', {}).get('common', 'N/A')
        capital = country.get('capital', ['N/A'])[0]  # capital es lista
        region = country.get('region', 'N/A')
        poblacion = country.get('population', 'N/A')
        transform_data.append((nombre,capital,region,poblacion))
    return transform_data