# Chapter 7 Question 10
import time


class Time:
    def __init__(self, seconds=int(time.time())):
        hours = seconds // 3600
        hour = hours % 24
        seconds %= 3600
        minute = seconds // 60
        second = seconds % 60

        self.__hour = int(hour)
        self.__minute = int(minute)
        self.__second = int(second)

    def getHours(self):
        return self.__hour

    def getMinutes(self):
        return self.__minute

    def getSeconds(self):
        return self.__second

    def setTime(self, seconds):
        object = Time(seconds)
        self.__hour = object.getHours()
        self.__minute = object.getMinutes()
        self.__second = object.getSeconds()

    def getTime(self):
        return str(self.getHours()) + ":" + str(self.getMinutes()) + ":" + str(self.getSeconds())


def main():
    time1 = Time()
    print("The current time is ", time1.getTime())
    elapsedTime = eval(input("Enter Elapsed Time : "))
    time1.setTime(elapsedTime)
    print("The hour:minute:second for the elapsed time is ", time1.getTime())


if __name__ == "__main__":
    main()
