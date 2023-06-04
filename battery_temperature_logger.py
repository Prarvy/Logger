# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: Battery Temperature Logger
# Version: 1.0: Base version by author

import random
import logging
import datetime


class BatteryLogger:
    def __init__(self, file_name):
        self.file_name = file_name
        logging.basicConfig(filename=self.file_name, filemode='w', level=logging.WARNING,
                            format='%(name)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger('BatteryLogger')

    def temperature_simulator(self):
        current_datetime = datetime.datetime.now()
        for _ in range(60):
            log_time = current_datetime + datetime.timedelta(minutes=1)
            simulated_time = log_time.strftime('%Y-%m-%d %H:%M:%S')
            temp = random.randint(20, 40)
            if temp < 20:
                self.logger.debug(f'{simulated_time}: Temperature in Celsius < 20')
            elif 30 <= temp <= 35:
                self.logger.warning(f'{simulated_time}: Temperature in Celsius between 30 and 35')
            elif temp > 35:
                self.logger.critical(f'{simulated_time}: Temperature in Celsius > 35')
            current_datetime = log_time


if __name__ == '__main__':
    battery_logger = BatteryLogger('battery_temperature.log')
    battery_logger.temperature_simulator()
