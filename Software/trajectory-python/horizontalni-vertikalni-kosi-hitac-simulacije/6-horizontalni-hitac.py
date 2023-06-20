from visual import *

# -*- coding: utf-8 -*-
# g = ~9.8
# brzina objekta u nekom trenutku -> v = a * t
# visina objekta nakon vremena -> y = pocetna_h + v_0 * t - g * t² / 2

# start velocity of the ball
v0 = float(input("Unesite početnu brzinu lopte: "))
h = float(input("Unesite visinu s koje je gurnut objekt: "))

int1 = v0

if int1 == 0:
    int1 = 1
elif int1 < 0:
    int1 *= -1

if h < 0.1:
    h = 0.1

#determines size of everything
sizefactor = int1 + h

# text to display values
t1 = label(pos = vector(-sizefactor / 2, -1, 0), text = "Starting1...")
t2 = label(pos = vector(-sizefactor / 2, -1.5 - 2, 0), text = "Starting2...")
t3 = label(pos = vector(-sizefactor / 2, -2 - 4, 0), text = "Starting3...")

# ball to be launched
ball = sphere(pos = vector(-sizefactor + 0.5, h, 0), radius = 0.1, color = color.orange, make_trail = True)
# ground landing point
ground = box(pos = vector(-sizefactor / 2, -0.0025, 0), size = vector(sizefactor, 0.005, 2), color = color.blue)
if v0 < 0 and int1 > 0:
    ground.pos.x += -sizefactor
# maximum height from which it was pushed
heightbox = box(pos = vector(-sizefactor + 0.375, ((h - ball.radius) / 2), 0), size = vector(0.25, h - ball.radius, 0.25), color = color.red)
# ball's mass
ball.m = 1

# starting position
r0 = ball.pos
# gravity vector
g = vector(0, -9.8, 0)
ball.make_trail = True

while True:
    
    # set ball to start position
    ball.pos = vector(-sizefactor + 0.5, h, 0)
    
    # update the ball's position horizontally
    ball.p = ball.m * v0 * vector(1, 0, 0)
    
    t = 0
    dt = 0.001
    
    # while the ball is above the ground
    while ball.pos.y >= 0.1:
        rate(1000) # perform the loop x times per second
        # calculate velocity of the ball
        ball.velocity = ball.p / ball.m
        # calculate forces on the ball
        a = ball.m * g
        ball.p = ball.p + a * dt
        ball.pos = ball.pos + ball.p * dt / ball.m
        t1.text = "h = " + str(ball.pos.y)
        t2.text = "v = " + str(mag(ball.velocity))
        t3.text = "d_horiz = " + str(ball.pos.x - -sizefactor + 0.5)
        t3.pos.x = ball.pos.x
        t = t + dt
    
    # deactivate trail before resetting the ball's position
    ball.make_trail = False
