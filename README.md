# efoyscripts
Scripts for efoy logging

efoyserial: reads in from the EFOY once per minute and prints to a logfile. 
Finds the EFOY via the USB product ID (pid) and vendor ID (vid) of the USB-serial adapter,
so if changing the adapter have to change those parameters.

Each line of the logfile consists of the Unix epoch time (ctime), human-readable date and time, and then the output of the 'SFC' command. From the EFOY interface user manual (pg. 36), the output of this command includes "a largely unformatted string" of the following parameters:

	'SFC': this is the command itself.

	'battery voltage': Voltage measured at the battery.

	'output current': Charging current measured at the fuel cell.

	'operation time (charge mode)': Hours the EFOY Pro fuel cell has been in operation.

	'operating state': Operating status of the EFOY Pro fuel cell:
		Auto on: The fuel cell is working in automatic mode and is on.
		Auto off: The fuel cell is working in automatic mode and is off.
		error: There is an error or malfunction. Please follow the instructions in the EFOY Fuel Cell user manual.
		remote on: The fuel cell is switched on via the remote contact
		remote off: The fuel cell is switched off via the remote contact. Used for Hybrid operation.
		Slave on: If several products are combined via a cluster controller, the following status is indicated for the non-leading units.
		Battery protection: When the battery protection is acitvated.
		Freeze protection: The fuel cell is being used in the freeze protection mode.
		
	'operating mode': Displays current operating mode:
		auto: Automatic
		On
		Off
		Hybrid

	'cumulative output energy': [no description in manual, assumed self-explanatory]

	'error': In addition to indicating the operating mode, the system also displays other text and error messages. Please refer to the user manual for detailed failure codes.

	'cartridge level': If a fuel-cartridge sensor is used, this will indicate whether the level is below or above the sensor level:
		cartridge level above sensor or no sensor
		cartridge level below sensor

	'DuoCartSwitch': Displayed in conjunction with previous status 'cartridge level.'
		Example: (cartridge 1 consumed 1.00 l): DuoCartSwitch is active. Since last fuel cartridge switch, 1 litre of methanol has been used.
		
	'warning': Warning status.
		Warning: An information is displayed and an action isrequired.
		No warning: No action is required.
		
	'SFC>': this is the terminal prompt returned at the end of the message. 

efoy_logs2csv: reads in efoy logfiles between a specified start date and stop date
and outputs to a csv file. Parameters to change in the script before running are 
startdate, stopdate, filepath of the efoy log files, and output directory (the output
directory probably has to be created).
