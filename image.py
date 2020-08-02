from PIL import Image

img = Image.open('./PokeDox/pikachu.jpg')
print("The format of image is "+img.format)
print("The size of image is ")
print(img.size)
print("The color of image is "+img.mode)