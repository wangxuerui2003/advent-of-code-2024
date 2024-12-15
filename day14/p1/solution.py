from dataclasses import dataclass
import re
import math

WIDTH = 101
HEIGHT = 103
SECONDS = 100
# WIDTH = 11
# HEIGHT = 7

@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int

robots: list[Robot] = []

def get_quadrant(x, y):
    middle = x == WIDTH // 2 or y == HEIGHT // 2
    if middle:
        return -1
    left = x < WIDTH // 2
    top = y < HEIGHT // 2
    if left and top:
        return 0
    elif not left and top:
        return 1
    elif left and not top:
        return 2
    return 3

with open("input.txt", 'r') as f:
    lines = f.readlines()
    pattern = "p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    for line in lines:
        match = re.match(pattern, line)
        px, py, vx, vy = map(int, match.groups())
        robots.append(Robot(px=px, py=py, vx=vx, vy=vy))

quadrant_robots = [0, 0, 0, 0]

for robot in robots:
    robot.px = (robot.px + robot.vx * SECONDS) % WIDTH
    if robot.px < 0:
        robot.px = WIDTH + robot.px
    robot.py = (robot.py + robot.vy * SECONDS) % HEIGHT
    if robot.py < 0:
        robot.py = HEIGHT + robot.py
    quadrant = get_quadrant(robot.px, robot.py)
    if quadrant == -1:
        continue
    quadrant_robots[quadrant] += 1


print(math.prod(quadrant_robots))