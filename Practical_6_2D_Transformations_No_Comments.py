import matplotlib.pyplot as plt
import numpy as np

                                                                   
def plot_shape(ax, vertices, color, label, linestyle="-"):
                                                              
  closed_shape = np.vstack([vertices, vertices[0]])
  ax.plot(
      closed_shape[:, 0],
      closed_shape[:, 1],
      color=color,
      label=label,
      linestyle=linestyle,
      linewidth=2,
  )
  ax.fill(vertices[:, 0], vertices[:, 1], color=color, alpha=0.3)

                                                       
                                       
original_object = np.array([[1.0, 1.0], [4.0, 1.0], [2.5, 4.0]])

                                                           
                                              
                                                           
scaling_matrix = np.array([[1.5, 0], [0, 2.0]])
scaled_object = original_object @ scaling_matrix

                                                           
                                             
                                                           
translation_vector = np.array([3.0, 2.0])
translated_object = original_object + translation_vector

                                                           
                                                                  
                                                           
theta = np.radians(45)
rotation_matrix = np.array(
    [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
)
rotated_object = original_object @ rotation_matrix

                                  
fig, ax = plt.subplots(figsize=(8, 8))

                  
plot_shape(ax, original_object, color="blue", label="Original Object")
plot_shape(
    ax,
    scaled_object,
    color="green",
    label="Scaled (sx=1.5, sy=2.0)",
    linestyle="--",
)
plot_shape(
    ax,
    translated_object,
    color="orange",
    label="Translated (tx=3, ty=2)",
    linestyle="-.",
)
plot_shape(
    ax,
    rotated_object,
    color="red",
    label="Rotated (theta=45°)",
    linestyle=":",
)

                      
ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
ax.set_xlim(-2, 10)
ax.set_ylim(-2, 10)
ax.set_aspect("equal")
ax.grid(True, linestyle=":", alpha=0.6)
ax.set_title("2D Transformations: Scaling, Translation, and Rotation")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend(loc="upper left")

plt.show()
