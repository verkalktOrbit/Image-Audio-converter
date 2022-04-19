# encode-decode-Images
This is the algotrithm for the glcodes.one project. 
The algorithm takes an Mp3 file as input and converts the bytes of the File into RGB values. These Values will be stored in an png. Furthermore, the Images can be converted back into the original data.
The Project is ready to be used and an audio file is already in the project. You must first run soundToImage.py to create the Image. The Image will be stored in the Image folder. Then you can run ImageToSound.py to convert the Image back into the mp3 file.
The code is commented, if you are interested in understanding it

The key princible is that 1 byte = 2 hex = 256 dec | the max value of a rgb value is 256 ==> 3 Bytes can be converted into one pixel
