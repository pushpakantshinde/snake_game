from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
#STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #-------------------------------------------------------------------------------------------------------------------

    '''Below code is as per the code explained in the course video. But I have doubt that when segment get extended 
    after eating food item, the new segment gets override with the last segment, so see my code below with required 
    changes'''

    # def create_snake(self):
    #     for position in STARTING_POSITION:
    #         self.add_segment(position)

    # def add_segment(self, position):
    #     new_segment = Turtle("square")
    #     new_segment.color("white")
    #     new_segment.penup()
    #     new_segment.goto(position)
    #     self.segments.append(new_segment)

    # def extend(self):
    #     self.add_segment(self.segments[-1].position())
    #-------------------------------------------------------------------------------------------------------------------

    def create_snake(self):
        for position in STARTING_POSITION:
            x_coordinate = position[0]
            y_coordinate = position[1]
            self.add_segment(x_coordinate, y_coordinate)

    def add_segment(self, x_coordinate, y_coordinate):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x_coordinate, y_coordinate)
        self.segments.append(new_segment)

    def extend(self):
        if self.segments[-1].heading() == UP:
            last_position_x_cor = self.segments[-1].xcor()
            last_position_y_cor = self.segments[-1].ycor() - 20
        elif self.segments[-1].heading() == DOWN:
            last_position_x_cor = self.segments[-1].xcor()
            last_position_y_cor = self.segments[-1].ycor() + 20
        elif self.segments[-1].heading() == LEFT:
            last_position_x_cor = self.segments[-1].xcor() + 20
            last_position_y_cor = self.segments[-1].ycor()
        elif self.segments[-1].heading() == RIGHT:
            last_position_x_cor = self.segments[-1].xcor() - 20
            last_position_y_cor = self.segments[-1].ycor()

        self.add_segment(last_position_x_cor, last_position_y_cor)

    def move(self):
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def clear_snake(self):
        for seg in self.segments:
            seg.hideturtle()

    def snake_reset(self):
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]





