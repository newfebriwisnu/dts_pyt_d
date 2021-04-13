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

    return result.to_string(index=False)


def main():
    df = get_data()

    column_get = get_column(df)
    selected_column = ['DATE']

    print()
    print('Data Covid Indonesia by @kawalcovid19\n')
    print('\tList Kota')
    print(*column_get, sep='\t ')
    print()

    total_kota = int(input('Total Kota: '))
    for x in range(0, total_kota):
        selected_column.append(input(f'Kota {x+1}: ').upper())
    print()

    start_date = input('Start Date (YYYY-MM-DD): ')
    end_date = input('End Date (YYYY-MM-DD): ')
    print()

    result = filter_data(df=df,
                         start_date=start_date,
                         end_date=end_date,
                         province=selected_column)

    print(result)


if __name__ == '__main__':
    main()
