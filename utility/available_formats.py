# (?) Dictionary structure
#     Format name:
#       Extensions      | Associated extensions: [1...N]
#       Transformations | Formats, to which can be converted to: [0...N]   *Key of different format
formats = {
    "PNG":
        {
            "extensions": [".png"],
            "transformations": ["JPEG", "BMP", "ICO"],
        },
    "JPEG":
        {
            "extensions": [".jpg", ".jpeg"],
            "transformations": ["PNG", "BMP"],
        },
    "BMP":
        {
            "extensions": [".bmp"],
            "transformations": ["JPEG", "PNG"],
        },
    "ICO":
        {
            "extensions": [".ico"],
            "transformations": None,
        }
}
