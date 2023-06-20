from visual import *


# -*- coding: utf-8 -*-
# g = ~9.8
# brzina objekta u nekom trenutku -> v = a * t
# visina objekta nakon vremena -> y = pocetna_h + v_0 * t - g * t^2 / 2

# start velocity of the ball
v0 = float(input("Unesite početnu brzinu loptice: "))
h = float(input("Unesite visinu s koje je bačena loptica: "))
theta = float(input("Unesite kut pod kojom je bačena loptica: "))
thetain = theta
theta = theta * pi / 180

#determines size of everything
sizefactor = 1
if h > 0:
    sizefactor += h
sizefactor += abs(v0)

bump = sizefactor
if bump > 4:
    bump = bump - 2
# text to display values
t1 = label(pos = vector(sizefactor + 0.5 - 2 - bump, -1, 0), text = "Starting1...")
t2 = label(pos = vector(sizefactor + 0.5 - 2 - bump, -1.5 - 2, 0), text = "Starting2...")
t3 = label(pos = vector(sizefactor + 0.5 - 2 - bump, -2 - 4, 0), text = "Starting3...")
t4 = label(pos = vector(-sizefactor + 0.5 + 1, -1, 0), text = "v_0 = " + str(v0))
t5 = label(pos = vector(-sizefactor + 0.5 + 1, -1.5 - 2, 0), text = "h_0 = " + str(h))
t6 = label(pos = vector(-sizefactor + 0.5 + 1, -2 - 4, 0), text = "theta = " + str(thetain))

# ball to be launched
ball = sphere(pos = vector(-sizefactor + 0.5, h, 0), radius = 0.1, color = color.orange, make_trail = True)
# ground landing point
ground = box(pos = vector(-sizefactor / 2, -0.0025, 0), size = vector(sizefactor, 0.005, 2), color = color.blue)
if h > 0:
    # maximum height from which it was pushed
    heightbox = box(pos = vector(-sizefactor + 0.375, ((h - ball.radius) / 2), 0), size = vector(0.25, h - ball.radius, 0.25), color = color.red)
# ball's mass
ball.m = 1

# create speed vector visual
arr = arrow(pos = ball.pos, axis = vector(cos(theta), sin(theta), 0), shaftwidth = 0.05, headwidth = 0.2, round = True)
arr.length = v0

# gravity vector
g = vector(0, -9.8, 0)

ball.make_trail = True

while True:
    
    # set ball start position
    ball.pos = vector(-sizefactor + 0.5, h, 0)
    
    # update the ball's momentum
    ball.p = ball.m * v0 * vector(cos(theta), sin(theta), 0)
    
    t = 0
    dt = 0.001
    
    if h > 0:
        # while the ball is above the ground
        while ball.pos.y >= 0.1:
            rate(1000) # perform the loop x times per second
            # calculate velocity of the ball
            ball.velocity = ball.p / ball.m
            # calculate forces on ball
            a = ball.m * g
            # update momentum
            ball.p = ball.p + a * dt
            # update position
            ball.pos = ball.pos + ball.p * dt / ball.m
            t1.text = "h = " + str(ball.pos.y)
            t2.text = "v = " + str(mag(ball.velocity))
            t3.text = "d_horiz = " + str(ball.pos.x - -sizefactor + 0.5)
            t = t + dt

    # this allows for negative height inputs
    # helps simulate if a ball will reach floor level or not given a certain force
    else:
        maxheight = ball.pos.y
        iterations = 0
        # while the ball is travelling to above the ground
        
        # note on while condition "maxheight <= ball.pos.y":
        # this will stop the simulation prematurely if the ball is determined
        # as not capable of reaching the floor's level at the current speed
        # and will have the simulation repeat again.
        while ball.pos.y >= 0.1 or maxheight <= ball.pos.y:
            rate(1000) # perform the loop x times per second
            # calculate velocity of the ball
            ball.velocity = ball.p / ball.m
            # calculate forces on ball
            a = ball.m * g
            # update momentum
            ball.p = ball.p + a * dt
            # update position
            ball.pos = ball.pos + ball.p * dt / ball.m
            t1.text = "h = " + str(ball.pos.y)
            t2.text = "v = " + str(mag(ball.velocity))
            t3.text = "d_horiz = " + str(ball.pos.x - -sizefactor + 0.5)
            t = t + dt
            if maxheight < ball.pos.y:
                maxheight = ball.pos.y
    
    ball.make_trail = False
