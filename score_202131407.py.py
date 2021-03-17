data=input('1회차, 2회차, ... 15회차 점수 입력') 
test1=int(input('중간고사 점수'))
test2=int(input('기말고사 점수'))

print(data.split())
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15=map(int,data.split()) #int는 입력값
sam_a=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15

na=sam_a/15
goap=na*0.4
goap2=test1*0.3
goap3=test2*0.3 

score=goap+goap2+goap3
if 100>= score>=90: 
    grade='A'
elif 90>score>=80:
    grade='B'
elif 80>score>=70:
    grade='C'
elif 70>score>=60:
    grade='D'
else:#elif score<60:
    #grade='F'
    grade='F'
    

print('%3d /%3d /%3d /%3d /%3d /%3d /%3d /%3d /%3d /%3d /%3d /%3d /%3d /%3d /%3d /합계 %3d /평균값 %6.2f /비중값 %6.2f '
      %(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, sam_a, na, goap))

print('과제평균(40%):',goap, '중간평균(30%):',goap2, '기말평균(30%):',goap3, '총합 :',goap+goap2+goap3)

print('등급은' ,grade, '입니다.')