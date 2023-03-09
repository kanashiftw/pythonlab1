import random
import itertools
import datetime

teams = {'Хакасия', 'Оренбургская область', 'Краснодарский край', 'Башкортостан', 'Татарстан',
         'ДНР', 'Ростовская область', 'Тыва', 'Северная Осетия', 'Свердловская область',
         'Чувашия', 'Якутия', 'Пермский край', 'Сахалинская область', 'Белгородская область', 'Крым'}
groups = {'group_A': set(), 'group_B': set(), 'group_C': set(), 'group_D': set()}
for group in groups.keys():
    groups[group] = set(random.sample(teams, 4))
    teams = set.difference(teams, groups[group])
print(groups)
del(teams)
games = {'group_A': list(itertools.combinations(groups['group_A'], 2)),
         'group_B': list(itertools.combinations(groups['group_B'], 2)),
         'group_C': list(itertools.combinations(groups['group_C'], 2)),
         'group_D': list(itertools.combinations(groups['group_D'], 2))}
game_date = datetime.datetime(2022, 9, 14, 22, 45)
delta = datetime.timedelta(days=14)
for i in range(6):
    for key in games:
        date = '{0:02d}/{1:02d}/{2} {3}:{4}'.format(game_date.day, game_date.month, game_date.year, game_date.hour, game_date.minute)
        print('{0}\tvs\t{1}, {2}'.format(games[key][i][0], games[key][i][1], date))
    game_date = game_date + delta
