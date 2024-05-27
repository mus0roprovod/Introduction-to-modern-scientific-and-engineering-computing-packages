import ephem
import pandas as pd
import requests
import statistics
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_full_to_new_moons(start_date, end_date):
    full_moons = []
    while start_date <= end_date:
        full_moon = ephem.next_full_moon(start_date)
        full_moon_date = ephem.localtime(full_moon)
        formatted_date = full_moon_date.strftime('%Y-%m-%d')
        if full_moon_date > end_date:
            break
        full_moons.append(formatted_date)
        start_date = full_moon_date + timedelta(days=1)

        # Сопоставляем каждое полнолуние со следующим новолунием
    full_to_new_moons = {}
    for full_moon in full_moons:
        next_new_moon = ephem.next_new_moon(full_moon)
        next_new_moon_date = ephem.localtime(next_new_moon).date()
        formatted_date = next_new_moon_date.strftime('%Y-%m-%d')
        full_to_new_moons[full_moon] = formatted_date
    return full_to_new_moons

def get_dataset_by_ticker(ticker, start_date, end_date):
    base_url = f'https://iss.moex.com/iss/history/engines/stock/markets/shares/securities/{ticker}.json'

    # Параметры запроса
    params = {
        'from': start_date,
        'till': end_date,
        'start': 0
    }

    all_data = pd.DataFrame()

    while True:
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print('Failed to retrieve data')
            break

        data = response.json()
        history_data = data['history']['data']
        df = pd.DataFrame(history_data)

        if not history_data:
            break

        # Добавляем данные в общий контейнер
        all_data = pd.concat([all_data, df], ignore_index=True)

        # Обновляем параметр start для следующего запроса
        params['start'] += len(history_data)


    return all_data

def get_distribution_by_moon_phase(start_date, end_date,  moon_periods):
    response = requests.get('https://iss.moex.com/iss/engines/stock/markets/shares/securities.json')
    data = response.json()
    securities_df = pd.DataFrame(data['securities']['data'], columns=data['securities']['columns'])
    tickers = securities_df['SECID']
    result = pd.DataFrame(columns=['TICKER','average_price_moon'])
    # преобразуем мун пириод в один список
    all_dates = list(moon_periods.keys()) + list(moon_periods.values())
    all_dates = pd.to_datetime(all_dates)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    for ticker in tickers:
        df = get_dataset_by_ticker(ticker, start_date, end_date)
        if len(df) < 8:
            continue
        df['dates'] = pd.to_datetime(df.iloc[:, 1])
        unique_dates_in_df = pd.Series(df['dates'].unique())
        unique_db_by_date = df.drop_duplicates(subset='dates', keep='first')
        dates_in_both = unique_dates_in_df[unique_dates_in_df.isin(all_dates)]
        filtered_df = unique_db_by_date[unique_db_by_date['dates'].isin(dates_in_both)].copy()
        for key, value in moon_periods.items():
            if not (unique_db_by_date['dates'].isin([key]).any() and unique_db_by_date['dates'].isin([value]).any()):
                filtered_df = filtered_df[~filtered_df['dates'].isin([key, value])]
        if filtered_df[7].isnull().any() or filtered_df[7].empty:
            continue
        price_diff = filtered_df[7][::2].values - filtered_df[7][1::2].values
        average = statistics.mean(price_diff)
        new_record = pd.Series([ticker, average], index=result.columns)
        result.loc[len(result)] = new_record
    return result

