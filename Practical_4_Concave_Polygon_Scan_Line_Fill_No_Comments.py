import matplotlib.pyplot as plt
import numpy as np

def scanline_fill_concave(vertices, width=400, height=400, fill_color=[0, 150, 255]):
    """
    Fills a concave polygon defined by its vertices using the Scan-Line Fill Algorithm.
    
    Parameters:
    - vertices: List of (x, y) coordinates defining the polygon's boundary nodes.
    - width, height: Dimensions of the output grid canvas.
    - fill_color: RGB list (0-255) for the chosen interior color.
    """
                                                   
    canvas = np.ones((height, width, 3), dtype=np.uint8) * 255
    
                                                                                  
    scaled_vertices = [(int(x), int(y)) for x, y in vertices]
    
                                      
    y_coords = [v[1] for v in scaled_vertices]
    y_min, y_max = min(y_coords), max(y_coords)
    
                            
                                                                                       
    edges = []
    num_vertices = len(scaled_vertices)
    for i in range(num_vertices):
        p1 = scaled_vertices[i]
        p2 = scaled_vertices[(i + 1) % num_vertices]                                 
        
                                                                                  
        if p1[1] != p2[1]:
                                             
            lower, upper = (p1, p2) if p1[1] < p2[1] else (p2, p1)
            
            x1, y1 = lower
            x2, y2 = upper
            inv_slope = (x2 - x1) / (y2 - y1)
            
            edges.append({
                'ymin': y1,
                'ymax': y2,
                'x': float(x1),
                'inv_slope': inv_slope
            })

                                                            
    for y in range(y_min, y_max + 1):
        intersections = []
        
                                                                 
        for edge in edges:
            if edge['ymin'] <= y < edge['ymax']:
                intersections.append(edge['x'])
        
                                                                                
        intersections.sort()
        
                                                       
        for idx in range(0, len(intersections), 2):
            if idx + 1 < len(intersections):
                x_start = int(np.ceil(intersections[idx]))
                x_end = int(np.floor(intersections[idx + 1]))
                
                                                                           
                for x in range(x_start, x_end + 1):
                    if 0 <= x < width and 0 <= y < height:
                        canvas[y, x] = fill_color
                        
                                                                                 
        for edge in edges:
            if edge['ymin'] <= y < edge['ymax']:
                edge['x'] += edge['inv_slope']
                
    return canvas

                         

                                                               
                                                                              
concave_vertices = [
    (200, 350),             
    (320, 100),                     
    (200, 180),                                       
    (80, 100)                      
]

                                                        
filled_canvas = scanline_fill_concave(concave_vertices, width=400, height=400, fill_color=[230, 50, 80])

                                                         
plt.figure(figsize=(6, 6))
plt.title("Concave Polygon Filled with Scan-Line Algorithm")
plt.imshow(filled_canvas)

                                                                         
plt.gca().invert_yaxis()                                                        
plt.xlabel("X Pixels")
plt.ylabel("Y Pixels")
plt.grid(True, linestyle="--", alpha=0.5)

                                  
plt.show()
