import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

#image resize
def resize_image(image, new_width=150):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio * 0.6)
    resized_image = image.resize((new_width, new_height))

    return(resized_image)

#pixels to grayscale
def grayscale(image):
    grayscale_image = image.convert("L")

    return(grayscale_image)
    
#pixels to ascii string
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//22] for pixel in pixels])

    return(characters)

def main(new_width=150):
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")

        return
  
    #image to ascii    
    new_image_data = pixels_to_ascii(grayscale(resize_image(image)))
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    #print result
    print(ascii_image)
    
    #save result
    res_path = path.split('.')[0] + ".txt"
    with open(res_path, "w") as f:
        f.write(ascii_image)
 
main()