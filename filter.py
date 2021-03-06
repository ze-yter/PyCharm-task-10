from PIL import Image
import numpy as np


def make_color(new_matrix, matrix, size, i, j):
    """
    Принимает на вход новую матрицу (матрицу изображения),
    Матрицу первоначальную,
    Размер и количество градаций серого,
    Индексы текущего пикселя,
    По итогу изменяет гамму изображения для заданного размера матрицы.
    """
    for x in range(i, i + size):
        for y in range(j, j + size):
            for z in range(3):
                matrix[x][y][z] = new_matrix


def create_mosaic_img(img, size, grad):
    """
    Принимает на вход начальное изображение,
    Размер и количество градаций серого,
    Возвращает обратно преобразованное изображение.
     >>> create_mosaic_img('images/img2.jpg', 10, 50)
    """
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


create_mosaic_img(input("Enter the name of the image file: "),
                  int(input("Enter the size of the mosaic: ")),
                  int(input("Enter the size of the gradation: "))).save('goodresult.jpg')