from PIL import Image


# Open image
def openImage(pathToImage):
    image = Image.open(pathToImage)
    return image


# Save image
def saveImage(imageToSave, imageName, oldExtension, newExtension, pathToSave):
    print("!",imageName, newExtension, pathToSave)
    print("SAVE",pathToSave+"\\"+imageName+newExtension)

    imageToSave = imageToSave.convert('RGB')
    imageToSave.save(pathToSave+"\\"+imageName+newExtension)

    print("DONE")
