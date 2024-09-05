from PIL import Image

img = Image.open('emir.jpg')

new_width = img.width 
new_height = int(img.height * 2.6)

resized_img = img.resize((new_width, new_height))

resized_img.save('taller_emir.jpg')
