# for문과 if문을 이용해서 과락 과목 출력.
minScore = 60
scores = [
    ['국어', 58],
    ['영어', 77],
    ['수학', 89],
    ['과학', 99],
    ['사회', 50]
]

for subject, score in scores:
    if score < minScore:
        print('과락 과목 : {}, 점수 : {}'.format(subject, score))