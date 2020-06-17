import csv


# Returns the landmarks for the nth face in the dataset as an array
def one_face(n):

    landmarks = []

    # open a file for writing
    with open('muct76.csv') as muctData:

        csv_reader = csv.reader(muctData)
        for row in csv_reader:
            if n == 0:
                break
            n -= 1
        landmarks.append(row)

    return landmarks


# Returns the nth x and y coordinate for all faces in the data set
def all_faces(n):

    xpoint = []
    ypoint = []

    # open a file for writing
    with open('muct76.csv') as muctData:
        csv_reader = csv.reader(muctData)
        for row in csv_reader:
            assert len(row) >= 2*n + 3
            loc = 2*n + 2
            xpoint.append(row[loc])
            ypoint.append(row[loc + 1])

    return xpoint, ypoint

