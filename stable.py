import requests
import webbrowser

URL = "https://backend.craiyon.com/generate"

prompt =input() 

response = requests.post(URL, json={"prompt": prompt})

if response.status_code == 200:
    result = response.json()
    image_urls = result['images'] 

    image_data = requests.get(image_urls[0]).content

    with open("generated_image.png", "wb") as f:
        f.write(image_data)

    print("Imagen generada y guardada como 'generated_image.png'.")

    webbrowser.open("generated_image.png")
else:
    print(f"Error: {response.status_code}")
    print(response.text)

