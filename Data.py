class Data:
    def __init__(self, process: int, arrival: int, burstTime: int, priority: int):
        self.process = process
        self.arrival = arrival
        self.burstTime = burstTime
        self.priority = priority


class DataList:
    def __init__(self):
        self.dataList = []

    @staticmethod
    def processKey(self, elem: Data):
        return elem.process

    @staticmethod
    def arrivalKey(self, elem: Data):
        return elem.arrival

    @staticmethod
    def burstKey(self, elem: Data):
        return elem.burstTime

    @staticmethod
    def priorityKey(self, elem: Data):
        return elem.priority

    def sortBy(self, by: str):
        if by == "PROCESS":
            self.dataList.sort(key=self.processKey)
        elif by == "ARRIVAL":
            self.dataList.sort(key=self.arrivalKey)
        elif by == "BURST":
            self.dataList.sort(key=self.burstKey)
        elif by == "PRIORITY":
            self.dataList.sort(key=self.priorityKey)
        else:
            print("INVALID INPUT")
