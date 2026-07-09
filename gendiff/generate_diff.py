import json


def generate_diff(file_path1, file_path2):
    json1 = json.load(open(file_path1))
    json2 = json.load(open(file_path2))
    
    lines = ['{']
    
    keys = sorted(json1.keys() | json2.keys())
    
    
    for key in keys:  
        if key in json1 and key in json2:
            if json1[key] == json2[key]:
                lines.append(f'    {key}: {json1[key]}')
            else:
                lines.append(f'  - {key}: {json1[key]}')
                lines.append(f'  + {key}: {json2[key]}')
                
        if key in json1 and key not in json2:
            lines.append(f'  - {key}: {json1[key]}')
        
        if key not in json1 and key in json2:
            lines.append(f'  + {key}: {json2[key]}')
    
    lines.append('}')
    
    # for item in lines:
    #     print(item)
        
    
    return '\n'.join(lines)