import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.findall(r"[a-z0-9-_. ]",new_id)
    new_id = ''.join(new_id)
    new_id = re.sub('[.]+','.',new_id)
    new_id = re.sub('^[.]','',new_id)
    if new_id == '':
        new_id = 'a'
    new_id = re.sub('[.]$','',new_id)
    new_id = re.sub('\s','a',new_id)

    if len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = re.sub('[.]$','',new_id)

    if len(new_id) <= 2:
        new_id = new_id.ljust(3,new_id[-1])
     

    answer = ''.join(new_id)
    return answer