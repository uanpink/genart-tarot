"""
It can be improved a lot, maybe later.

Use it as you wish.

Uan Pink - 2023

"""


import argparse
import random


def read_file(filename: str) -> [str]:
	all_data: str = [];

	with open(filename, "r") as file:
		all_data = file.readlines()

	return all_data


def spit_items(data: [str], numberOfItems: int) -> [str]:

	spitted: str = []
	
	for x in range(numberOfItems):
		rand: int = random.randint(0, len(data)-1)

		spitted.append(data[rand].rstrip())


	return spitted


def show(items: [str]):
	print("+!+!+!+!+ TO SPARK YOUR CREATIVITY +!+!+!+!+")

	for item in items:
		print(item)


parser = argparse.ArgumentParser()
parser.add_argument("--numberOfItems", type=int, default=4, required=False)
args = parser.parse_args()


file_data = read_file("my-texts.txt")
items = spit_items(file_data, args.numberOfItems)

show(items)