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

    def format_time(self): # Use data attributes stored by self when creating Time object
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objests and return the sum."""
        
        
        return sum

    def change_time(self, seconds):
        '''Modify time attribute by adding seconds'''
        time_seconds = self.time_to_sec() # Call time_to_sec on self data attributes to convert to seconds
        nt = sec_to_time(time_seconds + seconds) # 
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second # The minute, hour, and seconds from nt are stores in Time
        #return None

    def time_to_sec(self):
        '''convert a time object to a single integer representing the number of seconds from mid-night'''
        minutes = self.hour * 60 + self.minute 
        seconds = minutes * 60 + self.second
        return seconds
    
    def valid_time(self):
        """check for the validity of the time object attributes:
            24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True
    
def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60) # Returns a tuple with quotient and remainder from seconds / 60
    time.hour, time.minute = divmod(minutes, 60) # Returns a tuple with quotient and remainder from minutes / 60
    return time


