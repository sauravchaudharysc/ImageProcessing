from PIL import Image

filtered_img = Image.open('./PokeDox/pikachu.jpg')
print("Choose your desired rotation")
print("1.90")
print("2.180")
print("3.270")
print("4.360")
x = int(input())
if x==1 :
	rotated = filtered_img.rotate(90)
elif x==2 :
	rotated = filtered_img.rotate(180)
elif x==3 :
	rotated = filtered_img.rotate(270)
elif x==4 :
	rotated = filtered_img.rotate(360)
else :
	print("Choose your option carefully")


rotated.save("./Rotation/rotated.png","png")
rotated.show()
