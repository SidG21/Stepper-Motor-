def forward_step_distance2(step_distance):
    from time import sleep
    import RPi.GPIO as GPIO
    #
    PUL = 11  # Stepper Drive Pulses
    DIR = 13  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
    ENA = 15  # Controller Enable Bit (High to Enable / LOW to Disable).
    # NOTE: Leave DIR and ENA disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.
    GPIO.setmode(GPIO.BOARD)
    # GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 

    GPIO.setup(PUL, GPIO.OUT)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    # Could have usesd only one DURATION constant but chose two. This gives play options.
    durationFwd = 85 * step_distance # This is the duration of the motor spinning. used for forward direction
    #durationBwd = 5000 # This is the duration of the motor spinning. used for reverse direction
    delay = 0.0009 # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.#default
    #delay = 0.0009
    #speed

    GPIO.output(ENA, GPIO.HIGH)
    #GPIO.output(ENAI, GPIO.HIGH)
    print('ENA set to HIGH - Controller Enabled')
    #
    #sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.HIGH)
    #GPIO.output(DIRI, GPIO.HIGH)
    print('DIR set to HIGH - Moving forward at ' + str(delay))
    print('Controller PUL being driven.')
    #
    for y in range(durationFwd):
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
#     GPIO.output(ENA, GPIO.LOW)
    #GPIO.output(ENAI, GPIO.LOW)
    print('ENA set to LOW - Controller Disabled')
    #sleep(.5) # pause for possible change direction
    return

def reverse_step_distance2(step_distance):
    from time import sleep
    import RPi.GPIO as GPIO
    #
    PUL = 11  # Stepper Drive Pulses
    DIR = 13  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
    ENA = 15  # Controller Enable Bit (High to Enable / LOW to Disable).
    # NOTE: Leave DIR and ENA disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.
    GPIO.setmode(GPIO.BOARD)
    # GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 

    GPIO.setup(PUL, GPIO.OUT)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    # Could have usesd only one DURATION constant but chose two. This gives play options.
    #durationFwd = 5000 # This is the duration of the motor spinning. used for forward direction
    durationBwd = 85 * step_distance # This is the duration of the motor spinning. used for reverse direction
    delay = 0.0009# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.#default
    #delay = 0.0009 #speed

    
    GPIO.output(ENA, GPIO.HIGH)
    #GPIO.output(ENAI, GPIO.HIGH)
    print('ENA set to HIGH - Controller Enabled')
    #
    #sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.LOW)
    #GPIO.output(DIRI, GPIO.LOW)
    print('DIR set to LOW - Moving Backward at ' + str(delay))
    print('Controller PUL being driven.')
    for x in range(durationBwd): 
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
#     GPIO.output(ENA, GPIO.LOW)
    #GPIO.output(ENAI, GPIO.LOW)
    print('ENA set to LOW - Controller Disabled')
    #sleep(.5) # pause for possible change direction
    return