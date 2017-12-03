#!/usr/bin/python3

# todo exit if not python3

import os
import sys
import os.path
import calendar
from datetime import date, timedelta

ENDC = '\033[0m'
BOLD = '\033[1m'
WARNING = '\033[93m'

highlight = lambda num: \
        lambda x: \
            x.replace(f' {num} ', WARNING + BOLD + f' {num} ' + ENDC) \
             .replace(f' {num}\n', WARNING + BOLD + f' {num}\n' + ENDC) \
             .replace(f'\n{num} ', WARNING + BOLD + f'\n{num} ' + ENDC)

# switch to the path of the script
script_path = os.path.dirname(sys.argv[0])
if script_path != '':
    os.chdir(script_path)

csvs = list(map(lambda x: x[:-4], filter(lambda x: x.endswith('.csv'), os.listdir())))

last = csvs[-1].split('-')
last_date = date(int(last[0]), int(last[1]), 1)
new_date = last_date + timedelta(days=35)
new_date = date(new_date.year, new_date.month, 1)

ff_days = []

filename = f'{new_date.year}-{str(new_date.month).zfill(2)}.csv'
print(f"writing to file: {filename}:\n")

with open(filename, 'x') as f:
    sunday_cnt = 0
    # walk through days
    for d in range(1, 1+calendar.monthrange(new_date.year, new_date.month)[1]):
        day = date(new_date.year, new_date.month, d)

        anlass = "Arbeitstreffen"
        ort = "Computerwerkstatt"
        time = "19-00"

        if day.weekday() == calendar.THURSDAY:
            pass
        elif day.weekday() == calendar.SUNDAY:
            time = "17-00"
            anlass = "Newbie-Treffen"

            sunday_cnt += 1
            if sunday_cnt % 2 != 0:
                continue
        else:
            continue

        ff_days += [d]
        print(f"{anlass};{ort};{day}-{time}", file=f)
        print(f"{anlass};{ort};{day}-{WARNING}{time}{ENDC}")


    print()
    pretty = calendar.month(new_date.year, new_date.month)
    for d in ff_days:
        pretty = highlight(d)(pretty)

    print(pretty)
