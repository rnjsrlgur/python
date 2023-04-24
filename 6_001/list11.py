# enumerate() 함수

sports = ['야구', '축구', '농구', '테니스', '마라톤']

for i in range(len(sports)):
    print('{} : {}'.format(i, sports[i]))

for idx, val in enumerate(sports):
    print('{} : {}'.format(idx, val))