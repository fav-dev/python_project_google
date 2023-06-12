#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

def upload_file(url, file_path):
    with open(file_path, 'rb') as file:
        response = requests.post(url, files={'file': file})
        return response

if __name__ == '__main__':
    url = "http://localhost/upload/"
    image_path = '/home/student-01-a0a7adef2f7c/supplier-data/images'
    for image in image_path:
        response = upload_file(url, image_path)
        print(response.status_code)
