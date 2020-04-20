import base64
import json
import os

import requests

token = os.environ.get('SERVIY_OAUTH_TOKEN', None) or input('OAuth token: ')


def encode_file(file):
    with open(file, 'rb') as f:
        file_content = f.read()
    return base64.b64encode(file_content).decode('utf-8')


image_data = encode_file('bla.jpeg')
res_file = open("results.txt", "w")


def extract_image(vision_url, iam_token, catalog_id):
    response = requests.post(vision_url, headers={'Authorization': 'Bearer ' + iam_token}, json={
        'folderId': catalog_id,
        'analyzeSpecs': [
            {
                'content': image_data,
                'features': [
                    {
                        'type': 'TEXT_DETECTION',
                        'textDetectionConfig': {'languageCodes': ['en', 'ru']}
                    }
                ],
            }
        ]})
    return response.text


def get_iam_token(oauth_token):
    response = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens',
                             json={"yandexPassportOauthToken": oauth_token})
    json_data = json.loads(response.text)
    if json_data is not None and 'iamToken' in json_data:
        return json_data['iamToken']
    return None


def totext():
    catalog_id = 'b1gah3b0s98i5term047'
    vision_url = 'https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze'
    iam_token = get_iam_token(token)

    if iam_token is None:
        return "Couldn't get IAM token", 500
    try:
        data_file = extract_image(vision_url, iam_token, catalog_id)
    except requests.exceptions.RequestException as e:
        return str(e), 500

    json_text = json.loads(data_file)
    results = json_text['results'][0]['results'][0]['textDetection']
    pages = results['pages']
    for page in pages:
        for block in page['blocks']:
            for line in block['lines']:
                for word in line['words']:
                    res_file.write(word['text'] + ' ')
            res_file.write('\n')


if __name__ == '__main__':
    totext()
