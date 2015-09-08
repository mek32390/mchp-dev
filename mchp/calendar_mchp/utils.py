import math
import random
import webcolors


def calculate_color_distance(color1, color2):
    red = math.pow(color1[0]-color2[0], 2)
    blue = math.pow(color1[1]-color2[1], 2)
    green = math.pow(color1[2]-color2[2], 2)
    return math.sqrt(red+blue+green)


def generate_calendar_color(calendars, threshold=50, max_attempts=100):
    colors = []
    for calendar in calendars:
        rgb = webcolors.hex_to_rgb(calendar.color)
        colors.append(rgb)

    # Picking color
    picking_color = True
    attempt = 0
    while picking_color and attempt < max_attempts:
        attempt += 1
        candidate_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        picking_color = False
        for color in colors:
            if calculate_color_distance(candidate_color, color) < threshold:
                picking_color = True
                break
    return webcolors.rgb_to_hex(candidate_color)
