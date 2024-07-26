#!/usr/bin/env python3
# Student ID: sparaskevilo
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    seconds = time_to_sec(t1) + time_to_sec(t2) # Adding time_to_sec time objects to get total seconds
    new_time = sec_to_time(seconds) # Creating properly formatted time object from seconds
    return new_time

def change_time(time, seconds):
    '''Modify time attribute by adding seconds'''
    new_sec = time_to_sec(time) + seconds # Adding amount of seconds time needs to be changed by
    new_time = sec_to_time(new_sec) # Creating properly formatted time object from seconds
    return None

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute 
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60) # Returns a tuple with quotient and remainder from seconds / 60
    time.hour, time.minute = divmod(minutes, 60) # Returns a tuple with quotient and remainder from minutes / 60
    return time

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
