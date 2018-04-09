from ..models import Card
from config import type_list, priority_list

class ChartData():
    def __init__(self, from_date, to_date, manpower):
        self.manpower = int(manpower)
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

    def getPlanAccuracyData(self):
        data = [{'name':'计划点数', 'value':0},
                {'name':'实际点数', 'value':0}]
        for record in self.records:
            if record.expect_day is not 0:
                data[0]['value'] += record.expect_day
                data[1]['value'] += record.actual_day

        return data

    def getPlanCompletionData(self):
        data = [{'name':'计划点数', 'value':0},
                {'name':'实际点数', 'value':0}]
        for record in self.records:
            if record.priority is 1:
                data[0]['value'] += record.expect_day
                data[1]['value'] += record.actual_day

        return data

    def getManpowerDistributionData(self):
        data = [{'name':'计划投入', 'value':0},
                {'name':'非计划投入', 'value':0},
                {'name':'未知', 'value':0}]
        for record in self.records:
            if record.expect_day is not 0:
                data[0]['value'] += 1
            else:
                data[1]['value'] += 1
            data[2]['value'] = self.manpower - data[0]['value'] - data[1]['value']

        return self.clearNoneValue(data)