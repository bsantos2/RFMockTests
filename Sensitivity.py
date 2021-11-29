import logging

class Sensitivity:
    def __init__(self):
        self.ber   = -999
        self.sinad = -999
        self.dig_sensitivity    = -999
        self.analog_sensitivity = -999
        self.specBer   = 3
        self.specSinad = 12

    def measure(self, type):
        if str(type).upper() in "DIGITAL":
            return self.digital()
        else:
            return self.analog()

    def digital(self):
        startPin = -50
        stopPin = -100
        pin = range(startPin, stopPin - 1, -1)
        measurements = dict()

        #Create mock data for BER vs Pin measurements
        ber = 0.0
        for x in pin:
            measurements[x] = ber
            ber += 5.0/51.0

        for x in range(0, len(pin)):
            midPin = int((startPin + stopPin) * 0.5)
            midBer = measurements[midPin]

            if abs(midBer - self.specBer) <= 0.1:
                print('Sensitivity Pin: ' + str(midPin) + ' where BER: ' + str(midBer) + '\n')
                self.dig_sensitivity = midPin
                self.ber = midBer
                return self.ber
            if midBer < self.specBer:
                startPin = midPin
            elif midBer > self.specBer:
                stopPin  = midPin
        raise ValueError('Sensitivity cannot be measured')

    def analog(self):
        startPin = -50
        stopPin  = -100
        pin = range(startPin, stopPin - 1, -1)
        measurements = dict()

        #Create mock data for SINAD vs Pin measurements
        sinad = 22
        for x in pin:
            measurements[x] = sinad
            sinad -= 14.0/51.0

        for x in range(0, len(pin)):
            midPin = int((startPin + stopPin) * 0.5)
            midSinad = measurements[midPin]

            if abs(midSinad - self.specSinad) <= 0.2:
                print('Sensitivity Pin: ' + str(midPin) + ' where SINAD (dB): ' + str(midSinad) + '\n')
                self.analog_sensitivity = midPin
                self.sinad = midSinad
                return self.sinad
            if midSinad < self.specSinad:
                stopPin = midPin
            elif midSinad > self.specSinad:
                startPin  = midPin
        raise ValueError('Sensitivity cannot be measured')