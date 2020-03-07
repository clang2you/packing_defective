import datetime

# d1 = datetime.datetime(2020, 3, 7, 8, 0, 0)
# d2 = datetime.datetime(2020, 3, 7, 11, 40, 0)
# d3 = datetime.datetime(2020, 3, 7, 12, 30, 0)
# d4 = datetime.datetime(2020, 3, 7, 16, 30, 0)

# timeListAm = []
# # timeListAm.append(d1)

# for i in range(7):
#     if i == 0:
#         periodTime = d1
#     else:
#         periodTime = periodTime + datetime.timedelta(minutes=30)
#     if i == 6 and periodTime != d2:
#         periodTime = d2
#     # print(periodTime)
#     timeListAm.append(periodTime)

# print(timeListAm)

class TimeHelper():
    def __init__(self,amStart, amStop, pmStart, pmStop):
        self.amStartTime = amStart
        self.amStopTime = amStop
        self.pmStartTime = pmStart
        self.pmStopTime = pmStop
        self.isHalf = false

    def GetTimeSlice(self):
        pass