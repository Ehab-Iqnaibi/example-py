from PIL import Image, ImageFilter
#p1
def picture(img):
    print(img.format)
    print(img.size)
    print(img.mode)

def edit(img):
    small_img=img.crop((0,0,300,200))
    small_img.show()
#p2
def filter_(img):
    blured_img=img.filter(ImageFilter.BLUR)
    edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
    contour_img = img.filter(ImageFilter.CONTOUR)
    blured_img.show()
    edge_img.show()
    contour_img.show()
#p3
def convert_(img):
    grey_img = img.convert("L")
    hsv_img = img.convert("HSV")
    h, s, v = hsv_img.split()
    m= img.merge(h,s,v)
    grey_img.show()
    h.show()
    s.show()
    v.show()
    m.show()
#p4 Image Transformations
def Transformations_(img):
    resized_img = img.resize((200, 300))
    resized_img.show()
    rotated_img = img.rotate(45)
  #  rotated_img.show()
    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    #flipped_img = img.transpose(Transpose.FLIP_TOP_BOTTOM)   error
  #  flipped_img.show()


'''
#p1
img1= Image.open("C:/Users/Ehab M F Iqnaibi/Pictures/Camera Roll/E1.JPG")
picture(img1)
img1.show()

edit(img1)
img1.save("C:/Users/Ehab M F Iqnaibi/Pictures/Camera Roll/E1_new.JPG")

#p2
img2= Image.open("C:/Users/Ehab M F Iqnaibi/Pictures/Saved Pictures/m2.png")
filter_(img2)

#p3 Image Conversion, Splitting
img3 = Image.open("C:/Users/Ehab M F Iqnaibi/Pictures/Saved Pictures/m1.jfif")
convert_(img3)
'''
#p4 Image Transformations
img4 = Image.open("C:/Users/Ehab M F Iqnaibi/Pictures/course/f1.jpg")
'''
Transformations_(img4)

# creating thumbnail
MAX_SIZE = (200, 300)
img4.thumbnail(MAX_SIZE)
img4.show()
'''
#P5 Pointwise Operations
size = img4.size
print(size)
neg_img1 = Image.new('RGB', size)
for i in range(size[0]):
  for j in range(size[1]):
    in_pixel = img4.getpixel((i, j))
    out_pixel = (255-in_pixel[0], 255-in_pixel[1], 255-in_pixel[2])
    neg_img1.putpixel((i, j), out_pixel)

img4.show()
neg_img1.show()
# method 2
neg_img2 = img4.point(lambda i: 255-i)
neg_img2.show()