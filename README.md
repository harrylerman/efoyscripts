# efoyscripts
Scripts for efoy logging

efoyserial: reads in from the EFOY once per minute and prints to a logfile. 
Finds the EFOY via the USB product ID (pid) and vendor ID (vid) of the USB-serial adapter,
so if changing the adapter have to change those parameters.

efoy_logs2csv: reads in efoy logfiles between a specified start date and stop date
and outputs to a csv file. Parameters to change in the script before running are 
startdate, stopdate, filepath of the efoy log files, and output directory (the output
directory probably has to be created).
