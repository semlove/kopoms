str_input = input("태어난 해를 입력해 주세요 > ")
birth_year = int(str_input) % 12
tti = ["원숭이", "달", "개", "돼지",
      "쥐", "소", "범", "토끼",
      "용", "뱀", "말", "양"]
print(tti[birth_year], "띠입니다.")
