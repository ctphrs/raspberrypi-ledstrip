import pigpio
pi = pigpio.pi()
cont = ""
while cont != "c":
    cont = input("r for red b for blue g for green c to stop :")
    if cont == "r":
        pi.set_PWM_dutycycle(17, 255)
    elif cont == "b":
        pi.set_PWM_dutycycle(24, 255)
    elif cont == "g":
        pi.set_PWM_dutycycle(24, 255)
    else:
        print("unknown input")
pi.stop()
