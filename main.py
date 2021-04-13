from os import sep
import pandas as pd


def get_data():
    df = pd.read_excel('data.xls')
    return df


def get_column(df=None):
    result = df.keys().tolist()
    result.pop(0)

    return result


def filter_data(df=None, start_date=None, end_date=None, province=None):
    if start_date != None and end_date != None:
        result = df[(df['DATE'] >= str(start_date)) &
                    (df['DATE'] <= str(end_date))]

    if province != None:
        result = result[province]

    return result


def main():
    df = get_data()

    column_get = get_column(df)
    selected_column = ['DATE']

    print()
    print('Data Covid Indonesia by @kawalcovid19\n')
    print('\tList Kota')
    print(*column_get, sep='\t ')
    print()

    selected_column.append('JAKARTA')
    selected_column.append('JABAR')
    selected_column.append('NASIONAL')

    start_date = '2021-01-01'
    end_date = '2021-01-31'
    print()

    print('Total Positif Covid-19')
    result = filter_data(df=df,
                         start_date=start_date,
                         end_date=end_date,
                         province=selected_column)
    print(result.to_string(index=False))
    print()

    print('Rata-Rata')
    print(result.mean())


if __name__ == '__main__':
    main()
