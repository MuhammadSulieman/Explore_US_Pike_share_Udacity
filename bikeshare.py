import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# month list, six months only and the string "all"
months = ['january', 'february', 'march', 'april', 'may', 'june','all'] 
# day list, seven days and the string "all"
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday','friday','saturday','all'] 

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input("\n Please select the city you like to explore its data. You can select, New York City, Washington, or Chicago:\n").lower() 

     # Validate the the choice of city is as expected
    while city not in CITY_DATA:
            print("\n This is not in our database ! , Invalid input")
            city = input("\n Please select a city by typing one of  New York City, Washington, or   Chicago: \n").lower() 

    month = input("Please select a month from January, February, March, April, May, or June or type'All' for general analysis: \n").lower()
    # Validate the month is selected as expected
    while month not in months:
        print("\n This is not Available ! , Invalid input") 
        month = input("Please select a month from January, February, March, April, May, or June or type'All' for general analysis: \n").lower()
    day = input("\n Please select a day from 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday', or type 'All' for general analysis:\n").lower()
      
      # Validate the day is selected as expected
    while day not in days:
        print("\n This is not week day !") 
        day = input("\n Please select a day from 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','All' for general analysis:\n").lower()
    
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
    filename = (CITY_DATA[city])
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['hour'] = df['Start Time'].dt.hour
    df['week_day'] = df['Start Time'].dt.day_name()
    
    
    if month != 'all' :
        df = df[df['month'] == month.title()]
    if day != "all" :
        df = df[df['week_day'] == day.title()]
     
    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""
    #city, month, day = get_filters()
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #  display the most common month

    if month == 'all' :
        common_month = df['month'].mode()[0]
        print('Most common month:', common_month)
        
    # display the most common day of week    
    if day == "all" : 
        common_day = df['week_day'].mode()[0]
        print('Most common day of week :', common_day)
    
    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    poular_start_station = df['Start Station'].mode()[0]
    print('Most popular Start station:', poular_start_station)
    
    # display most commonly used end station
    poular_end_station = df['End Station'].mode()[0]
    print('Most popular End station:', poular_end_station)
    
    # display most frequent combination of start station and end station trip

    df['trip']=df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('Most popular trip:', popular_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #  display total travel time
    print(" The total trip duration :", df['Trip Duration'].sum())

    #  display mean travel time
    print(" The Average trip duration :", (df['Trip Duration'].sum())/df['Trip Duration'].count())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    
    user_count = df['User Type'].value_counts()
    print('\nUser types:\n', user_count  )
    print('-'*40)
    
    if city == 'washington' :
        print ("\n Sorry! Age and Gender data are not available for washington")
        print('-'*40)
    else :
        
        gender_count = df['Gender'].value_counts()
        print('\n  Gender types:\n', gender_count  )
        print('-'*40)
        earliest_yob = df['Birth Year'].min()
        print('The Earlest YOB :', earliest_yob  )
        most_recent_yob = df['Birth Year'].max()
        print('The most recent YOB :', most_recent_yob  )
        common_yob = df['Birth Year'].mode()[0]
        print('The common YOB :', common_yob  )
        print('-'*40)
        
def display_raw_data(df): 
    """ The fuction works on the city in get_filters fuction and returns the raw data of that city as sets of 5 rows.""" 
    print("\n Raw data are availble to display")
    # set row counnter 
    count_in = 0 
    # taking user option 
    display = input('Would you like to display  5 rows of data  Yes or No:\n').lower
    while display not in ['yes', 'no'] :
        print('This is not a valid option, pleas type  either yes or no')
        display = input('To display 5 rows of data enter Yes or no \n').lower()
    # when user option is yes
    while display == 'yes':
        print(df.iloc[count_in:count_in+5])
        count_in += 5
        display = input('Would you likt to display 5 more rows? yes or no: ').lower()
    # when user option is no
    if display == 'no':
        print('\nExiting...')
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()