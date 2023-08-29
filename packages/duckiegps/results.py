class Results:
    def __init__(self):
        self.location_array = []
        self.has_car = False
    def set_data(self,id,x,y):
        self.location_array.append([float(id),float(x),float(y)])

class Final_List:
    def __init__(self):
        self.big_list = []
    def add_car(self,car_data):
        self.big_list.append(car_data)
    def get_cars(self):
        return self.big_list
