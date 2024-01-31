from PIL import Image
from matplotlib import pyplot as plt

def convolution(image, kernel):
    width, height = image.size
    image_grise = image.convert('L')
    image_conv = Image.new('L', (width, height))

    for x in range(1, width - 1):  
        for y in range(1, height - 1):  
            somme = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    val = image_grise.getpixel((x + k, y + l))
                    somme += val * kernel[k + 1][l + 1]
            somme = min(max(int(somme), 0), 255)
            image_conv.putpixel((x, y), somme)

    return image_conv

chemin_image = 'image.jpg'
image = Image.open(chemin_image)

kernel_blur = [[1/9, 1/9, 1/9],
               [1/9, 1/9, 1/9],
               [1/9, 1/9, 1/9]]

image_convolutee = convolution(image, kernel_blur)
image_convolutee.show()

