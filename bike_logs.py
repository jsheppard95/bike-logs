"""
bike-logs.py
script to monitor my bike riding, compute total distance, display results
"""
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Start with function that takes in current bike computer total and writes
# the result to a file with a timestamp

class BikeLogs:
    """
    BikeLogs class to log bike rides I take
    """
    def write_single_ride(self, distance_travelled, unit='mi'):
        """
        Function that writes the distance of a single ride to the main file
        bike-logs.csv with a timestamp

        Parameters:
        -----------

        distance_travelled : float
            length of single bike ride, default in miles
        unit : string, opt
            unit of choice, default to mi, can use 'km'
        """
        if unit == 'km':
            # convert to mi, 1 mi = 1.60934 km
            distance_travelled *= (1/1.60934) 
        f = open('bike-logs.csv', 'a')
        now = datetime.datetime.now()
        now_iso = now.isoformat() # YYYY-MM-DDTHH:MM:SS
        today = now_iso[:10]
        f.write(today + ' ' + str(distance_travelled) + '\n')
        f.close()

    def get_total_distance(self):
        """
        Function that returns the total travelled

        Returns:
        --------
        total_distance : float, mi
            the total distance travelled thus far in miles
        """
        # First total up single ride distances found in bike-logs.csv
        total_distance = 0
        f = open('bike-logs.csv', 'r')
        for line in f:
            line_values = line.split(' ') # list [time, distance_travelled]
            total_distance += float(line_values[1])
        f.close()
        return total_distance
    
    def convert_date(self, date_bytes):
        """
        Helper function needed to get dates into array
        """
        return mdates.strpdate2num('%Y-%m-%d')(date_bytes.decode('ascii'))

    def plot_cumulative_distance(self):
        """
        Function that plots the cumulative distance travalled vs. time
        """
        # Some numpy magic
        # dates : array containing floating point numbers representing date
        # distances : corresponding distance travelled on that date
        dates, distances = np.loadtxt('bike-logs.csv', unpack=True,
                                      delimiter=' ',
                                      converters= {0:self.convert_date})
        # Get cumulative distance array
        cumulative_distances = np.zeros(len(distances))
        for i in range(1, len(distances)):
            cumulative_distances[i] = cumulative_distances[i-1] + \
                                      distances[i]
        f1, ax1 = plt.subplots()
        ax1.plot_date(x=dates, y=cumulative_distances, fmt='r-')
        ax1.set_title("Cumulative Distance vs. Time")
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Cumulative Distance (mi)")
        ax1.grid(True)
        f1.show()
        input("\nPress <Enter to exit...\n")