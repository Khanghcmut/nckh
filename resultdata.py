import csv
def result_file_csv(n):
    print(f'{n:02d}')
    file=f'/Users/khangphan/Desktop/nckh_sv/data/gps_u{n:02d}.csv'
    # Read the first file
    with open('/Users/khangphan/Desktop/nckh_sv/data/gps_result.csv', 'r') as f1:
        reader1 = csv.reader(f1)
        header1 = next(reader1)
        data1 = [row for row in reader1]

    # Read the second file
    with open(file, 'r') as f2:
        reader2 = csv.reader(f2)
        header2 = ['tnv']+next(reader2)
        data2 = [[n+1]+row for row in reader2]
    data=data1+data2
    # Check that headers match
    if header1 != header2:
        raise ValueError('Headers do not match')

    # Write the result to a new file
    with open('/Users/khangphan/Desktop/nckh_sv/data/gps_result.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header1)
        writer.writerows(data)
def first_result_file(n):
    file=f'/Users/khangphan/Desktop/nckh_sv/data/gps_u{n:02d}.csv'
    with open(file, 'r') as f2:
        reader2 = csv.reader(f2)
        header2 = ['tnv']+next(reader2)
        data2 = [[n+1]+row for row in reader2]
    data=data2
    # Write the result to a new file
    with open('/Users/khangphan/Desktop/nckh_sv/data/gps_result.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header2)
        writer.writerows(data)
first_result_file(0)
for i in range(1,60):
    try:
        result_file_csv(i)
        print(f'add file no {i} done')
    except: print(f'file stt {i} khong ton tai')