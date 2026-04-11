from vpython import *

scene = canvas(width=1000, height=600, background=color.black)

# Object definitions
ball = sphere(pos=vector(-2.4,0.6,0.6), radius=0.5, color=color.red)
ball.trail = curve(radius=0.1, color=ball.color)
ball.velocity = vector(0,0,0)

wallR = box(pos=vector(21,6,0), size=vector(0.2,12,12), color=color.green)
wallL = box(pos=vector(-3,6,0), size=vector(0.2, 12, 12), color=color.green)
wallU = box(pos=vector(9,12,0), size=vector(24,0.2,12), color=color.green)
wallD = box(pos=vector(9,0,0), size=vector(24,0.2,12), color=color.green)
wallB = box(pos=vector(9,6,-6), size=vector(24,12,0.2), color=color.purple)
walls_thickness = wallR.size.x/2

# Wall collision conditions

def collision_check(v, o):
    if o == 'R' and v == 'x' :
        check = (ball.pos.x + ball.radius) >= (wallR.pos.x - walls_thickness)
    elif o == 'L' and v == 'x' :
        check = (ball.pos.x - ball.radius) <= (wallL.pos.x + walls_thickness)
    elif o == 'U' and v == 'y' :
        check = (ball.pos.y + ball.radius) >= (wallU.pos.y - walls_thickness)
    elif o == 'D' and v == 'y' :
        check = (ball.pos.y - ball.radius) <= (wallD.pos.y + walls_thickness)
    elif o == 'B' and v == 'z' :
        check = (ball.pos.z - ball.radius) <= (wallB.pos.z + walls_thickness)
    elif o == 'F' and v == 'z' :
        check = (ball.pos.z + ball.radius) >= (6 + walls_thickness)
    return check


# Motion and animation

dt = 0.05
g = 9.8
move = True

def ball_motion(x0, y0, v_y0, z0):
    # x-motion
    ball.pos.x = x0 + ball.velocity.x*dt
    # y-motion
    ball.pos.y = y0 + v_y0*dt - (0.5*g*(dt)**2)
    ball.velocity.y = v_y0 - g*dt
    # z-motion
    ball.pos.z = z0 + ball.velocity.z*dt

def velocity_x(v_x):
    ball.velocity.x = float(v_x.text)

def velocity_y(v_y):
    ball.velocity.y = float(v_y.text)
    
def velocity_z(v_z):
    ball.velocity.z = float(v_z.text)
    
def animate():
    # Animating the ball's motion
    bv = arrow(pos=ball.pos, axis=ball.velocity, color=color.yellow)
    while move :
        rate(20)
        ball_motion(ball.pos.x, ball.pos.y, ball.velocity.y, ball.pos.z)
        ball.trail.append(pos=ball.pos)
        bv.pos = ball.pos
        bv.axis = ball.velocity

        if collision_check('x', 'R') or collision_check('x', 'L')  :
            ball.velocity.x = -ball.velocity.x
            ball.velocity.x = ball.velocity.x - 0.5
            if ball.velocity.x == 0:
                ball.velocity.x == 0
        elif collision_check('y', 'D') or collision_check('y', 'U') :
            ball.velocity.y = - ball.velocity.y
            if collision_check('y', 'D'):
                ball.velocity.y = ball.velocity.y - g*dt
                if ball.velocity.y <= 0 :
                    ball.velocity = vector(0,0,0)
                    break
        elif collision_check('z', 'B') or collision_check('z', 'F') :
            ball.velocity.z = -ball.velocity.z
            ball.velocity.z = ball.velocity.z - 0.5
            if ball.velocity.z == 0:
                ball.velocity.z == 0

def Reset():
    move = False
    ball.pos = vector(-2.4,0.6,0.6)
    v_x.text = '0'
    v_y.text = '0'
    v_z.text = '0'
    ball.trail.clear_trail()

    
# widgets
scene.append_to_caption('Entere velocity components:','\n\n', "velocity_x: ")
v_x = winput(type='numeric', bind=velocity_x)
scene.append_to_caption('\n\n', "velocity_y: ")
v_y = winput(type='numeric', bind=velocity_y)
scene.append_to_caption('\n\n', "velocity_z: ")
v_z = winput(type='numeric', bind=velocity_z)
scene.append_to_caption('\n\n')
launch = button(text='Launch', bind=animate)
reset = button(text='Reset', bind=Reset)

        
