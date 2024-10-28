import math

def radius_inscribed_pentagon(side_length):
    return (side_length * (1 + math.sqrt(5))) / (2 * math.sqrt(3))

def radius_circumscribed_pentagon(side_length):
    return side_length / (2 * math.sin(math.pi / 5))

side_length = 5
r_inscribed = radius_inscribed_pentagon(side_length)
r_circumscribed = radius_circumscribed_pentagon(side_length)

print(f"Радіус кола, вписаного в п'ятикутник зі стороною {side_length}: {r_inscribed}")
print(f"Радіус кола, описаного навколо п'ятикутника зі стороною {side_length}: {r_circumscribed}")
