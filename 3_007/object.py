# 중간고사 클래스와 기말고사 클래스를 상속관계로 만들고 각각의 점수를 초기화 하자.
# 또한 총점 및 평균을 반환하는 기능 구현

class MidExam:
    def __init__(self, s1, s2, s3):
        print('[midExam] __init__() 생성자 호출!')

        self.mid_kor_score = s1
        self.mid_eng_score = s2
        self.mid_math_score = s3

    def printScore(self):
        print(f'mid_kor_score: {self.mid_kor_score}')
        print(f'mid_eng_score: {self.mid_eng_score}')
        print(f'mid_math_score: {self.mid_math_score}')

class EndExam(MidExam):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        print('[endExam] __init__() 생성자 호출!')

        super().__init__(s1, s2, s3)

        self.end_kor_score = s4
        self.end_eng_score = s5
        self.end_math_score = s6

    def printScore(self):
        super().printScore()
        print(f'end_kor_score: {self.end_kor_score}')
        print(f'end_eng_score: {self.end_eng_score}')
        print(f'end_math_score: {self.end_math_score}')

    def getTotalScore(self):
        total = self.mid_kor_score + self.mid_eng_score + self.mid_math_score
        total += self.end_kor_score + self.end_eng_score + self.end_math_score

        return total

    def getAvgScore(self):
        return self.getTotalScore() / 6

exam = EndExam(85, 90, 88, 75, 85, 95)
exam.printScore()

print(f'Total : {exam.getTotalScore()}')
print(f'Average : {round(exam.getAvgScore())}')