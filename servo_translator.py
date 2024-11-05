# Submit this file via brightspace

# You should not modify the signature (name, input, return type) of this function
def translate(angle: float) -> int:
	"""
	Converts an angle in degrees to the corresponding input
	for the duty_u16 method of the servo class

	See https://docs.micropython.org/en/latest/library/machine.PWM.html for more
	details on the duty_u16 method
	"""
	

	# Your code here

	pulse_width = 500 + (2500 - 500) * angle / 180 # the equation for the pulse width from the manual
	duty_cycle = pulse_width / 20000  # 20000 microseconds = 20ms period
	duty_u16_value = int(duty_cycle * 65535) # multiply so it is in the pwm class

	duty_u16_value = max(1638, min(8192, duty_u16_value)) #this clamps the value if the value outputs outside of the safe range
	return duty_u16_value #return the output


	