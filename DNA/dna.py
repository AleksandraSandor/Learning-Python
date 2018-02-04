#!/usr/bin/python3.5
from modules import load_file, save_file, load_file_char, save_file_char
import sys
import time

if len(sys.argv) > 1:
	file_name = sys.argv[1]
else:
	file_name = "data.txt"

attempts = 1
dna1 = load_file(file_name)
convert_time = dna1[1]
dna1 = dna1[0]
print("-------")
dna2 = []
start_time_1 = 0
all_times_1 = 0
for _ in range(attempts):
	dna2 = [] # tylko po to aby do pliku nie zapisywał x prób
	start_time_1 = time.time()
	for d in dna1:
		if d == 65:
			dna2.append(84)
		if d == 84:
			dna2.append(65)
		if d == 71:
			dna2.append(67)
		if d == 67:
			dna2.append(71)
		if d == 10:
			dna2.append(10)
	all_times_1 += time.time() - start_time_1
print("Poczatkowe 10 aminokwasów 1 łańcucha: \t\t\t", end='')
for d in dna1[:10]:
	sys.stdout.write(chr(d))
print("\nPoczatkowe 10 aminokwasów 2 łańcucha: \t\t\t", end='')
for d in dna2[:10]:
	sys.stdout.write(chr(d))
print("\n", "\bCzas konwersji {} prób sposób 1: \t\t\t{:1.4f}s".format(attempts, all_times_1 + convert_time))
save_file(file_name + ".out", dna2)


dna3 = load_file_char(file_name)
print("-------")
dna4 = ""
start_time_2 = 0
all_times_2 = 0
dict_my1 = {"A": "T", "G": "C"}
dict_my2 = {"T": "A", "C": "G"}
for _ in range(attempts):
	dna4 = "" # tylko po to aby do pliku nie zapisywał x prób
	start_time_2 = time.time()
	for d in dna3[:-1]:
		if d in dict_my1:
			dna4 += dict_my1[d]
		else:
			dna4 += dict_my2[d]
	dna4 += "\n"
	all_times_2 += time.time() - start_time_2
print("Poczatkowe 10 aminokwasów 1 łańcucha: \t\t\t", end='')
for d in dna3[:10]:
	sys.stdout.write(d)
print("\nPoczatkowe 10 aminokwasów 2 łańcucha: \t\t\t", end='')
for d in dna4[:10]:
	sys.stdout.write(d)
print("\n", "\bCzas konwersji {} prób sposób 2: \t\t\t{:1.4f}s".format(attempts, all_times_2))
save_file_char(file_name + ".out2", dna4)


dna5 = load_file_char(file_name)
print("-------")
dna6 = ""
start_time_2 = 0
all_times_2 = 0
dict_my = {"A": "T", "G": "C", "T": "A", "C": "G", "\n": "\n"}
for _ in range(attempts):
	dna6 = "" # tylko po to aby do pliku nie zapisywał x prób
	start_time_2 = time.time()
	for d in dna5:
		dna6 += dict_my[d]
	all_times_2 += time.time() - start_time_2
print("Poczatkowe 10 aminokwasów 1 łańcucha: \t\t\t", end='')
for d in dna5[:10]:
	sys.stdout.write(d)
print("\nPoczatkowe 10 aminokwasów 2 łańcucha: \t\t\t", end='')
for d in dna6[:10]:
	sys.stdout.write(d)
print("\n", "\bCzas konwersji {} prób sposób 3: \t\t\t{:1.4f}s".format(attempts, all_times_2))
save_file_char(file_name + ".out3", dna6)


import datetime as dt

def log_time(message, time=None):
    if time is None:
        time=dt.datetime.now()
    print("{0}: {1}".format(time.isoformat(), message))
    

message = "Test"
time=dt.datetime.now()
print("{0}: {1}".format(time.isoformat(), message))