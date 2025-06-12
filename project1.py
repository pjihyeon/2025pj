import threading
import queue
import requests
from bs4 import BeautifulSoup

urls = [
    "https://example.com", "https://httpbin.org", "https://www.python.org"
]

q = queue.Queue()
results = []

def worker():
    while not q.empty():
        url = q.get()
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No Title"
            results.append((url, title))
        except Exception as e:
            results.append((url, str(e)))
        finally:
            q.task_done()

for url in urls:
    q.put(url)

threads = []
for _ in range(3):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for t in threads:
    t.join()

print("Results:", results)
