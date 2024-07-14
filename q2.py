'''
2. Write a Python function that takes a list of URLs, attempts to download their content, and
retries up to 3 times if an error occurs. Use appropriate error handling to manage
different types of exceptions.
'''
import requests

def download(url):
    for i in range(3):
        try:
            return requests.get(url)
        except Exception as e:
            print("Attempt", i + 1,"failed", e,".")
    
url = input("Enter URL: ")
print(download(url))