import matplotlib.pyplot as plt

def get_circle_points(xc, yc, r):
    """
    Calculates all pixel coordinates for a circle using the Midpoint Circle Algorithm.
    xc, yc: Center coordinates of the circle
    r: Radius of the circle
    """
    x = 0
    y = r
    p = 1 - r                              
    
                                                        
    points = set()
    
    def add_symmetric_points(x, y):
                                                            
        points.add((xc + x, yc + y))
        points.add((xc - x, yc + y))
        points.add((xc + x, yc - y))
        points.add((xc - x, yc - y))
        points.add((xc + y, yc + x))
        points.add((xc - y, yc + x))
        points.add((xc + y, yc - x))
        points.add((xc - y, yc - x))

                                           
    add_symmetric_points(x, y)
    
                                                                          
    while x < y:
        x += 1
        
        if p < 0:
                                                                      
            p = p + 2 * x + 1
        else:
                                                                               
            y -= 1
            p = p + 2 * x - 2 * y + 1
            
        add_symmetric_points(x, y)
        
    return list(points)

def draw_circle(xc, yc, r):
                             
    points = get_circle_points(xc, yc, r)
    
                                               
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]
    
                                      
    plt.figure(figsize=(7, 7))
    
                                                                            
    plt.scatter(x_vals, y_vals, color='crimson', s=20, label='Rasterized Pixels')
    
                                
    plt.title(f"Midpoint Circle Algorithm\nCenter = ({xc}, {yc}), Radius = {r}", fontsize=12, fontweight='bold')
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    
                                                                              
    plt.gca().set_aspect('equal', adjustable='box')
    
                       
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.axhline(yc, color='black', linewidth=0.8, alpha=0.7)
    plt.axvline(xc, color='black', linewidth=0.8, alpha=0.7)
    plt.legend()
    
                                   
    plt.show()

                       
if __name__ == "__main__":
                                                                   
    center_x = 0
    center_y = 0
    radius = 15
    
    draw_circle(center_x, center_y, radius)
