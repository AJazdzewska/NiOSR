#!/usr/bin/env python3

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
import tkinter as tk


class Turtle:
	def __init__(self):
		self.node = Node("t_node")
		self.publisher = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
	def window(self):
		window=tk.Tk()
		window.geometry("450x300+10+10")
		window.title('Wybrany punkt')
		window.canvas = tk.Canvas(window, bg = "white", width = 450, height = 300)
		window.canvas.pack()
		window.canvas.bind("<Button-1>", self.control)
		window.mainloop()
	def control(self, event):
		move = Twist()
		move.linear.x=0.0
		speed=1.0
		if event.y < 150:
			move.linear.y = speed
		else:
			move.linear.y = -speed
		self.publisher.publish(move)		

def main():
	rclpy.init()
	turtle = Turtle()
	turtle.window()
	turtle.control()
	rclpy.spin(turtle.node)
	turtle.node.destroy_node()
	rclpy.shutdown()

if __name__=='__main__':
	main()

