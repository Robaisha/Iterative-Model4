GlowScript 3.0 VPython
####### ITERATIVE MODELLING #######
### acceleration ## but, with the rabbit and vectors


#-------------- set scene settings
#scene=canvas(background=color.white)
#-------------- define your origin (it can be of your choice, just don't forget
#-------------- to offset everything elese wrt to your defined origin
oriin = sphere(color=color.white, opacity=0.4)
#-------------- set your axes
x_ax = curve(pos=[vector(-70,0,0),vector(70,0,0)],color=color.red)
y_ax = curve(pos=[vector(0,-70,0),vector(0,70,0)],color=color.green)
z_ax = curve(pos=[vector(0,0,-70),vector(0,0,70)],color=color.blue)
#--------------



#-------------- create objects

rabbit = sphere(radius=5, pos=vector(28,30,0),color=color.white, make_trail=True)
print("initial pos = ", rabbit.pos)

rabb_pos = arrow(axis=rabbit.pos, opacity=0.3)

#-------------- variables

# set of parametric equation
#x = -0.31*t*t + 7.2*t + 28
#y = 0.22*t - 9.1*t +30

t = 0                    #initial time value
dt = 0.1                 #time step size


#instantaneuos velocity
rabb_vx = -0.62*t + 7.2
rabb_vy = 0.44*t - 9.1
rabb_vel = arrow(pos=rabbit.pos, axis=vector(rabb_vx,rabb_vy,0) , color=color.blue,opacity=0.3)

#instantaneuos acceleration
rabb_ax = -0.62
rabb_ay = 0.44
rabb_acc = arrow(pos=rabbit.pos, axis=vector(rabb_ax,rabb_ay,0) , color=color.green,opacity=0.3)


# we do not need velocity and acceleration because we already have the parametric
# set of equations.
#vel = vector(3,1,7)      #boxer velocity
#acc = vector(0,0,-7)     #boxer acceleration


#-------------- iteration
while t<31:
    rate(10)
    x = -0.31*t*t + 7.2*t + 28
    y = 0.22*t*t - 9.1*t +30
    rabbit.pos = (x,y,0)
    #boxer.pos = boxer.pos + vel*dt + 0.5*acc*dt*dt
    #vel = vel + acc*dt
    t=t+dt
    
    #position vector
    rabb_pos.axis = rabbit.pos
    #velocity vector
    rabb_vx = -0.62*t + 7.2
    rabb_vy = 0.44*t - 9.1
    rabb_vel.pos = rabbit.pos
    rabb_vel.axis=vector(rabb_vx,rabb_vy,0)
    #acceleration vector
    rabb_acc.pos = rabbit.pos 

    


print("finial position = ", rabbit.pos)
#print("finial velocity = ", vel)
#print("acceleration = ", acc)
print("time elapsed = ", t)
    