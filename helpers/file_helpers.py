from typing import List


def get_file_paths(patterns: List[str], base_url: str = None):
    import glob
    new_patterns = patterns
    if(base_url != None):
        new_patterns = list(
                        map(
                            lambda x: '{}/{}'.format(base_url, x),
                            patterns
                        )
                    )
    response = []
    for pattern in new_patterns:
        response = response + glob.glob(pattern)
    return response

def search_pattern_in_file(pattern: str, file_path: str):
    import re
    response = []
    with open(file_path, 'r', encoding='utf-8') as t:
        content_per_line = t.read().split('\n')
    line_index = 1
    for line in content_per_line:
        finds = re.findall(pattern, line)
        if(len(finds) > 0):
            new_line = line
            for find in finds:
                response.append({
                    'line': line_index,
                    'col': new_line.index(find) + 1,
                    'find': find
                })
                new_line = new_line.replace(find,'~'*len(find),1)
        line_index+=1
    return response
    

    
