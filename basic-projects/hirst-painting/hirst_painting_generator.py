import turtle as t
import random
# import colorgram


# rgb_colors=[]
# colors=colorgram.extract('paint.jpg',30)
# for color in colors:
#     r= color.rgb.r
#     g= color.rgb.g
#     b= color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
color_list=[  (166, 7, 28),  (245, 220, 60), (171, 85, 33), (27, 49, 72), (205, 153, 12), (200, 175, 69), (47, 101, 170), (110, 163, 216), (217, 117, 163), (40, 35, 25), (231, 239, 247), (134, 68, 102), (104, 12, 82), (96, 189, 156), (52, 99, 77), (236, 169, 195), (33, 52, 45), (104, 94, 189), (5, 52, 130), (185, 186, 213), (187, 5, 3), (173, 100, 115), (42, 73, 69), (45, 70, 75), (189, 99, 81), (237, 171, 160), (164, 207, 189)]
t.colormode(255)
tim=t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(350)
tim.setheading(0)
num_dots=100


for dot_counts in range(1,num_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(60)

    if dot_counts % 10 == 0:

        tim.setheading(90)
        tim.forward(40)
        tim.setheading(180)
        tim.forward(600)
        tim.setheading(0)

screen=t.Screen()
screen.exitonclick()
