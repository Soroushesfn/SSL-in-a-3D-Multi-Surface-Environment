def get_cords():
    # Define the field dimensions in centimeters
    field_width = 280  # in cm
    field_height = 400  # in cm

    # Define the point spacing in centimeters
    point_spacing = 20  # in cm

    # Define the table's properties
    table_z = 75  # height of the table in cm
    table_x_min = 70  # x coordinate of the left edge of the table
    table_x_max = 210  # x coordinate of the right edge of the table
    table_y_min = 330  # y coordinate of the top edge of the table
    table_y_max = 400  # y coordinate of the bottom edge of the table

    # Calculate the number of points along each axis
    num_points_x = field_width // point_spacing + 1
    num_points_y = field_height // point_spacing + 1

    # Generate the points
    points = []
    index = 0

    for y in range(int(num_points_y)):
        for x in range(int(num_points_x)):
            point_x = x * point_spacing
            point_y = y * point_spacing

            # Check if the point is within the table's footprint
            if table_x_min <= point_x <= table_x_max and table_y_min <= point_y <= table_y_max:
                point_z = table_z  # Points on the table have z-coordinate 75
            else:
                point_z = 0  # Points on the ground have z-coordinate 0

            points.append({str(index): (point_x, point_y, point_z)})
            index += 1
    return points