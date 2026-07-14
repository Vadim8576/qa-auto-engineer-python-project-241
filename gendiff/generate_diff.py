def generate(data1, data2):  
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
                    "value": data1[key],
                })
            else:
                diff.append({
                    "key": key,
                    "status": "changed",
                    "old_value": data1[key],
                    "new_value": data2[key],
                })
        elif in_first and not in_second:
            diff.append({
                "key": key,
                "status": "removed",
                "old_value": data1[key],
            })
        elif not in_first and in_second:
            diff.append({
                "key": key,
                "status": "added",
                "new_value": data2[key],
            })

    return diff