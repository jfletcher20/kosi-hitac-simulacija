from visual import *
tlo=box(pos=vector(0,-.2,0),size=vector(15,.2,1),color=color.green)
h=float (input("Visina="))
kugla=sphere(pos=vector(-5,h,0),radius=.4, color=color.red, make_trail=True)
kutija=box(pos=vector(-5,h-0.4*2,0), color=color.blue)
r0=kugla.pos
g=vector(0,-9.8,0)
kugla.masa=0.2
v=float(input("Brzina="))
kut=0*pi/180
kugla.p=kugla.masa*v*vector(cos(kut),sin(kut),0)
t=None
s=label(pos=vector (2,2,2), text=str(kugla.pos.x+5))
kugla.v=kugla.p/kugla.masa
trenutna_visina=label( pos=vector(-10,kugla.pos.y,0), text=str(kugla.pos.y))
trenutna_brzina=label(pos=vector(6,kugla.pos.y,1), text=str(v))
for i in range (60000):
    kugla.p=kugla.masa*v*vector(cos(kut),sin(kut),0)
    kugla.pos=vector(-5,h,0)
    t=0
    dt=0.001
    while kugla.pos.y>=0.1:
        rate(1000)
        Fnet=kugla.masa*g
        kugla.p=kugla.p+Fnet*dt
        kugla.pos=kugla.pos+kugla.p*dt/kugla.masa
        t=t+dt
        s.text="Prijedeni put="+str(kugla.pos.x+5)
        trenutna_visina.text="h="+str(kugla.pos.y)
        kugla.v=kugla.p/kugla.masa
        trenutna_brzina.text="v="+str(mag(kugla.v))

    kugla.make_trail=False
print("Kraj = ",kugla.pos-r0," m")
print("Vrijeme = ",t," s")
