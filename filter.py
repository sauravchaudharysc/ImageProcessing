from PIL import Image,ImageFilter

img = Image.open('./PokeDox/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img1 = img.convert('L')
filtered_img.save("./Blur/blur.png","png")
filtered_img1.save("./Blur/format.png","png")
filtered_img.show()
filtered_img1.show()