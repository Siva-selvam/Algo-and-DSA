#Printing numbers using threads:

import threading
import time

def print_numbers():
    for i in range(1, 11):
        time.sleep(1)
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()

#Downloading files using threads:

import threading
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

urls = [
    "https://www.example.com/file1.pdf",
    "https://www.example.com/file2.pdf",
    "https://www.example.com/file3.pdf"
]

threads = []
for url in urls:
    filename = url.split("/")[-1]
    thread = threading.Thread(target=download_file, args=(url, filename))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()