import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon as MplPolygon

def is_convex(vertices):
  """Determine if a 2D polygon is convex or concave using cross products."""
  n = len(vertices)
  if n < 3:
    return False

                                               
  cross_products = []
  for i in range(n):
    p1 = vertices[i]
    p2 = vertices[(i + 1) % n]
    p3 = vertices[(i + 2) % n]

                                            
    v1 = p2 - p1
    v2 = p3 - p2

                                                 
    cp = v1[0] * v2[1] - v1[1] * v2[0]
    cross_products.append(cp)

                                                                          
  positive = all(cp > 1e-9 for cp in cross_products)
  negative = all(cp < -1e-9 for cp in cross_products)

  return positive or negative

                                                                    
                                               
vertices = np.array([
    [1, 1],
    [5, 1],
    [4, 3],
    [6, 5],
    [3, 4],
    [1, 6],
])

                    
convex = is_convex(vertices)
polygon_type = "Convex Polygon" if convex else "Concave Polygon"

                          
fig, ax = plt.subplots(figsize=(6, 6))

                                  
poly_patch = MplPolygon(
    vertices,
    closed=True,
    facecolor="skyblue" if convex else "salmon",
    edgecolor="darkblue" if convex else "darkred",
    linewidth=2,
    alpha=0.6,
)
ax.add_patch(poly_patch)

                              
ax.plot(vertices[:, 0], vertices[:, 1], "ko", markersize=6)
for i, (x, y) in enumerate(vertices):
  ax.text(
      x + 0.1, y + 0.1, f"P{i}({x},{y})", fontsize=9, fontweight="bold"
  )

                 
ax.set_xlim(0, 7)
ax.set_ylim(0, 7)
ax.set_aspect("equal")
ax.grid(True, linestyle="--", alpha=0.5)
plt.title(
    f"Polygon Type: {polygon_type}", fontsize=12, fontweight="bold", pad=12
)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
