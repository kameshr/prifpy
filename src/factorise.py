#!/usr/bin/python3

# Copyright 2019 Kamesh Raghavendra
# All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# File: factorise.py
# Description: Sample wrapper program for prifpy from command line

import prifpy
import sys

print("Welcome to prime factorization!\n")
try:
	num = int(input("Enter the number to be prime factorized: "))
except:
	print(prifpy.ERRORCOLOR + "[ERROR] Wrong input. Please try again with an interger number greater than 1.\n" + prifpy.LOSECOLOR)
	sys.exit()

if not(isinstance(num, int)) or num <= 1:
	print(prifpy.ERRORCOLOR + "[ERROR] Wrong input '" + str(num) + "'. Please try again with an integer number greater than 1.\n" + prifpy.LOSECOLOR)
	sys.exit()

prifpy.printprifac(prifpy.prifac(num))
