from gendiff.formatters import json, plain, stylish


def generate_diff(data1, data2, frmt='stylish'):  
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        in_first = key in data1
        in_second = key in data2

        if in_first and in_second:
            if data1[key] == data2[key]:
                diff.append({
                    "key": key,
                    "status": "unchanged",
                    "value": str(data1[key]).lower(),
                })
            else:
                diff.append({
                    "key": key,
                    "status": "changed",
                    "old_value": str(data1[key]).lower(),
                    "new_value": str(data2[key]).lower(),
                })
        elif in_first and not in_second:
            diff.append({
                "key": key,
                "status": "removed",
                "old_value": str(data1[key]).lower(),
            })
        elif not in_first and in_second:
            diff.append({
                "key": key,
                "status": "added",
                "new_value": str(data2[key]).lower(),
            })
    
    if frmt == 'plain':
        return plain.format(diff)
    elif frmt == 'json':
        return json.format(diff)
    
    return stylish.format(diff)