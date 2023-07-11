class Results:
    def __init__(self):
        self.car_tags = []
        self.fixed_tags = []
    def set_data(self,car_tags,fixed_tags):
        self.car_tags = car_tags
        self.fixed_tags = fixed_tags

class Final_List:
    def __init__(self):
        self.big_list = []
    def add_car(self,car_data):
        self.big_list.append(car_data)
    def get_cars(self):
        return self.big_list