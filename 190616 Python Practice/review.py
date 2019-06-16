#딕셔너리 복습
student_info = {20140012:'Sungchul', 20140059:'Jiyong', 20140058:'JaeHong'}
student_info[20140012]
print(student_info[20140012]) #값의 키를 대괄호로 묶어 호출한다.

#재할당
student_info[20140012] = 'Janhyeok' #20140012에 해당하는 값을 바꿔줌
print(student_info[20140012]) #20140012에 해당하는 값을 출력해준다
print(student_info) #stutdent_info라는 딕셔너리를 전부 다 출력한다

student_info[20140039] = 'Wonchul' #원철을 추가함
print(student_info)

#딕셔너리의 함수
country_code={}
country_code={"America" : 1, "Korea" : 82, "China" : 86, "Japan" : 81}
print(country_code)

country_code.keys() #키 값만 출력

country_code["German"] = 49 #딕셔너리 추가
print(country_code)
country_code.values() #딕셔너리 키 값만 출력 values
country_code.items() #딕셔너리 키-값 쌍을 모두 보여줌 items

#실제로 딕셔너리를 사용할때는 for문과 함께
for k, v in country_code.items():
    print("Key:", k)
    print("Value:", v)