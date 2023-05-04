import printScore

scores = []

kor = int(input('korScore : '))
scores.append(kor)
eng = int(input('engScore : '))
scores.append(eng)
mth = int(input('mthScore : '))
scores.append(mth)
sci = int(input('sciScore : '))
scores.append(sci)
his = int(input('hisScore : '))
scores.append(his)

totalScore = sum(scores)
print(f'total score : {totalScore}')

avgScore = totalScore / len(scores)
print(f'avg score : {avgScore}')

grade = printScore.getNearNum(avgScore)
print(f'grade : {grade}')
