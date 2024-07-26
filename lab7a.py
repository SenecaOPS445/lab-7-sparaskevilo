#!/usr/bin/env python3
# Student ID: [seneca_id]
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
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    #If seconds/minutes is 60 or more subtract 60 and add 1 to the minute/hour
    if sum.second >= 60:
        remainder = sum.second // 60 
        while remainder > 0: 
            sum.second -= 60 
            sum.minute += 1
    if sum.minute >= 60:
        remainder = sum.minute // 60  # Floor division to reutrn a rounded number less than or equal to the result.
        while remainder > 0: 
            remainder = remainder - 1 # Remainder to keep track how many times we need to subtract by 60 and add to minute
            sum.minute -= 60 # Stores the result of subtracting 60 in sum.second
            sum.hour += 1 # Add to the hour based on how many times the minutes excedded 60
        
    return sum

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
