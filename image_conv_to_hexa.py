from PIL import Image

img = Image.open('101.jpg').convert('L')  


data = list(img.getdata()) 
#print(data)
print(type(data))
b=[]
for item in data:
    b.append(hex(item))
print ("List in proper method", '[%s]' % ', '.join(map(str, b)))
print(b)
with open("b.txt", 'a') as f:
        writer = f.write(str(b))
        f.close()
   
print(type(b))    
 

