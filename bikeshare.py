import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=''
    while city not in ('new york city', 'chicago', 'washington'):
      city = input("\ninput one from cities (chicago, new york city, washington)\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month=''
    while month not in ('january','february','march','april','may','june','all'):
      month = input("\ninput one from monthes (all, january, february, ... , june)\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =''
    while day  not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
      day  = input("\ninput one from days of week (all, monday, tuesday, ... sunday)\n").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popularMonth = df['month'].mode()[0]
    print('the most common month: ', popularMonth)
    # TO DO: display the most common day of week
    popularDay = df['day_of_week'].mode()[0]
    print('the most common day of week: ', popularDay)

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    popularHour = df['hour'].mode()[0]
    print('the most common start hour: ', popularHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    column = df["Start Station"]
    values = column.value_counts()
    maximumIndexStart=values.idxmax()
    print('most commonly used start station : ',maximumIndexStart)
    # TO DO: display most commonly used end station
    column = df["End Station"]
    values = column.value_counts()
    maximumIndexEnd=values.idxmax()
    print('most commonly used end station : ',maximumIndexEnd)
    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time :',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time :',df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].value_counts()
    print('counts of user types:\n',users)
    print()
    print()
    # TO DO: Display counts of gender
    if (city!='washington'): 
        gender = df['Gender'].value_counts()
        print('counts of gender:\n', gender)
        print()
        print()
        # TO DO: Display earliest, most recent, and most common year of birth
        maxRecent = df['Birth Year'].max()
        print('most recent of birth:', maxRecent)
        print('most common year of birth: ', df['Birth Year'].value_counts().idxmax())

        print('earliest year of birth: ', df['Birth Year'].min())

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

