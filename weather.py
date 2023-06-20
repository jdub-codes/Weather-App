import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):

    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """    

    date_obj = datetime.fromisoformat(iso_string)
    return date_obj.strftime("%A %d %B %Y")

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing the temperature in degrees Celsius, rounded to 1 decimal place.
    """

    celsius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    return round(celsius, 1)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass

    weather_data_sum = []
    for num in weather_data:
        weather_data_sum.append(float(num))
    
    mean = sum(weather_data_sum) / len(weather_data_sum)
    return float(mean)

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(file=csv_file, mode="r", encoding="utf-8") as my_file:
        csv_reader = csv.reader(my_file, delimiter = ",")
        csv_reader.__next__()
        for row in csv_reader:
                if len(row) > 0:
                    row[1] = int(row[1])
                    row[2] = int(row[2])
                    list_1.append(row)
    return list_1

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    # minimum = min(weather_data)
    # position = weather_data.index(minimum)
    # return minimum, position

    weather_data_min = []
    if len(weather_data) > 0:   
        for num in weather_data:
            weather_data_min.append(float(num))
        minimum = min(weather_data_min)
        # for num in weather_data:
        #     if num == minimum:
        position = weather_data.index(minimum)
        # print(position)
        # print(weather_data_min)
        # print(minimum)
        return minimum, position
    else:
        return ()

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass

    maximum = max(weather_data)
    position = weather_data.index(maximum)
    return maximum, position

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

    num_days = len(weather_data)
    average_temp = sum(day[1] for day in weather_data) / num_days
    min_temp = min(day[1] for day in weather_data)
    max_temp = max(day[1] for day in weather_data)
    summary = f"Weather Summary:\nNumber of days: {num_days}\nAverage temperature: {average_temp:.2f}°C\nMinimum temperature: {min_temp}°C\nMaximum temperature: {max_temp}°C"
    return summary

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

    daily_summaries = []
    for day in weather_data:
        date = day[0]
        temperature = day[1]
        summary = f"Date: {date}\nTemperature: {temperature}°C"
        daily_summaries.append(summary)
    return "\n\n".join(daily_summaries)