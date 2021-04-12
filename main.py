import pandas as pd


def get_data():
    df = pd.read_excel('data.xls')
    return df


def filter_data(df=None, start_date=None, end_date=None, province=None):
    result = df[(df['DATE'] >= str(start_date)) &
                (df['DATE'] <= str(end_date))]

    if province != None:
        result = result[['DATE', f'{province}']]

    return result.to_string(index=False)


df = get_data()

result = filter_data(df=df,
                     start_date='2021-01-01',
                     end_date='2021-01-10',
                     province='DIY')
print(result)
