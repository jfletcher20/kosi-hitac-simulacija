from visual import *
tlo=box(pos=vector(0,-.2,0),size=vector(20,.1,1),color=color.green)
kugla=sphere(pos=vector(-5,1.1,0),radius=.4, color=color.red, make_trail=True)

r0=kugla.pos 
g=vector(0,-9.8,0)
kugla.masa=10
v=float (input("Početna brzina = "))
kut=90*pi/180 
kugla.p=kugla.masa*v*vector(cos(kut),sin(kut),0)
h=(v*sin(90))**2/(2*9.8)
t=None
kugla.v=kugla.p/kugla.masa
max_visina=label( pos=vector(0,kugla.pos.y,0), text=str(h))
trenutna_visina=label( pos=vector(-10,kugla.pos.y,0), text=str(kugla.pos.y))
trenutna_brzina=label(pos=vector(6,kugla.pos.y,1), text=str(v))
for i in range (60000):
    kugla.pos=vector(-5,1.1,0)
    kugla.p=kugla.masa*v*vector(cos(kut),sin(kut),0)
    t=0
    dt=0.0001 
    while(kugla.pos.y>=0.1):
        rate(10000)
        F=kugla.masa*g
        kugla.p=kugla.p+F*dt
        kugla.pos=kugla.pos+kugla.p*dt/kugla.masa
        t=t+dt
        trenutna_visina.text=str(kugla.pos.y)
        kugla.v=kugla.p/kugla.masa
        trenutna_brzina.text=str(kugla.v.y)

print("Vrijeme = ",t," sek")
print("Maksimalna visina = ",h,"m")
