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
    list_1 = []
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
    min_value = float('inf')
    max_index = -1
    if len(weather_data) > 0:
        for i in range(len(weather_data)):
            num = float(weather_data[i])
            if num <= min_value:
                min_value = num
                max_index = i
        return min_value, max_index
    else:
        return ()

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    max_value = float('-inf')
    max_index = -1
    if len(weather_data) > 0:
        for i in range(len(weather_data)):
            num = float(weather_data[i])
            if num >= max_value:
                max_value = num
                max_index = i
        return max_value, max_index
    else:
        return ()

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summaries = ""
    if len(weather_data) > 0:
        overview = f"{len(weather_data)}"
        num_days = len(weather_data)
        min_temp, min_index = find_min([day[1] for day in weather_data])
        max_temp, max_index = find_max([day[2] for day in weather_data])
        average_low = calculate_mean(day[1] for day in weather_data)
        average_high = calculate_mean(day[2] for day in weather_data)
        min_day = convert_date(weather_data[min_index][0])
        max_day = convert_date(weather_data[max_index][0])
        daily_summaries += f"{overview} Day Overview\n"
        daily_summaries += f"  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp))}, and will occur on {min_day}.\n"
        daily_summaries += f"  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {max_day}.\n"
        daily_summaries += f"  The average low this week is {format_temperature(convert_f_to_c(average_low))}.\n"
        daily_summaries += f"  The average high this week is {format_temperature(convert_f_to_c(average_high))}.\n"
        return daily_summaries

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summaries = ""
    for day in weather_data:
        date = "---- " + convert_date(day[0]) + " ----"
        min_temp = format_temperature(convert_f_to_c(day[1]))
        max_temp = format_temperature(convert_f_to_c(day[2]))
        summary = f"{date}\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"
        daily_summaries += summary
    return daily_summaries
