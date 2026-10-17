import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self,):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_y = random.randint(-230, 230)
            
            # ✅ Check BEFORE creating
            safe = True
            for car in self.all_cars[-3:]:
                if abs(car.ycor() - random_y) < 40:
                    safe = False
                    break
            
            if safe:
                
                new_car = Turtle("square")
                new_car.shapesize(stretch_len=2, stretch_wid=1)
                new_car.penup()
                new_car.goto(-300, random_y)  # ✅ move before color
                new_car.color(random.choice(COLORS))
                self.all_cars.append(new_car)

            # random_y= random.randint(-230,230)
            # new_car.goto(-300,random_y)
            # self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
        #removes all off screen cars from memory
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320] 

    def level_up(self):
        if self.car_speed < 20:
            self.car_speed += MOVE_INCREMENT

        
