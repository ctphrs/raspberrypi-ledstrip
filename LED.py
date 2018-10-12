import pigpio
pi = pigpio.pi()
cont = ""
r = 0
b = 0
g = 0
while cont != "c":
    cont = raw_input("r for red;\n b for blue;\n g for green;\n o for off;\n c to stop :")
    if cont == "r" and r != 1:
        pi.set_PWM_dutycycle(17, 255)
        r = 1
    elif cont == "b" and b != 1:
        pi.set_PWM_dutycycle(24, 255)
        b = 1
    elif cont == "g" and g != 1:
        pi.set_PWM_dutycycle(22, 255)
        g = 1
    elif cont == "r" and r == 1:
        pi.set_PWM_dutycycle(17, 0)
        r = 0
    elif cont == "b" and b == 1:
        pi.set_PWM_dutycycle(24, 0)
        b = 0
    elif cont == "g" and g == 1:
        pi.set_PWM_dutycycle(22, 0)
        g = 0
    elif cont == "o":
        pi.set_PWM_dutycycle(17, 0)
        pi.set_PWM_dutycycle(24, 0)
        pi.set_PWM_dutycycle(22, 0)
        r = 0
        g = 0
        b = 0
    elif cont == "c":
        print("stopping...")
        pi.set_PWM_dutycycle(17, 0)
        pi.set_PWM_dutycycle(24, 0)
        pi.set_PWM_dutycycle(22, 0)
    else:
        print("unknown input")


pi.stop()
