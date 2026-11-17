import matplotlib.pyplot as plt
import numpy as np

def koch_curve(p1, p2, order):
  if order == 0:
    return np.array([p1, p2])

                                  
  p1 = np.array(p1, dtype=float)
  p2 = np.array(p2, dtype=float)

                                              
  delta = p2 - p1
  s1 = p1 + delta / 3.0
  s3 = p1 + (2.0 * delta) / 3.0

                                                              
  angle = np.pi / 3                         
  rotation_matrix = np.array(
      [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
  )
  s2 = s1 + np.dot(rotation_matrix, (s3 - s1))

                                                          
  c1 = koch_curve(p1, s1, order - 1)
  c2 = koch_curve(s1, s2, order - 1)
  c3 = koch_curve(s2, s3, order - 1)
  c4 = koch_curve(s3, p2, order - 1)

                                                         
  return np.concatenate([c1[:-1], c2[:-1], c3[:-1], c4])

                                               
start_point = (0.0, 0.0)
end_point = (1.0, 0.0)
recursion_order = 4                                    

                                 
points = koch_curve(start_point, end_point, recursion_order)

                       
plt.figure(figsize=(8, 4))
plt.plot(points[:, 0], points[:, 1], color="teal", linewidth=1.2)
plt.title(f"Koch Curve (Order {recursion_order})", fontsize=14)
plt.axis("equal")
plt.axis("off")                                    
plt.show()
