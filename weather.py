import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):  # 1 DONE!
    """Takes a temperature and returns it in string format with the degrees
        and celsius symbols.
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celsius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

###############################################


def convert_date(iso_string):  # 2 DONE!
    format_date = datetime.fromisoformat(iso_string)
    format_date_iso = format_date.strftime("%A %d %B %Y")
    # print(format_date_iso)
    return format_date_iso
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """


pass

###############################################


def convert_f_to_c(temp_in_farenheit):  # 3 DONE!
    temp_in_celsius = (float(temp_in_farenheit) - 32) * (5 / 9)
    # print(float(temp_in_celsius))
    return round(temp_in_celsius, 1)
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass


###############################################

def calculate_mean(weather_data):  # 4 DONE!
    weather_floats = []
    for item in weather_data:
        if item != float:
            weather_floats.append(float(item))
    mean = sum(weather_floats) / len(weather_floats)
    return mean
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """


pass

###############################################


def load_data_from_csv(csv_file):  # 5 DONE!
    weather_data = []  # Creating an empty list
    with open(csv_file, encoding="utf-8") as csv_file:  # Opening the CSV file
        reader = csv.reader(csv_file)  # Reading the CSV file
        next(reader)  # Skipping the header/first line
        for line in reader:  # For each row in the CSV
            if len(line) > 0:  # If the row is not blank/empty
                # Appending information from the row into the empty list by turning it into a sublist
                weather_data.append([line[0], int(line[1]), int(line[2])])
                # Returning the right type of information - -> min_temp and max_temp to an integer
    # Checking if the list appears correctly according to the test
    # print(weather_data)
    return weather_data  # Giving back the list for python to run

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

###############################################


def find_min(weather_data):  # 6 DONE!
    # If the weather data list is empty, return what is specified as the expected result for this in test_find_min file.
    # If length of weather data is 0, then the function will return an empty variable to satisfy the expected output in test_find_min file.
    if len(weather_data) == 0:
        return ()

    # Setting our starting point for the indexation of the min_temp column, which is column 0.
    min_index = 0
    # Column 0 because that is the column that contains the min values. We also know from the expected outputs that we expect this value to be a float.
    min_temp = float(weather_data[0])

    # inbuilt function that acts as a loop. Efficient as we can avoid having to set up a counter, or use the length of the list to find the min_temp.
    enumerated_weather_data = enumerate(weather_data)

    for data in enumerated_weather_data:
        # This defines clearly that each tuple consists of the index/position at column 0, and the temperature in column 1.
        index, temp = data
        # Converting the temperature value in the tuple to a float before any comparisons to find the min are made.
        # converting the temp value into a     float before comparisons between temp and min_temp are made.
        temp = float(temp)

        if temp <= min_temp:
            min_temp = temp
            min_index = index

    return min_temp, min_index

    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """


pass

###############################################


def find_max(weather_data):  # 7 DONE!
    # If the weather data list is empty, return what is specified as the expected result for this in test_find_max file.
    # If length of weather data is 0, then the function will return an empty variable to satisfy the expected output in test_find_max file.
    if len(weather_data) == 0:
        return ()

    # Setting our starting point for the indexation of the max_temp column, which is column 0.
    max_index = 0
    # Column 0 because that is the column that contains the max values, according to the test_find_max file. We also know from the expected outputs that we expect this value to be a float.
    max_temp = float(weather_data[0])

    # inbuilt function that acts as a loop. Efficient as we can avoid having to set up a counter, or use the length of the list to find the max_temp.
    enumerated_weather_data = enumerate(weather_data)

    for data in enumerated_weather_data:
        # This defines clearly that each tuple consists of the index/position at column 0, and the temperature in column 1.
        index, temp = data
        # Converting the temperature value in the tuple to a float before any comparisons to find the max are made.
        # converting the temp value into a float before comparisons between temp and max_temp are made.
        temp = float(temp)

        if temp >= max_temp:
            max_temp = temp
            max_index = index

    return max_temp, max_index

    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """


pass

###############################################


def generate_summary(weather_data):
    min_temp_list = []
    max_temp_list = []

    for row in weather_data:
        min_temp_list.append(row[1])
        max_temp_list.append(row[2])

    # Day number
    day_number = len(weather_data)

    # # formatted min temp
    min_temp = find_min(min_temp_list)
    formatted_min_temp = convert_f_to_c(min_temp[0])

    # formatted min date
    formatted_min_date = convert_date(weather_data[min_temp[1]][0])

    # formatted max temp
    max_temp = find_max(max_temp_list)
    formatted_max_temp = convert_f_to_c(max_temp[0])

    # formatted max date
    formatted_max_date = convert_date(weather_data[max_temp[1]][0])

    # formatted mean low
    mean_low = calculate_mean(min_temp_list)
    mean_low_c = convert_f_to_c(mean_low)
    formatted_mean_low = format_temperature(mean_low_c)

    # formatted mean high
    mean_high = calculate_mean(max_temp_list)
    mean_high_c = convert_f_to_c(mean_high)
    formatted_mean_high = format_temperature(mean_high_c)

    # Summary breakdown
    first_line = f"{day_number} Day Overview"
    second_line = f"The lowest temperature will be {formatted_min_temp}°C, and will occur on {formatted_min_date}."
    third_line = f"The highest temperature will be {formatted_max_temp}°C, and will occur on {formatted_max_date}."
    fourth_line = f"The average low this week is {formatted_mean_low}."
    fifth_line = f"The average high this week is {formatted_mean_high}."

    # Summary
    summary_data = f"""{first_line}
  {second_line}
  {third_line}
  {fourth_line}
  {fifth_line}
"""

    return summary_data
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """


pass


def generate_daily_summary(weather_data):
    summary = ""
    daily_summary = []
    for item in weather_data:
        formatted_date = convert_date(item[0])
        min_temp_c = convert_f_to_c(item[1])
        formatted_min_temp = format_temperature(min_temp_c)
        max_temp_c = convert_f_to_c(item[2])
        formatted_max_temp = format_temperature(max_temp_c)
        daily_summary.append(
            [formatted_date, formatted_min_temp, formatted_max_temp])

    for day in daily_summary:
        date = day[0]
        ind_min = day[1]
        ind_max = day[2]

        summary += f"""---- {date} ----
  Minimum Temperature: {ind_min}
  Maximum Temperature: {ind_max}

"""

    return summary
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
