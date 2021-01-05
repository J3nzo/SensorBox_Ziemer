from grovepi import *
import time
import grovepi

dht_sensor_port = 7
ledred = 4
ledorange = 3
ledgreen = 2
air_sensor = 0
example = 120
grovepi.pinMode(air_sensor,"INPUT")


time.sleep(1)

while True:
        [temp, hum] = dht(dht_sensor_port, 0)
        print
        "temp =", temp, "C\thumadity =", hum, "%"
        t = str(temp)
        h = str(hum)


        if not hum is None:
            print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(11, hum, temp))
        else:
            print('DHT{0}, humidity & temperature: {1}'.format(11, temp))
        time.sleep(1)

        try:
            pinMode(ledgreen, "OUTPUT")
            digitalWrite(ledgreen, 0)
            print("LEDWhite ON!")
            time.sleep(1)

            pinMode(ledred, "OUTPUT")
            digitalWrite(ledred, 1)
            print("LEDRED ON!")
            time.sleep(1)

            pinMode(ledorange, "OUTPUT")
            digitalWrite(ledorange, 0)
            print("LEDGREEN OFF!")
            time.sleep(1)


        except KeyboardInterrupt:
            digitalWrite(ledred, 0)
            break
        except IOError:
            print("Error")

        try:
            sensor_value = grovepi.analogRead(air_sensor)

            if sensor_value > 700:
                print("High pollution")
            elif sensor_value > 300:
                print("Low pollution")
            else:
                print("Air fresh")

            print("sensor_value =", sensor_value)

            time.sleep(.5)
            pinMode(ledred, "OUTPUT")
            digitalWrite(ledred, 0)
            print("LEDRED OFF!")
            time.sleep(1)

            pinMode(ledorange, "OUTPUT")
            digitalWrite(ledorange, 1)
            print("LEDGREEN ON!")
            time.sleep(1)

        except IOError:
            print("Error")

        if example < 100:
            pinMode(ledgreen, "OUTPUT")
            digitalWrite(ledgreen, 1)
            print("LEDWhite ON!")
            time.sleep(1)

        else:
            pinMode(ledgreen, "OUTPUT")
            digitalWrite(ledgreen, 0)
            print("LEDWhite OFF!")
            time.sleep(1)