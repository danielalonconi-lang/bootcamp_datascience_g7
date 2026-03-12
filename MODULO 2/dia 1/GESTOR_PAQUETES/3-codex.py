import requests

def obtener_persona_aleatoria():
    url = "https://randomuser.me/api/"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
    except requests.RequestException as exc:
        print(f"Error al consumir la API: {exc}")
        return

    data = respuesta.json()
    resultado = data.get("results", [])
    if not resultado:
        print("Respuesta sin datos.")
        return

    persona = resultado[0]
    nombre = persona.get("name", {})
    ubicacion = persona.get("location", {})
    correo = persona.get("email", "")

    nombre_completo = "{0} {1}".format(nombre.get("first", ""), nombre.get("last", "")).strip()
    ciudad = ubicacion.get("city", "")
    pais = ubicacion.get("country", "")

    print("Persona aleatoria")
    print(f"Nombre: {nombre_completo}")
    print(f"Email: {correo}")
    print(f"Ciudad: {ciudad}")
    print(f"Pais: {pais}")

if __name__ == "__main__":
    obtener_persona_aleatoria()
