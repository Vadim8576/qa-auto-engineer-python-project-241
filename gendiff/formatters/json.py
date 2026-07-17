import json


def format(diff):
    result = {}

    for item in diff:
        key = item['key']
        status = item['status']

        if status == 'unchanged':
            result[key] = item['value']

        elif status == 'changed':
            # Для changed можно хранить и старое, и новое значение
            result[key] = {
                'old_value': item['old_value'],
                'new_value': item['new_value'],
                'status': 'changed'
            }

        elif status == 'removed':
            result[key] = {
                'old_value': item['old_value'],
                'status': 'removed'
            }

        elif status == 'added':
            result[key] = {
                'new_value': item['new_value'],
                'status': 'added'
            }

    return json.dumps(result, indent=2, ensure_ascii=False)
