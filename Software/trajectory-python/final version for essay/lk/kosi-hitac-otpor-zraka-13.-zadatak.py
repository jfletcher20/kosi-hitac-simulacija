from visual import *
h=float (input("Visina="))
kugla=sphere(pos=vector(-5,h,0),radius=.4, color=color.red, make_trail=True)
r0=kugla.pos
g=vector(0,-9.8,0)
kugla.masa=0.8e-3
v=float(input("Brzina="))
alpha=float(input("Kut hitca="))
kut=alpha*pi/180
R=0.02
ro=1.2
k=float(input("Otpor= "))
A=pi*R**2
kugla.p=kugla.masa*v*vector(cos(kut),sin(kut),0)
t=None
vrijeme_trajanja= float (input("Vrijeme trajanja= "))
s=label(pos=vector (2,2,2), text=str(kugla.pos.x+5))
kugla.v=kugla.p/kugla.masa
trenutna_visina=label( pos=vector(-10,kugla.pos.y,0), text=str(kugla.pos.y))
trenutna_brzina=label(pos=vector(6,kugla.pos.y,1), text=str(v))
print(str("stupnjevi=" + str(alpha)))
print(str("h=" + str(h)))
print(str("v=" + str(v)))
print(str("k=" + str(k)))
print(str("t=" + str(vrijeme_trajanja)))
for i in range (60000):
    kugla.p=kugla.masa*v*vector(cos(kut),sin(kut),0)
    kugla.pos=vector(-5,h,0)
    t=0
    dt=0.001
    while t<vrijeme_trajanja:
        rate(1000)
        Fnet=kugla.masa*g-0.5*ro*A*k*(mag(kugla.v)**2)*norm(kugla.v)
        kugla.p=kugla.p+Fnet*dt
        kugla.pos=kugla.pos+kugla.p*dt/kugla.masa
        t=t+dt
        s.text="Prijedeni put="+str(kugla.pos.x+5)
        trenutna_visina.text="h="+str(kugla.pos.y)
        kugla.v=kugla.p/kugla.masa
        trenutna_brzina.text="v="+str(mag(kugla.v))
        
    kugla.make_trail=False
