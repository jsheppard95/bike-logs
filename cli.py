"""
bike-logs command line utility
"""

# cli.py

import argparse
from bike_logs import BikeLogs

# Instantiat bike log obkect
bike_logs = BikeLogs()

# Argument Parser Setup
parser = argparse.ArgumentParser(description='bike-logs command line utility')

parser.add_argument('--plot', '-p', action='store_true',
                    help='Plot cumulative distance vs. time')

args = parser.parse_args()

if args.plot:
    bike_logs.plot_cumulative_distance()
