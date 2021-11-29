# Press the green button in the gutter to run the script.
from Sensitivity import Sensitivity

if __name__ == '__main__':
    MeasureSensitivity = Sensitivity()
    MeasureSensitivity.measure("digital")
    MeasureSensitivity.measure("fm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
