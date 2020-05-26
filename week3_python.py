

# function make_card(image){
#     console.log(image);
# }

def make_card(image):
#파이썬은 들여쓰기를 강제한다! 대신 {} 쓰지 않는다
print(image)

make_card('hello')

#조건문
def oddeven(num):
if num % 2 == 0: #if 다음에 () 없음 : 들여쓰기로 구분
return True
else:
return False

print(oddeven(10))

#반복문
fruits = ['사과', '배', '감', '귤']

# 자바스크립트 스타일
# for(let i = 0; i< fruits.length; i++){
#     console.log(fruits[i]);
# }

for fruit in fruits: #fruits에서 하나씩 꺼내다가 fruits에 저장해서 쓴다
print(fruit)


#응용
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:
if fruit == 사과:
count+=1

print(count)
# 사과의 갯수를 세어 보여줍니다.



people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

def get_age(myname):
#myname에 들어온 이름의 나이를 출력하는 함수
for person in people:
    if person['name'] == myname:
    return person['age']
return '해당하는 이름이 없습니다'

print(get_age('bob'))
print(get_age('carry'))