from visual import *

# -*- coding: utf-8 -*-
# g = ~9.8
# brzina objekta u nekom trenutku -> v = a * t
# visina objekta nakon vremena -> y = pocetna_h + v_0 * t - g * t^2 / 2
# ukupna sila s otporom zraka -> F = m * g - (1 / 2) * gustoca_zraka * P * k * v^2 * v

# start velocity of the ball
v0 = float(input("Unesite početnu brzinu loptice: "))
x = float(input("Unesite x koordinatu točke s koje loptica počinje gibati: (x = ?, y, z)"))
y = float(input("Unesite y koordinatu točke s koje loptica počinje gibati: (x, y = ?, z)"))
z = float(input("Unesite z koordinatu točke s koje loptica počinje gibati: (x, y, z = ?)"))
print(str("Početna točka: (" + str(x) + ", " + str(y) + ", " + str(z) + ")"))
k = float(input("Unesite jakost otpora zraka: "))
t = float(input("Unesite duljinu trajanja simulacije: t = "))
#theta = float(input("Unesite kut pod kojom je bačena loptica: "))
theta = 45
thetain = theta
theta = theta * pi / 180

# approximate air density
density = 1.225

# starting point held in a vector
x0 = vector(x, y, z)
startx = x0.x

# text to display values
t1 = label(pos = vector(startx - 2, 3, 0), text = "Starting1...")
t2 = label(pos = vector(startx - 2, 2, 0), text = "Starting2...")

t3 = label(pos = vector(startx - 2, 1, 0), text = "v_0 = " + str(v0))
t4 = label(pos = vector(startx - 2, 0, 0), text = "x_0 = " + str(x0))
t5 = label(pos = vector(startx - 2, -1, 0), text = "k = " + str(k))
t6 = label(pos = vector(startx - 2, -2, 0), text = "t = " + str(t))

# ball to be launched
ball = sphere(pos = x0, radius = 0.1, color = color.orange, make_trail = True)
# ball's mass -> air drag becomes negligible at higher values (1 = 1kg)
ball.m = 0.010

# gravity vector
g = vector(0, -9.8, 0)

ball.make_trail = True

while True:
    
    # set ball start position
    ball.pos = x0
    
    # update the ball's momentum
    ball.p = ball.m * v0 * vector(cos(theta), sin(theta), 0)
    
    time = 0
    dt = 0.001

    # while there is time left to the simulation
    while time < t:
        rate(1000) # perform the loop x times per second
        # calculate velocity of the ball
        ball.velocity = ball.p / ball.m
        # calculate forces on ball
        a = ball.m * g - 0.5 * density * (pi * (ball.radius * ball.radius)) * k * (mag(ball.velocity) * mag(ball.velocity)) * norm(ball.velocity)
        # update momentum
        ball.p = ball.p + a * dt
        # update position
        ball.pos = ball.pos + ball.p * dt / ball.m
        t1.text = "v = " + str(mag(ball.velocity))
        t2.text = "poz = " + str(ball.pos)
        #t2.text = "v = " + str(ball.p.y)
        time = time + dt
    
    ball.make_trail = False
