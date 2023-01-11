#!/usr/bin/python3
from sys import stdin


count = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0


def print_logs():
    ''' prints the logs '''
    global status_codes, total_size
    print('File size: {}'.format(total_size), flush=True)
    for key, val in sorted(status_codes.items(), key=lambda v: v[0]):
        if val:
            print('{}: {}'.format(key, val), flush=True)


def main():
    ''' logs network requests '''
    global count, status_codes, total_size
    try:
        for line in stdin:
            parts = line.strip().split()
            if len(parts) >= 2:
                status_code = parts[-2]
                file_size = parts[-1]
                total_size += int(file_size)
                if status_code in status_codes.keys():
                    status_codes[status_code] += 1
            count += 1
            if count % 10 == 0:
                print_logs()
        print_logs()
    except KeyboardInterrupt:
        print_logs()


if __name__ == '__main__':
    main()
