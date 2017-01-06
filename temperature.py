#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Creation:    02.01.2013
# Last Update: 07.04.2015
#
# Copyright (c) 2013-2015 by Georg Kainzbauer <http://www.gtkdb.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#

# import sys module
import sys

# open 1-wire slaves list for reading
file = open('/sys/devices/w1_bus_master1/w1_master_slaves')

# read 1-wire slaves list
w1_slaves = file.readlines()

# close 1-wire slaves list
file.close()

# print header for results table

# repeat following steps with each 1-wire slave
for line in w1_slaves:

  # extract 1-wire slave
  w1_slave = line.split("\n")[0]

  # open 1-wire slave file
  file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')

  # read content from 1-wire slave file
  filecontent = file.read()

  # close 1-wire slave file
  file.close()

  # extract temperature string
  stringvalue = filecontent.split("\n")[1].split(" ")[9]

  # convert temperature value
  temperature = float(stringvalue[2:]) / 1000

  # print temperature
  print(str() + "%.1f" % temperature)
  #print temperature


# quit python script
sys.exit(0)
