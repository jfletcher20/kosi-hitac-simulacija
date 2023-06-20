from visual import *

# -*- coding: utf-8 -*-
# g = 9.8
# brzina objekta u nekom trenutku -> v = a * t
# pozicija objekta nakon nekog vremena stalnom brzinom -> v = s / t -> s = vt
# vektor položaja objekta jednoliko ubrzano s akceleracijom i pocetnom brzinom -> x(t) = 
# max visina objekta -> h_max = (v_0y²) / 2 * g
# visina objekta nakon vremena -> h = pocetna_h + v_0 * t - g * (t² / 2) -> npr. h(t) = 5 + 10 * t - 9.8 * (t² / 2)
# vektor položaja objekta bačeno vertikalno uvis -> 

# start velocity of the ball
v0 = float(input("Unesite početnu brzinu lopte: "))

# text to display values
t1 = label(pos = vector(0, -1, 0), text = "Starting1...")
t2 = label(pos = vector(0, -2, 0), text = "Starting2...")
t3 = None
# ground landing point
ground = box(pos = vector(0, -0.0025, 0), size = vector(5, 0.005, 2), color = color.blue)
# ball to be launched
ball = sphere(pos = vector(0, 0.10000001, 0), radius = 0.1, color = color.orange)
# ball's mass
ball.m = 1

# gravity vector
g = vector(0, -9.8, 0)

# max height starts at 0
maxheight = 0

while True:

    if t3 == None:
        t3 = label(pos = vector(ball.pos.x + 1.5, ball.pos.y, 0), text = str(ball.pos.y))
    
    ball.pos = vector(0, 0.10000001, 0)
    
    # update the ball's position vertically
    ball.p = ball.m * v0 * vector(0, 1, 0)
    
    t = 0
    dt = 0.001
    
    pr = 1
    
    # while the ball is above the ground
    while ball.pos.y >= 0.1:
        
        rate(1000) # perform the loop x times per second
        # calculate velocity of the ball
        ball.velocity = ball.p / ball.m
        # calculate forces on ball
        a = ball.m * g
        ball.p = ball.p + a * dt
        ball.pos = ball.pos + ball.p * dt / ball.m
        
        t1.text = "h = " + str(ball.pos.y)
        t2.text = "v = " + str(mag(ball.velocity))
        t1.pos.y = -1 + ball.pos.y
        t2.pos.y = -1.5 + ball.pos.y
        
        if maxheight < ball.pos.y:
            maxheight = ball.pos.y
            t3.pos.y = maxheight
            t3.text = "<- h_max = " + str(maxheight)
        t = t + dt
