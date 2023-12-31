from averageTemperature.avgtemp import avg_year_city


def test_avg_year_city_1():
    assert avg_year_city(r'C:\Users\User\python for data analysis\q\python_tools\averageTemperature\data\test_data_1.csv','dt', 'Moscow', 2020) == 3.445

def test_avg_year_city_2():
    assert avg_year_city(r'C:\Users\User\python for data analysis\q\python_tools\averageTemperature\data\test_data_1.csv', 'dt', 'Saint-Petersburg', 2023) == 0.545

def test_avg_year_city_3():
    assert avg_year_city(r'C:\Users\User\python for data analysis\q\python_tools\averageTemperature\data\test_data_2.csv', 'dt', 'Moscow', 2020) == 0.875

def test_avg_year_city_4():
    assert avg_year_city(r'C:\Users\User\python for data analysis\q\python_tools\averageTemperature\data\test_data_2.csv', 'dt', 'Saint-Petersburg', 2023) == 3.45
