def read_csv_data(file_name, skip=1, samples=120, sep=','):
    data = []
    with open(file_name) as csv_file:
        first =  csv_file.readline()
        if len(first) == 0:
            return data
        rows = 1
        cols = len(first.split(sep))
        while csv_file.readline():
            rows += 1
    data = list([0]*samples for i in range(cols))
    print(len(data), len(data[0]))
    with open(file_name) as csv_file:
        for i in range(samples):
            for _ in range(skip):
                row = csv_file.readline().strip()
            data_row = [float(item) for item in row.split(sep)]
            for j in range(cols):
                data[j][i] = data_row[j]

    return data

