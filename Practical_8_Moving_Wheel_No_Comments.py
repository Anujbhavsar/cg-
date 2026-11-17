import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

                                 
RADIUS = 1.0                               
V = 2.0                                                   
FPS = 30                                 
DURATION = 5                                               
TOTAL_FRAMES = FPS * DURATION
DT = 1.0 / FPS                             

                                                                
OMEGA = V / RADIUS 

                               
fig, ax = plt.subplots(figsize=(10, 5))
                                               
ax.set_xlim(-2, 12)
ax.set_ylim(-0.5, 2.5)
ax.set_aspect('equal')                                    
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("Moving Wheel Simulation (Rolling Without Slipping)")
ax.set_xlabel("Distance")
ax.set_ylabel("Height")

                      
ax.axhline(0, color='black', linewidth=2)

                                  
                                                   
theta_circle = np.linspace(0, 2 * np.pi, 100)
tire_x_local = RADIUS * np.cos(theta_circle)
tire_y_local = RADIUS * np.sin(theta_circle)
tire_line, = ax.plot([], [], color='dimgray', linewidth=4, label='Tire')

                                                                          
num_spokes = 8
spoke_angles = np.linspace(0, 2 * np.pi, num_spokes, endpoint=False)
spokes_lines = [ax.plot([], [], color='crimson', linewidth=2)[0] for _ in range(num_spokes)]

                                
hub_dot, = ax.plot([], [], 'ko', markersize=8, label='Hub (Center)')
                                                          
rim_dot, = ax.plot([], [], 'bo', markersize=6, label='Rim Marker')
path_x, path_y = [], []
path_line, = ax.plot([], [], 'b--', alpha=0.5, label='Cycloid Path')

ax.legend(loc="upper right")

                             
def init():
    """Initialize clear frame elements."""
    tire_line.set_data([], [])
    hub_dot.set_data([], [])
    rim_dot.set_data([], [])
    path_line.set_data([], [])
    for line in spokes_lines:
        line.set_data([], [])
    return [tire_line, hub_dot, rim_dot, path_line] + spokes_lines

def update(frame):
    """Update positions for each frame timestep."""
    t = frame * DT
    
                                                       
    center_x = V * t
    center_y = RADIUS
    
                                                                                           
    phi = -OMEGA * t
    
                          
    tire_line.set_data(tire_x_local + center_x, tire_y_local + center_y)
    
                         
    hub_dot.set_data([center_x], [center_y])
    
                             
    for i, angle in enumerate(spoke_angles):
                                                                    
        current_angle = angle + phi
        end_x = center_x + RADIUS * np.cos(current_angle)
        end_y = center_y + RADIUS * np.sin(current_angle)
        spokes_lines[i].set_data([center_x, end_x], [center_y, end_y])
        
                                                                                               
        if i == 0:
            rim_dot.set_data([end_x], [end_y])
            path_x.append(end_x)
            path_y.append(end_y)
            path_line.set_data(path_x, path_y)

    return [tire_line, hub_dot, rim_dot, path_line] + spokes_lines

                           
                                                                       
ani = animation.FuncAnimation(
    fig, update, frames=TOTAL_FRAMES, init_func=init, 
    interval=int(DT * 1000), blit=True, repeat=True
)

plt.show()
