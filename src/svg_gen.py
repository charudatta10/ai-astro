import svgwrite

# Create SVG file
dwg = svgwrite.Drawing('rectangle_with_connections.svg', profile='tiny')

# Define rectangle dimensions
rect_x, rect_y = 200, 200  # Bottom-left corner (pixels)
rect_width, rect_height = 600, 400  # Width and height (pixels)

# Draw the rectangle
dwg.add(dwg.rect(insert=(rect_x, rect_y), size=(rect_width, rect_height), stroke="black", fill="none", stroke_width=2))

# Calculate midpoints of the rectangle sides
mid_top = (rect_x + rect_width / 2, rect_y)
mid_bottom = (rect_x + rect_width / 2, rect_y + rect_height)
mid_left = (rect_x, rect_y + rect_height / 2)
mid_right = (rect_x + rect_width, rect_y + rect_height / 2)

# Add lines connecting midpoints to adjacent sides
lines_midpoints = [
    (mid_top, mid_right),
    (mid_right, mid_bottom),
    (mid_bottom, mid_left),
    (mid_left, mid_top)
]

for start, end in lines_midpoints:
    dwg.add(dwg.line(start=start, end=end, stroke="black", stroke_width=2))

# Draw lines connecting the corners of the rectangle
corners = [
    (rect_x, rect_y),  # Bottom-left
    (rect_x + rect_width, rect_y),  # Bottom-right
    (rect_x, rect_y + rect_height),  # Top-left
    (rect_x + rect_width, rect_y + rect_height)  # Top-right
]

lines_corners = [
    (corners[0], corners[3]),
    (corners[3], corners[0]),
    (corners[2], corners[1]),
    (corners[1], corners[2])
]

for start, end in lines_corners:
    dwg.add(dwg.line(start=start, end=end, stroke="black", stroke_width=2))

# Save the SVG
dwg.save()
print("SVG saved as 'rectangle_with_connections.svg'")