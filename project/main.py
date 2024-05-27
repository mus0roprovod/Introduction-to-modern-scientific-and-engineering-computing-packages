import ephem
import pandas as pd
from helpers import *
from datetime import datetime, timedelta

# # Начальная и конечная даты для поиска новолуний и полнолуний
# start_date = datetime(2023, 1, 1)
# end_date = datetime(2024, 1, 1)
# # Функции для вычисления дат новолуния и полнолуния после заданной даты
# # Получение векторов дат полнолуний, которые сопоставлены с новолунием
# moon_dates = get_full_to_new_moons(start_date, end_date)
# end_date = datetime.strptime(moon_dates[next(reversed(moon_dates))], "%Y-%m-%d")
# print(end_date)
# start_date = start_date.strftime("%Y-%m-%d")
# end_date = datetime.strptime(moon_dates[next(reversed(moon_dates))], "%Y-%m-%d")
# end_date = end_date.strftime("%Y-%m-%d")
# ans = get_distribution_by_moon_phase(start_date, end_date, moon_dates)
# print(ans)
# ans.to_json('/home/musoroprovod/pakets_projects/pythonProject1/out.json', orient='records', lines=True)
# ans.drop_duplicates(subset='TICKER', keep='first')
# unique_dates_in_df = pd.Series(ans['TICKER'].unique())
# unique_db_by_date = ans.drop_duplicates(subset='TICKER', keep='first')
# df_sorted = ans.sort_values(by='average_price_moon', ascending=False)
# top5_tickets_from_top = df_sorted.head(10)
# df_sorted = ans.sort_values(by='average_price_moon', ascending=True)
# top5_cheap_tickets = df_sorted.head(10)
# print(top5_tickets_from_top)
# print()
# print(top5_cheap_tickets)
halloween = datetime(2023, 10, 31)
start_day_spring = datetime(2024, 4, 28)
end_day_spring = datetime(2024, 5, 10)

start_day_spring = start_day_spring.strftime("%Y-%m-%d")
end_day_spring = end_day_spring.strftime("%Y-%m-%d")
halloween = halloween.strftime("%Y-%m-%d")

best_company = ['TRNFP', 'KOGK', 'RU000A1034U7', 'RU000A102N77', 'RKKE']
worst_company = ['VSMO', 'MGNT', 'FIVE', 'LKOH', 'AGRO']

res = get_distribution_by_halloween(start_day_spring, end_day_spring, halloween, best_company)
res = get_distribution_by_halloween(start_day_spring, end_day_spring, halloween, worst_company)
res = res.sort_values(by='diff', ascending=False)
the_best = res.head(10)
res = res.sort_values(by='diff', ascending=True)
the_worst = res.head(10)
