import meanAlgorithm as ma

scores = [8.9, 7.6, 8.2, 9.1, 8.8, 8.1, 7.9, 9.4, 7.2, 8.7]
top5 = [9.12, 8.95, 8.12, 7.90, 7.88]
print(f'top5: {top5}')

total = 0; average = 0
for n in scores:
    total += n

average = round(total / len(scores), 2)

print(f'total: {total}')
print(f'average: {average}')

tp = ma.Top5Players(top5, average)
tp.setAlignScore()
top5 = tp.getFinalTop5()
print(f'top5 :  {top5}')