def parseData(file):
    f = open(file)
    questions = []
    answers = []
    text = f.read().split(",")
    # get all the questions
    for i in range(56):
        questions.append(text[i])
    # get all the answers
    start = 57
    while start < 112:
        answers.append(text[i])
        start += 1
    print(answers)
    f.close()


if __name__ == '__main__':
    parseData('test.csv')
