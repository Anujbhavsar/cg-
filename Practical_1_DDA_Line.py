import matplotlib.pyplot as plt

def draw_line_dda(x1, y1, x2, y2):
                               
    dx = x2 - x1
    dy = y2 - y1

                                                                 
    steps = max(abs(dx), abs(dy))

                                                      
    x_inc = dx / steps
    y_inc = dy / steps

                                
    x = x1
    y = y1

                                                
    x_coords = []
    y_coords = []

                                    
    for _ in range(int(steps) + 1):
                                                               
        x_coords.append(round(x))
        y_coords.append(round(y))
        
                           
        x += x_inc
        y += y_inc

                                                      
    plt.figure(figsize=(6, 6))
    
                                                                          
    plt.plot(x_coords, y_coords, marker="o", color="blue", markersize=5, label="DDA Pixels")
    
                                              
    plt.scatter([x1, x2], [y1, y2], color="red", zorder=5, label="End Points")

                                   
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    
                            
    plt.show()

             
if __name__ == "__main__":
                                                   
    start_x, start_y = 2, 3
    end_x, end_y = 12, 8
    
    draw_line_dda(start_x, start_y, end_x, end_y)
