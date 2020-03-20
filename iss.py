#!/usr/bin/env python

__author__ = 'DavidRinSE'

import requests
import turtle
import time


def in_space():
    r = requests.get('http://api.open-notify.org/astros.json')
    space = r.json()
    for astro in space["people"]:
        print(astro["name"] + ",", astro["craft"])
    print(f"{space['number']} people in space")


def iss_coords():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    location_obj = r.json()
    return location_obj


def indy_time():
    r = requests.get(
        "http://api.open-notify.org/iss-pass.json?lat=39.768&lon=-86.158")
    pass_res = r.json()
    return time.ctime(pass_res["response"][1]["risetime"])


def start_turtle():
    screen = turtle.Screen()
    screen.setup(710, 360)
    screen.bgpic("./map.gif")
    screen.reset()
    screen.setworldcoordinates(-170, -85, 180, 90)
    screen.addshape("iss.gif")
    screen.title("ISS Tracker - Update every 10s")
    turtle.shape("iss.gif")
    turtle.penup()

    turtle.goto(-65, 70)
    turtle.color("red")
    turtle.write(indy_time(), font=("Arial", 20, "bold"))

    turtle.goto(float(-86.158), float(39.768))
    turtle.dot(5, 'yellow')

    while True:
        iss = iss_coords()
        coords = iss["iss_position"]
        turtle.goto(float(coords["longitude"]), float(coords["latitude"]))
        time.sleep(10)


def main():
    in_space()
    indy_time()
    start_turtle()


if __name__ == '__main__':
    main()

# 39.7684 lat
# 86.1581 lon
