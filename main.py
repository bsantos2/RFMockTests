# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def sensitivity(type):
    if type.upper() == 'DIGITAL':
        startPin = -50
        stopPin = -100
        pin = range(startPin, stopPin - 1, -1)
        measurements = dict()

        ber = 0.0
        for x in pin:
            measurements[x] = ber
            ber += 5.0/51.0

        specBer = 3
        for x in range(0, len(pin)):
            midPin = int((startPin + stopPin) * 0.5)
            midBer = measurements[midPin]

            if abs(midBer - specBer) <= 0.5:
                outputBer = midBer
                print('Sensitivity Pin: ' + str(midPin) + ' where BER: ' + str(midBer) + '\n')
                return outputBer
            if midBer < specBer:
                startPin = midPin
            elif midBer > specBer:
                stopPin = midPin
        print('Sensitivity cannot be measured')
        return -100









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sensitivity('digital')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
