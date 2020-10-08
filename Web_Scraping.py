import requests
for k in range(50):
    res = requests.get('http://3.95.249.159:8000/random_company')
    allres = res.text
    sentence = allres.split('\n')

    for i in sentence:
        if 'Name:' in i:
            n = i
            n = n[16:-5]
            print(k, n)
        if 'Purpose' in i:
            allpur = i
            allpur = allpur[16:-5]
            print(k, allpur)