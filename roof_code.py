import rhinoscriptsyntax as rs
import math

def create_pavillion(u_count, v_count, spacing, height, curve_amplitude, curve_frequency):
    point = []
    roof_points = []
    roof_lines = []

    # generate pavillion point, column & roof 
    for i in range(u_count):
        for j in range(v_count):
            x = i* spacing
            y = j*spacing
            z = 0
            pt = rs.AddPoint(x,y,z)
            point.append(pt)
            
            
            #generate roof points
            z_roof = height + curve_amplitude * math.sin(curve_frequency * math.pi * i / (u_count - 1)) * math.sin(curve_frequency * math.pi * j / (v_count - 1))
            pt_roof = rs.AddPoint(x, y, z_roof)
            roof_points.append(pt_roof)
            
    #Generate lines between roof points
    for i in range(u_count):
        for j in range(v_count):
            #Horizontal lines
            if i < u_count -1:
                start_pt = roof_points[j*u_count+i]
                end_pt = roof_points[j*u_count+(i+1)]
                roof_lines.append(rs.AddLine(start_pt,end_pt))
            # Vertical lines
            if j < v_count -1:
                start_pt = roof_points[j*u_count+i]
                end_pt = roof_points[(j+1)*u_count+i]
                roof_lines.append(rs.AddLine(start_pt,end_pt))
            
    return point,roof_points, roof_lines


#create pavillion
points,roof_points, roof_lines= create_pavillion(u_count, v_count,spacing,height, curve_amplitude, curve_frequency)