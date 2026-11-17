import matplotlib.pyplot as plt

def draw_line_dda(x0, y0, x1, y1):
    """Generates line pixels using the Digital Differential Analyzer (DDA) algorithm."""
    dx = x1 - x0
    dy = y1 - y0
    
                                            
    steps = int(max(abs(dx), abs(dy)))
    
                                                     
    x_inc = dx / float(steps) if steps != 0 else 0
    y_inc = dy / float(steps) if steps != 0 else 0
    
    x, y = x0, y0
    x_coords, y_coords = [], []
    
    for _ in range(steps + 1):
        x_coords.append(round(x))
        y_coords.append(round(y))
        x += x_inc
        y += y_inc
        
    return x_coords, y_coords

def draw_circle_bresenham(xc, yc, r):
    """Generates circle pixels using Bresenham's Circle Drawing algorithm."""
    x = 0
    y = r
    d = 3 - (2 * r)
    
    x_coords, y_coords = [], []
    
    def plot_symmetric_points(xc, yc, x, y):
                                 
        return [
            xc + x, xc - x, xc + x, xc - x,
            xc + y, xc - y, xc + y, xc - y
        ], [
            yc + y, yc + y, yc - y, yc - y,
            yc + x, yc + x, yc - x, yc - x
        ]

                                       
    x_pts, y_pts = plot_symmetric_points(xc, yc, x, y)
    x_coords.extend(x_pts)
    y_coords.extend(y_pts)
    
    while x <= y:
        x += 1
        if d < 0:
            d = d + (4 * x) + 6
        else:
            y -= 1
            d = d + (4 * (x - y)) + 10
            
        x_pts, y_pts = plot_symmetric_points(xc, yc, x, y)
        x_coords.extend(x_pts)
        y_coords.extend(y_pts)
        
    return x_coords, y_coords

def main():
                                
    plt.figure(figsize=(7, 7))
    plt.title("Pattern using DDA Line & Bresenham's Circle Algorithms")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
                                                         
                                                  
    circle1_x, circle1_y = draw_circle_bresenham(xc=0, yc=0, r=100)
    circle2_x, circle2_y = draw_circle_bresenham(xc=0, yc=0, r=50)
    
    plt.scatter(circle1_x, circle1_y, color='blue', s=2, label='Outer Circle (Bresenham)')
    plt.scatter(circle2_x, circle2_y, color='cyan', s=2, label='Inner Circle (Bresenham)')
    
                                               
                                               
    vertices = [(0, 100), (-86, -50), (86, -50)]
    
                                                    
    for i in range(len(vertices)):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % len(vertices)]                                
        
        line_x, line_y = draw_line_dda(p1[0], p1[1], p2[0], p2[1])
                                             
        if i == 0:
            plt.scatter(line_x, line_y, color='crimson', s=4, label='Triangle Boundary (DDA)')
        else:
            plt.scatter(line_x, line_y, color='crimson', s=4)
            
                                                              
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    main()
