#!/usr/bin/python3

import sys
count = 0
filesize = 0
possible_stat_code = {"200": 0, "301": 0, "400": 0,
                      "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for line in sys.stdin:
        elements = line.split(" ")
        if (len(elements) > 4):

            stat_code = elements[-2]
            if (stat_code in possible_stat_code.keys()):
                possible_stat_code[stat_code] += 1

            # print(elements)
            filesize = filesize+(int(elements[-1]))
            if (count == 10):
                print('File size: {}'.format(filesize))
                for key, value in sorted(possible_stat_code.items()):
                    if value:
                        print('{}: {}'.format(key, value))
                count = 0
            count = count+1
except KeyboardInterrupt as err:
    raise

finally:
    print('File size: {}'.format(filesize))
    for key, value in sorted(possible_stat_code.items()):
        if value:
            print('{}: {}'.format(key, value))
