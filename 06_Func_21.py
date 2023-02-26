solution = input()
def read_answers() :
    N = int(input())
    answers = []
    for k in range(N):
        sid, ans = input().split()
        answers.append([sid, ans])
    return answers

def marking(answer, solution) :
    score = 0
    for i in range(len(answer)) :
        if answer[i] == solution[i] :
            score += 1
    return score

def grading(score):
    g = [[80,"A"], [70,"B"],[60,"C"], [50,"D"]]
    for a,b in g:
        if score >= a :
            return b
    return "F"

def scoring(answers, solution) :
    scores = []
    for sid, ans in answers :
        score = marking(ans, solution) / len(solution) * 100
        grade = grading(score)
        scores.append([sid, score, grade])
    return scores
    
def report(scores) :
    for sid,sc,grade in scores[::-1] :
        print(sid, sc, grade)

def sort(scores) :
    x = []
    for sid,score,grade in scores :
        x.append([score, sid, grade])
    x.sort()
    for i in range(len(x)) :
         scores[i] = [x[i][1], x[i][0], x[i][2]]
    scores = scores[::-1]
    for i in range(len(scores)-1) :
        if scores[i][1] == scores[i+1][1] :
            if scores[i][0] < scores[i+1][0] :
                scores[i],scores[i+1] = scores[i+1],scores[i]
x = read_answers()
scores = scoring(x, solution)
score = marking(x, solution)
grading(score)
sort(scores)
report(scores)