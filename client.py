import requests

url = "http://localhost:8080/"
print(f"Fazendo 10 requisições para {url}...")
print("-" * 40)

for i in range(10):
    r = requests.get(url)
    container_id = r.text.strip()
    print(f"Requisição {i+1}: Resposta do container -> {container_id}")

print("-" * 40)
print("Teste concluído.")
