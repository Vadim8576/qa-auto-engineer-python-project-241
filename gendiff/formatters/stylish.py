def format(diff):
    lines = ['{']

    for item in diff:
        key = item['key']
        status = item['status']

        if status == 'unchanged':
            lines.append(f'    {key}: {item['value']}')

        elif status == 'changed':
            
            lines.append(f'  - {key}: {item['old_value']}')
            lines.append(f'  + {key}: {item['new_value']}')

        elif status == 'removed':
            lines.append(f'  - {key}: {item['old_value']}')

        elif status == 'added':
            lines.append(f'  + {key}: {item['new_value']}')

    lines.append('}')
    return '\n'.join(lines)

    