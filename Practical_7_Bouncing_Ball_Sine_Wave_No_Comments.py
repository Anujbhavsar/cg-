import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

                            
fig, ax = plt.subplots(figsize=(8, 4.5))

                                                     
x_wave = np.linspace(0, 4 * np.pi, 500)
y_wave = np.sin(x_wave)

                         
ax.plot(x_wave, y_wave, '--', color='gray', alpha=0.5, label='Sine Path')

                                                              
(ball,) = ax.plot([], [], 'ro', markersize=12, label='Bouncing Ball')

                            
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Bouncing Ball Along a Sine Wave', fontsize=14)
ax.set_xlabel('X Position (radians)')
ax.set_ylabel('Amplitude (Y)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

                                           
def init():
  ball.set_data([], [])
  return (ball,)

                                       
def update(frame):
                                           
  x_pos = x_wave[frame]
                                                                                           
                                                                                         
  y_pos = np.sin(x_pos)

  ball.set_data([x_pos], [y_pos])
  return (ball,)

                      
ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(x_wave),
    init_func=init,
    interval=20,
    blit=True,
    repeat=True,
)

plt.show()
