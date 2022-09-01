#입력의 첫 번째 줄은 속도 제한입니다.
#두 번째 입력 라인은 자동차의 기록된 속도입니다.

#출력
#운전자가 과속하지 않는 경우 출력은 다음과 같아야 합니다.
#Congratulations, you are within the speed limit!

#운전자가 과속하면 출력은 다음과 같아야 합니다.
#You are speeding and your fine is $F.

#여기서 F는 위의 표에 설명된 벌금 액수입니다.

# 1 ~ 20	$100
# 21 ~ 30	$270
# 31 이상	$500

limit = int(input())
speed = int(input())
over = speed - limit

if over >= 31 : print("You are speeding and your fine is $500.")
elif over >= 21 : print("You are speeding and your fine is $270.")
elif over >= 1 : print("You are speeding and your fine is $100.")
else : print("Congratulations, you are within the speed limit!")