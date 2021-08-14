import time

import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago', 'new york city', 'washington']
    city = input("Please enter the city: ").lower()
    while city not in cities:
        print('invalid input, Please retry')
        city = input('Ex.chicago, new york city, washington,... \nEnter the city:').lower()
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = input('Enter Day:').lower()
    while day not in days:
        print('invalid input, Please retry')
        day = input('Enter Day:').lower()
    months = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
    month = input('Enter month "As Number":')
    while month not in months:
        print('invalid input, Please retry')
        month = input('Enter month:')
    return city, int(month), day


print('-' * 40)


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day'] = df['Start Time'].dt.day_name()

    df['hour'] = df['Start Time'].dt.hour

    df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('Most Popular Start Hour:', df['hour'].mode()[:1])
    print('-' * 5)
    print('Most Popular Start Day:', df['day'].mode()[:1])
    print('-' * 5)
    print('Most Popular Start month:', df['month'].mode()[:1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('most commonly used start station:', df['Start Station'].mode()[:1])
    print('-' * 5)
    print('most commonly used end station:', df['End Station'].mode()[:1])
    print('-' * 5)
    df['trip'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    print('most common trip:', df['trip'].mode()[:1])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('total travel time: ', df['Trip Duration'].sum())
    print('-' * 5)
    print('mean travel time: ', df['Trip Duration'].mean())
    print('-' * 5)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on Bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('User Type:\n', df['User Type'].value_counts())
    print('-' * 5)
    if 'Gender' in df.columns:
        print('Gender:\n', df['Gender'].value_counts())
    else:
        print('Gender: '+'Data is not available')
    print('-' * 5)
    if 'Birth Year' in df.columns:
        print('Earliest year of birth:', df['Birth Year'].min())
        print('Most recent year of birth:', df['Birth Year'].max())
        print('Most common year of birth:', df['Birth Year'].mode()[:1])
    else:
        print('Birth Year: '+'Data is not available')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def view_data(df):
    data_view = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while data_view == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        data_view = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
