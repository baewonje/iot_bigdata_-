import os


def search(dirname):
    filename = os.listdir(dirname)

    for filename in filename:
        full_filename = os.path.join(dirname, filename)
        print(full_filename)

search("C:/")