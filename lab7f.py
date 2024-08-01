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

    def __str__(self):
        '''return a string representation for the object self'''
        
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}' # Specify how the object will be formated when called with print function
    
    def __repr__(self):
        '''return a string representation for the object self'''
        '''just instead of ':', you are required use the '.'  in the formatting string.'''

        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}' # This result will appear if print function is not called on object
    
    def __add__(self, t2): # Can now use + to call sum_times instead of t1.sum_times(t2)
        """return the result by using sum_times() method"""
        t2_seconds = t2.time_to_sec()
        total = self.change_time(t2_seconds)
        return total
        
    def format_time(self): # Use data attributes stored by self when creating Time object
        """Return time object (t) as a formatted string"""

        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2): # Self is already stored information under Time hour/minute/second. t2 is additional Time object to be added to whatever is in self
        """Add two time objests and return the sum."""

        t2_seconds = t2.time_to_sec() # Convert t2 to sec first otherwise TypeError unsupported operand type
        total = self.change_time(t2_seconds)  
        return total # The sum value is returned as Time function with hour, minute, second attributes
        
    
    def change_time(self, seconds):
        '''Modify time attribute by adding seconds'''

        time_seconds = self.time_to_sec() # Call time_to_sec on self data attributes to convert to seconds
        nt = sec_to_time(time_seconds + seconds) # Add together the time in seconds from the previously stored self attributes with additional seconds entered
        self.hour, self.minute, self.second = nt.hour,nt.minute,nt.second # sec_to_time is called outside of the class its values are stored under the class using self
        return Time(self.hour, self.minute, self.second) # Store values as part of time function. Return None did not return anything for sum_times to use and return self.hour/min/sec was read as a tuple
    
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


