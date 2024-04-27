import datetime

class DataRepository:
    def __init__(self):
        self.data_storage = {}

    def save_data(self, timestamp, data):
        self.data_storage[timestamp] = data

    def get_nearest_data(self, requested_time):
        nearest_time_difference = None
        nearest_time = None

        for timestamp_str in self.data_storage.keys():
            timestamp = datetime.datetime.fromisoformat(timestamp_str)
            time_difference = abs(timestamp - requested_time)
            if nearest_time_difference is None or time_difference < nearest_time_difference:
                nearest_time_difference = time_difference
                nearest_time = timestamp_str

        return self.data_storage[nearest_time]
