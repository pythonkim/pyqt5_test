aa = {}
print(aa)
aa.update({'code':{}})
print(aa)
aa['ddd'] = {}

aa['cad'] = "김회진"
aa['aac'] = "이정희"
print(aa)

if 'code' in aa: #키만 비교가 되는구나
    print("key도 검색이 되네")
if '김회진' in aa.values(): #이렇게 하면 모든 value를 가져오나 보나다
    print("value 도 검색됨")
if "이정희" in aa.values():
    print('이정희 만세')
else:
    print("검색은 개뿔")