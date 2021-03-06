#!/usr/bin/env python3

#    Copyright (c) 2018 Vladimir Shchur (vlshchur@gmail.com)
#
#    This file is part of MiSTI.
#
#    MiSTI is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MiSTI is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with MiSTI.  If not, see <https://www.gnu.org/licenses/>.


import sys

if len(sys.argv) < 3:
    print("./MSSPLIT.py <INPUT FILE> <DESTINATION FOLDER>")
    exit(0)

fn = sys.argv[1]
dest = sys.argv[2]

fnw1 = dest + "/ms2g1.ms"
fnw2 = dest + "/ms2g2.ms"
fw1 = open(fnw1, 'w')
fw2 = open(fnw2, 'w')

with open(fn) as f:
    for line in f:        
        for _ in range(2):
            fw1.write(line)
            fw2.write(line)
            line = next(f)
        chrLen = int( next(f) )
        lc = 0
        f1 = []
        f2 = []
        while 1:
            line = next(f)
            lc += 1
            if lc > int(chrLen):
                print("Too many segsites, expected at most " + str(chrLen))
                sys.exit(0)
            if line == "@end\n":
                break
            line = line.split("\t")
            if line[1][0] != line[1][1]:
                f1.append( line[0] )
            if line[1][2] != line[1][3]:
                f2.append( line[0] )
        fw1.write("@begin " + str( len(f1) ) + "\n" )
        fw1.write( str(chrLen) + "\n" )
        for val in f1:
             fw1.write( val + "\t10" + "\n" )
        fw1.write("@end\n")
        
        fw2.write("@begin " + str( len(f2) ) + "\n" )
        fw2.write( str(chrLen) + "\n" )
        for val in f2:
             fw2.write( val + "\t10" + "\n" )
        fw2.write("@end\n")
fw1.close()
fw2.close()
