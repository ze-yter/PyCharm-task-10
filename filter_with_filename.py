from PIL import Image
import numpy as np


def make_color(new_matrix, matrix, size, i, j):
    for x in range(i, i + size):
        for y in range(j, j + size):
            for z in range(3):
                matrix[x][y][z] = new_matrix


def create_mosaic_img(img, size, grad):
    list_img = np.array(Image.open(img)).astype(int)
    limit = 255 // grad
    len_img = len(list_img)
    height = len(list_img[0])
    i = 0

    while i < len_img:
        j = 0
        while j < height:
            part = list_img[i: size + i, j: size + j]
            sum = np.sum(part)
            avg = int(sum // (size ** 2))
            make_color(int(avg // limit) * limit / 3, list_img, size, i, j)
            j += size
        i += size

    return Image.fromarray(np.uint8(list_img))


create_mosaic_img('img2.jpg', 10, 50).save('noinput.jpg')