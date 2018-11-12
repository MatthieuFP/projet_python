from src.support.relative_path import get_relative_path

# PATHS
Root_path = get_relative_path()

Root_data = Root_path + r"\data"
Path_train = Root_data + r"\train.csv"
Path_test = Root_data + r"\test.csv"
Root_graphs = "graphs"

# DF COLUMNS
# Original Columns
Key = 'key'
Fare_amount = 'fare_amount'
Pickup_datetime = 'pickup_datetime'
Pickup_longitude = 'pickup_longitude'
Pickup_latitude = 'pickup_latitude'
Dropoff_longitude = 'dropoff_longitude'
Dropoff_latitude = 'dropoff_latitude'
Passenger_count = 'passenger_count'

# Added Columns
Date = 'Date'
Time = 'Time'
Week_day = 'week_day'
Distance = "distance"
Outlier = 'Outlier'
Month = 'month'
