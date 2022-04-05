import requests



def think(x):
    headers = {
        'Authorization': 'Bearer EAVEWGZUG4RS3WH2S3ILAYIPKKKUPTEL',
    }
    params = (
        ('v', '20220217'),
        ('q', x),
    )
    response = requests.get('https://api.wit.ai/message', headers=headers, params=params).json()
    return response


