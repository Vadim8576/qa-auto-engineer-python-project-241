def format(diff):
    lines = []

    for item in diff:
        key = item['key']
        status = item['status']

        if status == 'removed':
            old_value = item['old_value']
            lines.append(f"Property '{key}' was removed")
            
        elif status == 'added':
            value = item.get('value', item.get('new_value'))       
            lines.append(f"Property '{key}' was added with value: {value}")

        elif status == 'changed':
            old_value = item['old_value']
            new_value = item['new_value']
            lines.append(
                f"Property '{key}' was updated. From {old_value} to {new_value}"
            )

    return "\n".join(lines)

