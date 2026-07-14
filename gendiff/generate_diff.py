def generate(data1, data2):  
    lines = ['{']  
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    for key in keys:  
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                lines.append(f'    {key}: {data1[key]}')
            else:
                lines.append(f'  - {key}: {data1[key]}')
                lines.append(f'  + {key}: {data2[key]}')
                
        if key in data1 and key not in data2:
            lines.append(f'  - {key}: {data1[key]}')
        
        if key not in data1 and key in data2:
            lines.append(f'  + {key}: {data2[key]}')
    
    lines.append('}')
            
    return '\n'.join(lines)