from PIL import Image

img = Image.open('./PokeDox/pikachu.jpg')
resize=img.resize((300,300))
resize.save("./Resize/resize.png",'png')
resize.show()