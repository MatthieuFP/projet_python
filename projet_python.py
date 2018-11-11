#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 20:33:54 2018

@author: matthieufuteral-peter
"""

from support.my_logger import logger
import pandas as pd
import datetime
import geopy.distance

from support.constants import *

class CsvDataframe:

    def __init__(self, nrows=200000):
        logger.info("start importing the first {} lines of the train_df".format(nrows))
        self.df = pd.read_csv(Path_train, sep=",", nrows=nrows)
        logger.info("start formatting the train_df".format(nrows))
        self.format_df()
        logger.info("done formatted the df".format(nrows))


    def format_df(self):
        self.df[Date] = self.df[Key].map(lambda x: self.get_date(key=x))
        self.df[Time] = self.df[Key].map(lambda x: self.get_hour(key=x))
        self.df[Week_day] = self.df[Date].map(lambda x: self.get_week_day(date=x))
        del self.df[Key], self.df[Pickup_datetime]

        self.drop_outliers()
        self.df[Distance] = self.df[[Pickup_latitude, Pickup_longitude, Dropoff_latitude, Dropoff_longitude]].apply(
            lambda x: self.get_distance(coords_pickup=(x[Pickup_latitude], x[Pickup_longitude]),
                                        coords_dropoff=(x[Dropoff_latitude], x[Dropoff_longitude])), axis=1)

        self.df = self.df.reset_index()

        self.df[Outlier] = self.df[[Distance, Fare_amount]].apply(
            lambda x: self.detect_distance_amount_outliers(dis=x[Distance], amount=x[Fare_amount]), axis=1)
        self.df = self.df[self.df[Outlier] == False]
        del self.df[Outlier]
        logger.info("the new number of lines in the df is {}".format(self.df.shape[0]))

        self.df = self.df.reset_index()

    @staticmethod
    def get_date(key):
        """
        Turn Key into Date
        """
        date = key.split(sep=' ')[0]
        return date

    @staticmethod
    def get_hour(key):
        """
        Turn Key into Hour
        """
        full_time = key.split(sep=' ')[1]
        hour = full_time.split(sep=':')[0]
        return hour

    @staticmethod
    def get_week_day(date):
        """
        Turn Date into Week day
        """
        year, month, day = (int(x) for x in date.split('-'))
        ans = datetime.date(year, month, day)
        week_day = ans.strftime('%A')
        return week_day

    def drop_outliers(self):
        """
        df["pickup_longitude"].max()=2140.60116
        df["pickup_latitude"].max()=1703.092772
        df["dropoff_longitude"].max()=40.851027
        df["dropoff_latitude"].max()=404.61667
        """
        df = self.df

        df = df[df[Pickup_longitude] != 0.000000]

        df = df[df[Pickup_longitude] >= -180]
        df = df[df[Pickup_longitude] <= 180]
        df = df[df[Pickup_latitude] >= -90]
        df = df[df[Pickup_latitude] <= 90]

        df = df[df[Dropoff_longitude] >= -180]
        df = df[df[Dropoff_longitude] <= 180]
        df = df[df[Dropoff_latitude] >= -90]
        df = df[df[Dropoff_latitude] <= 90]

        df = df[df[Fare_amount] > 1]

        self.df = df

    def get_distance(self, coords_pickup, coords_dropoff):
        """
        :return: distance between two coords through geopy
        """
        distance = geopy.distance.vincenty(coords_pickup,coords_dropoff).km
        distance_truncated = float(self.truncate(distance, 3))
        return distance_truncated

    @staticmethod
    def truncate(f, n):
        s = '{}'.format(f)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(f, n)
        i, p, d = s.partition('.')
        return '.'.join([i, (d + '0' * n)[:n]])

    def detect_distance_amount_outliers(self, dis, amount):
        ratio = dis/amount
        if ratio <= 0.08:
            return True
        elif ratio >= 1.5:
            return True
        else:
            return False

if __name__ == '__main__':
    CsvDataframe()



