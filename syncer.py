import asyncio
from datetime import date
import json
import os
import requests
from label_studio_sdk import Client
from const import LABEL_STUDIO_URL, API_KEY, EXPORT_PATH, IMG_PATH, PROJ_ID


def main():
    # Connect to the Label Studio API and check the connection
    lbsd = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
    if not lbsd.check_connection()['status'] == 'UP':
        print('Connection Fails! Please try again.')
        pass
    else:
        print('Connection Succeeds!')
        headers = {
            'Authorization': 'Token ' + API_KEY,
            'Content-Type': 'application/json',
        }
        data = {
            "path": "/home/ethanjia/dev/label-studio-pipeline/img",
            "regex_filter": "",
            "use_blob_urls": True,
            "title": "test sync",
            "description": "test sync",
            "last_sync": "2019-08-24T14:15:22Z",
            "last_sync_count": 0,
            "project": 1
        }
        # FIXME 这里的id不知道是啥
        response = requests.post(
            'http://localhost:8080/api/storages/localfiles/1/sync', headers=headers, data=json.dumps(data, separators=(',', ':')))
        print(response.json())


if __name__ == '__main__':
    main()
