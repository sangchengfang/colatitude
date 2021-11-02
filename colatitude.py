#!/usr/bin/env python3

import sys


def colatitude(in_filename, out_filename, file_code):
    in_filename = str(in_filename)
    out_filename = str(out_filename)
    file_code = str(file_code)

    if file_code == 'coorfile':
        lon_col = 0
        lat_col = 1
        row_len = 2
    elif file_code == 'gpsfile':
        lon_col = 1
        lat_col = 2
        row_len = 3
    else:
        print('wrong file code')
        sys.exit()

    with open(in_filename, 'r') as fip, open(out_filename, 'w') as fop:
        for line in fip.readlines():
            lat = line.split()

            # with open(OutFilename,'w') as colat_results:
            if lat[0] != '#':
                fop.write(str(format(float(lat[lon_col]), '.2f')).ljust(8))
                if len(lat) > row_len:
                    fop.write(str(format(90.00 - float(lat[lat_col]), '.2f')).ljust(8))
                    for item in lat[lat_col+1:]:
                        fop.write(str(item).ljust(10))
                    fop.write('\n')
                else:
                    fop.write(str(format(90.00 - float(lat[lat_col]), '.2f')) + '\n')


def main():
    colatitude('coor.dat', 'coor_colat.dat', 'coorfile')


if __name__ == '__main__':
    main()
