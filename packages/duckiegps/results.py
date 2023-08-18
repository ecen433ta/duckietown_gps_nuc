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

class Num_Matrix:
    def __init__(self,number,matrix):
        self.id = number
        self.cam_car_matrix = matrix
    def set_tag_car_matrix(self,matrix):
        self.tag_car_matrix = matrix
    # def set_location(self,x,y):
    #     self.x = x
    #     self.y = y