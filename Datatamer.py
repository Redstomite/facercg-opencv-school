import os
dst = ""
src = ""
def main():
    i = 4
    for filename in os.listdir("C:/Users/Rahul/Desktop/skule/dataset/"):
        print (filename)
        dst = "User." + str(i) + ".1" + ".jpg"
        dst = os.path.join(os.path.dirname("dataset/"),dst)
        src = os.path.join(os.path.dirname("dataset/"),filename)
        print(src, dst)
        os.rename(src, dst)
        i += 1



main()
