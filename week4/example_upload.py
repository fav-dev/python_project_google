#!/usr/bin/env python3
import requests

def upload_file(url, file_path):
    with open(file_path, 'rb') as file:
        response = requests.post(url, files={'file': file})
        return response

if __name__ == '__main__':
    url = "http://localhost/upload/"
    file_path = '/usr/share/apache2/icons/icon.sheet.png'
    response = upload_file(url, file_path)
    print(response.status_code)
