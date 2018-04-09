from ..models import Card
from config import type_list

class ChartData():
    def __init__(self, from_date, to_date, manpower):
        self.manpower = manpower
        self.records = Card.query.filter(Card.end_time.between(from_date, to_date)).all()

    def dataInit(self, list):
        data = []
        for item in list:
            data.append({"name":item[1], "value": 0})
        return data

    def clearNoneValue(self, data):
        for index, elem in enumerate(data):
            if elem["value"] is 0:
                data.pop(index)
        return data

    def getTaskDistribution(self):
        data = self.dataInit(type_list)
        for record in self.records:
            for index, elem in enumerate(data):
                if record._type is elem["name"]:
                    data[index]["value"] += 1

        return self.clearNoneValue(data)

