import random

team_1 = []
team_2 = []

for i in range(0, 20):
    score_1 = round(random.uniform(5, 10), 2)
    score_2 = round(random.uniform(5, 10), 2)
    team_1.append(score_1)
    team_2.append(score_2)

winners = [max(team_1[i], team_2[i]) for i in range(20)]

print("Первая команда: ", team_1)
print("Вторая команда: ", team_2)
print("Победители", winners)