def copy_odd_lines(ip_file, op_file):
    with open(ip_file, 'r') as ipf:
        with open(op_file, 'w') as opf:
            lines = ipf.readlines()
            for i in range(len(lines)):
                if (i+1) % 2 != 0:
                    opf.write(lines[i])
    print('odd lines copied successfully!')


ip_file = 'ip_file.txt'
op_file = 'op_file.txt'
copy_odd_lines(ip_file, op_file)
