from datetime import datetime, timedelta

def lambda_handler(event, context):
    today = datetime.now().strftime("%Y%m%d")
    tommorow = (datetime.now()+timedelta(1)).strftime("%Y%m%d")
    week = create_week_dictionary()
    print(week)
    print(today)
    print(tommorow)
    intent = event['request']['intent']
    print(intent)
    when = intent['slots']['When']['value']

    gabage = ""
    if when == '今日':
        gabage = '燃えるゴミの日です。'
    elif when == '明日':
        gabage = '燃えないゴミの日は水曜日です。'

    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': gabage
            }
        }
    }
    return response


def create_week_dictionary():
    keys = []
    values = []
    for i in range(7):
        keys.append((datetime.now()+timedelta(i)).weekday())
        values.append((datetime.now()+timedelta(i)).strftime("%Y%m%d"))
    return dict(zip(keys, values))
