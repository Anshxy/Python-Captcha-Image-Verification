import secrets
from captcha.image import ImageCaptcha
import secrets
import string
import os


# had a problem where capital letters were too hard to differentiate so I made it so that it doesn't matter it so its all lowercase.
a_n = string.ascii_letters.lower()
 
# Create an image instance of the given size
image = ImageCaptcha(width = 280, height = 90)

# Generate a random string of length 6

random_string = ''.join(secrets.choice(a_n) for i in range(6))
# Generate the captcha
data = image.generate(random_string)

# Write the captcha to a file
image.write(random_string, 'captcha.png')




while True:
    # print(random_string)
    text = input("Write the text from the image (Or Type 'skip' to generate a new Captcha): ")

    if text.lower() == "skip":
        print("Generating a new Captcha...")
        random_string = ''.join(secrets.choice(a_n) for i in range(6))
        data = image.generate(random_string)
        image.write(random_string, 'captcha.png')
    elif text.lower() != random_string:
        print(False)
    # If the user types the correct text, break the loop.
    elif text.lower() == random_string:
        print(True)
        os.remove("captcha.png")
        break
    
