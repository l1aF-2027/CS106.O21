import os


directory = r'D:\Asus\Trí tuệ nhân tạo - CS106\BT4\Test\multiagent\layouts'

files = os.listdir(directory)

for i in range(len(files)):
    files[i] = os.path.splitext(files[i])[0]
    files[i] = '-l ' + files[i]

agent = ['-p MinimaxAgent', '-p AlphaBetaAgent', '-p ExpectimaxAgent']
evaluation = [',evalFn=scoreEvaluationFunction', ',evalFn=betterEvaluationFunction']
randomseed = ['-s 22520460', '-s 22520461', '-s 22520462', '-s 22520463', '-s 22520464']
for file in files:
    depth = ' -a depth=3'
    if file == files[4]:
        evaluation = [',evalFn=scoreEvaluationFunction']
    if file == files[10] or file == files[5] or file == files[4]:
        depth = ' -a depth=2'
    for ag in agent:
        for ev in evaluation:
            for rs in randomseed:
                temp = 'python pacman.py ' + file +     ' ' + ag + depth + ev + ' ' + rs + ' -q'
                print(temp)
                os.system(temp)
                print('-'*30)

