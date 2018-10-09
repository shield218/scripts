from PIL import Image
import sys
import os

# fill image to a square with white if width!=height 
def fill_image(image):
 
	width,height=image.size
	print(width,height)
 
	new_image_length=width if width>height else height
 
	print(new_image_length)
 
	new_image=Image.new(image.mode,(new_image_length,new_image_length),color='white')
	
	if width>height:
 
		new_image.paste(image,(0,int((new_image_length-height)/2)))
	else:
		new_image.paste(image,(int((new_image_length-width)/2),0))
	return new_image

#cut images, v,h is the number of vertical and horizonal slices w.r.t
def cut_image(image,vslice,hslice):
	width,height=image.size
	width_sliced=width/vslice
	height_sliced=height/hslice
	box_list=[]
	count=0
	for v in range(0,vslice):
		for h in range(0,hslice):
			count+=1
			box=(v*width_sliced,h*height_sliced,(v+1)*width_sliced,(h+1)*height_sliced)
			box_list.append(box)
	print(count)
	image_list=[image.crop(box) for box in box_list]
	return image_list
 
def save_images(imgcnt, image_list,path,subdir):
	index=1
	for image in image_list:
		image.save(path+'sliced/'+subdir+str(format(index+imgcnt,'0>6d'))+'_10.png')
		index+=1

if __name__ == '__main__':
	path='/home/chu/scene_flow/temp/'
	ldir='image_2/'
	rdir='image_3/'
	lname=os.listdir(path+ldir)
	rname=os.listdir(path+rdir)
	imgcnt=0

	vslice=1
	hslice=3

for i in range(0,len(lname)):
	# left 
	limage=Image.open(path+ldir+lname[i])
	limage_list=cut_image(limage,vslice,hslice)
	save_images(imgcnt,limage_list,path,ldir)

	# right
	rimage=Image.open(path+rdir+rname[i])
	rimage_list=cut_image(rimage,vslice,hslice)
	save_images(imgcnt,rimage_list,path,rdir)

	imgcnt+=vslice*hslice