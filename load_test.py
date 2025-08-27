import requests
import concurrent.futures

URL = "http://localhost:8000/"

def hit_endpoint(_):
    response = requests.get(URL)
    return response.status_code

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(hit_endpoint, range(100)))

    print(f"Sent {len(results)} requests. Success = {results.count(200)}")
