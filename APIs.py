import requests

respuesta = requests.get("https://fakestoreapi.com/products/", params={"limit":3})

print(respuesta.json())

print(respuesta.status_code)

#Añadir a la API
nuevoProducto = {"title":"Ordenador", "price":12, "description":"ordenador de prueba", "category":"electronic"}
respuesta = requests.post("https://fakestoreapi.com/products", json=nuevoProducto)
print(respuesta)