def get_distribution_by_halloween(start_date, end_date,  halloween):
    response = requests.get('https://iss.moex.com/iss/engines/stock/markets/shares/securities.json')
    data = response.json()
    securities_df = pd.DataFrame(data['securities']['data'], columns=data['securities']['columns'])
    tickers = securities_df['SECID']
    result = pd.DataFrame(columns=['TICKER', 'halloween_price', 'spring_price'])
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    all_dates = list(start_date) + list(end_date)

    for ticker in tickers:
        df = get_dataset_by_ticker(ticker, halloween, end_date)
        if len(df) < 8:
            continue
        df['dates'] = pd.to_datetime(df.iloc[:, 1])
        df['price'] = df.iloc[:, 7]
        unique_dates_in_df = pd.Series(df['dates'].unique())
        unique_db_by_date = df.drop_duplicates(subset='dates', keep='first')
        if not df.loc[df['dates'] == halloween, 'price'].empty:
            price = df.loc[df['dates'] == halloween, 'price'].values[0]
        else:
            continue  # или какое-то другое действие в случае отсутствия данных
        # узнаем сринг  avarege
        mask = (df['dates'] >= start_date) & (df['dates'] <= end_date)
        filtered_df = df.loc[mask]
        average_price = filtered_df['price'].mean()

        if filtered_df['price'].isnull().any() or filtered_df['price'].empty:
            continue

        new_record = pd.Series([ticker, price, average_price], index=result.columns)
        result.loc[len(result)] = new_record
        print(filtered_df)
        # price_diff = filtered_df[7][::2].values - filtered_df[7][1::2].values
        # average = statistics.mean(price_diff)
        # new_record = pd.Series([ticker, average], index=result.columns)
        # result.loc[len(result)] = new_record

    result['diff'] = result['spring_price'] - result['halloween_price']
    return result


def get_distribution_by_halloween(start_date, end_date,  halloween, tickers):

    result = pd.DataFrame(columns=['TICKER', 'halloween_price', 'spring_price'])
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    for ticker in tickers:
        df = get_dataset_by_ticker(ticker, halloween, end_date)
        if len(df) < 8:
            continue
        df['dates'] = pd.to_datetime(df.iloc[:, 1])
        df['price'] = df.iloc[:, 7]
        # узали в хеллуин
        if not df.loc[df['dates'] == halloween, 'price'].empty:
            price = df.loc[df['dates'] == halloween, 'price'].values[0]
        else:
            continue  # или какое-то другое действие в случае отсутствия данных
        # узнаем сринг  avarege
        mask = (df['dates'] >= start_date) & (df['dates'] <= end_date)
        filtered_df = df.loc[mask]
        average_price = filtered_df['price'].mean()

        if filtered_df['price'].isnull().any() or filtered_df['price'].empty:
            continue

        new_record = pd.Series([ticker, price, average_price], index=result.columns)
        result.loc[len(result)] = new_record
        # price_diff = filtered_df[7][::2].values - filtered_df[7][1::2].values
        # average = statistics.mean(price_diff)
        # new_record = pd.Series([ticker, average], index=result.columns)
        # result.loc[len(result)] = new_record

    result['diff'] = result['spring_price'] - result['halloween_price']
    return result
def get_moex_data(ticker, start_date, end_date):
    url = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/securities/{ticker}.json"
    params = {
        'from': start_date,
        'till': end_date,
        'start': 0,
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Извлечение данных из ответа
    columns = data['history']['columns']
    rows = data['history']['data']
    df = pd.DataFrame(rows, columns=columns)

    # Преобразование данных
    df['TRADEDATE'] = pd.to_datetime(df['TRADEDATE'])
    df.set_index('TRADEDATE', inplace=True)

    return df

def plot_top_tickers(start_date, end_date, tickers, halloween_day, start_spring_day, end_spring_day):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    halloween_day = pd.to_datetime(halloween_day)
    start_spring_day = pd.to_datetime(start_spring_day)
    end_spring_day = pd.to_datetime(end_spring_day)

    for ticker in tickers:
        # Получение данных
        df = get_moex_data(ticker, start_date, end_date)

        # Создание нового окна для графика
        plt.figure(figsize=(10, 5))
        plt.plot(df.index, df['CLOSE'], label=f'{ticker} Closing Price')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f'{ticker} Stock Prices')
        plt.legend()
        plt.grid(True)

        # Линия и точка для Halloween
        plt.axvline(halloween_day, color='blue', linestyle='--', linewidth=1)
        closest_halloween_date = df.index[np.abs(df.index - halloween_day).argmin()]
        plt.scatter(closest_halloween_date, df.loc[closest_halloween_date, 'CLOSE'], color='red', zorder=5)

        # Линии для весеннего периода
        plt.axvline(start_spring_day, color='red', linestyle='--', linewidth=1)
        plt.axvline(end_spring_day, color='red', linestyle='--', linewidth=1)

        plt.show()







