'''
the entity file incorporates the classes of Rider and Driver
property begin with _ denotes it is a private attribute
'''
import random
import pandas as pd
import numpy as np


'''
b'REGULAR'    689869    0
b'SUV'         25346    1
b'PREMIUM'      6357    2
b'LUXURY'       2376    3
'''

model_type_dict = {''}

# a tuple (latitude, longitude) for origin and destination
class Rider:
    def __init__(self, rider_id, rider_origin, rider_destination, rider_earliest_departure_time,
                 rider_latest_departure_time, rider_request_model_type):
        self._rider_id = rider_id
        self._rider_origin = rider_origin
        self._rider_destination = rider_destination
        self._rider_earliest_departure_time = rider_earliest_departure_time
        self._rider_latest_departure_time = rider_latest_departure_time
        self._rider_request_model_type = rider_request_model_type
        self._matched_driver_id = -1  # not matched yet

    @property  # like getter method
    def get_rider_id(self):
        return self._rider_id

    @property
    def get_rider_origin(self):
        return self._rider_origin

    @property
    def get_rider_destination(self):
        return self._rider_destination

    @property
    def get_rider_earliest_starting(self):
        return self._rider_earliest_departure_time

    @property
    def get_rider_latest_arrival(self):
        return self._rider_latest_departure_time

    @property
    def get_rider_request_model_type(self):
        return self._rider_request_model_type

    rider_list = []

    @classmethod
    def get_rider_list(cls, df, time_slot, number_of_driver):
        for i in range(len(df)):
            origin_latitude = df.iloc[i]['start_location_lat']
            origin_longitude = df.iloc[i]['start_location_long']
            destination_latitude = df.iloc[i]['end_location_lat']
            destination_longitude = df.iloc[i]['end_location_long']

            '''in data set, pickup time -> requested time; pickup time + 30 -> es; dropoff time + 60 -> la'''
            edt = (pd.to_datetime(df.iloc[i]['rider earliest departure time']))
            ldt = (pd.to_datetime(df.iloc[i]['rider latest departure time']))     #  add one column in the data set, value: edt+10

            request_model_type = df.iloc[i]['requested_car_category']

            print('rider {}, O is {}, D is {}, es is {}, la is {}, request_model_type is {}'.format(i, (origin_latitude, origin_longitude), (destination_latitude, destination_longitude), edt, ldt, request_model_type))

            cls.rider_list.append(
                Rider(i, (origin_latitude, origin_longitude), (destination_latitude, destination_longitude), edt, ldt, request_model_type))
        return cls.rider_list

    # @classmethod
    # def get_rider_by_rider_id(cls, rider_id):    # this method can be replaced by navie visiting the array index....
    #     return cls.rider_list[rider_id]
    # @staticmethod
    # def get_rider_by_origin_point_id(rider_list, rider_origin_point_id, number_of_driver):
    #     return rider_list[rider_origin_point_id - 2 * number_of_driver]


'''
driver information is randomly generated..
latitutde range (30.259, 30.481)
longtitude range (-97.642, -97.748)
model type (0, 3)
'''
lat_lower_bound = 30.259
lat_upper_bound = 30.481
log_lower_bound = -97.748
log_upper_bound = -97.642
class Driver:
    def __init__(self, driver_id, driver_origin, driver_destination, driver_model_type):
        self._driver_id = driver_id
        self._driver_origin = driver_origin
        self._driver_model_type = driver_model_type

    @property
    def get_driver_id(self):
        return self._driver_id

    @property
    def get_driver_origin(self):
        return self._driver_origin

    @property
    def get_driver_model_type(self):
        return self._driver_model_type

    '''randomly generate drivers, driver's O and D must be different'''
    driver_list = []

    @classmethod
    def get_driver_list(cls, number_of_driver):
        driver_model_list = Driver.get_driver_model_list(number_of_driver)

        for i in range(number_of_driver):
            origin_latitude = np.random.uniform(lat_lower_bound, lat_upper_bound)
            origin_longitude = np.random.uniform(log_lower_bound, log_upper_bound)
            model_type = driver_model_list[i]    #  remain unsolved...
            print('driver {}, O is {}, model type is {}'.format(i, (origin_latitude, origin_longitude), model_type))
            cls.driver_list.append(Driver(i, (origin_latitude, origin_longitude), model_type))
        return cls.driver_list


    @staticmethod
    def random_model_generation(model_list, probabilities):
        x = random.uniform(0, 1)
        cumulative_probability = 0.0
        for item, item_probability in zip(model_list, probabilities):
            cumulative_probability += item_probability
            if x < cumulative_probability:
                break
        return item

    @staticmethod
    def get_driver_model_list(number_of_driver):
        driver_model_list = []
        for i in range(number_of_driver):
            driver_model_list.append(Driver.random_model_generation([0, 1], [0.95, 0.05]))
    # @classmethod
    # def get_driver_by_driver_id(cls, driver_id):
    #     return cls.driver_list[driver_id]

    # @staticmethod
    # def get_driver_by_origin_point_id(driver_list, driver_origin_point_id):
    #     return driver_list[driver_origin_point_id]



if __name__ == '__main__':
    # set_point_id_from_object(Driver(1,1,1,1,1,1,1,1))

    pass
