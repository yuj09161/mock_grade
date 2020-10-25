import random,json

def test_data_gen():
    result=[]
    for num in (45,30,45,20,20,20):
        ans   = tuple(str(random.randint(1,5)) for _ in range(num))
        cor   = tuple(str(random.randint(1,5)) for _ in range(num))
        score = random.randint(1,100)
        result.append((ans,cor,score))
    return result

with open('save.mockdata','w',encoding='utf-8') as file:
    json.dump(test_data_gen(),file,indent=4,ensure_ascii=False)