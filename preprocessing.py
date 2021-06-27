import cv2 
import numpy as np 
import os
import os.path
"""
    Inputs:
        Raw valve seat Image files.

    Returns:
        preprocessed images that maksed and cropped.
        sav_iSize 크기의 1구간 사진.
        1구간을 제외한 다른 부분은 검은색 마스킹 처리
"""

sav_iSize = 128

PATH = 'C:\\Users\\Seungchan_HCI\\OneDrive - inha.edu\\HCI\\valve_seat\\정상\\'
PATH = 'C:\\Users\\Seungchan_HCI\\Desktop\\Nuts\\Nuts_preprocessed\\NORMAL\\'
# PATH = 'C:\\Users\\Seungchan_HCI\\Desktop\\Nuts\\Nuts_preprocessed\\dd\\'
PATH = 'C:\\Users\\Seungchan_HCI\\Desktop\\Nuts\\Nuts_preprocessed\\2\\0208\\purified\\normal\\'
PATH = 'C:\\Users\\Seungchan_HCI\\Desktop\\Nuts\\Nuts_preprocessed\\2\\0208\\purified\\abnormal\\'
PATH = 'C:\\Transfer\\'

PREFIX_BMP = '.bmp'
PREFIX_PNG = '.png'

directory = PATH + 'cropped'
try:
    if not os.path.exists(directory):
        os.makedirs(directory)
except OSError:
    pass


def prnFile(rootDir, prefix):
    files = os.listdir(rootDir)
    tmp = []
    for file in files:
        path = os.path.join(rootDir, file)
        if(file[-4:] == prefix):
            tmp.append(path)
    return tmp

def img_Contrast(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8,8))
    cl = clahe.apply(l)

    limg = cv2.merge((cl, a, b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return final

fail_list = []

imSizeX = 1280
imSizeY = 720
imCenter = 55+610/2

xBias = 280
yBias = 0

k = 0
for filePath in prnFile(PATH, PREFIX_BMP):
    k += 1
    raw = cv2.imread(filePath, cv2.IMREAD_COLOR) 
    imSize = 720
    img = raw[yBias:yBias+imSize, xBias:xBias+imSize]
    img = img_Contrast(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    # Blur using 3 * 3 kernel. 
    gray_blurred = cv2.blur(gray, (3, 3)) 
    
    # Apply Hough transform on the blurred image. 
    detected_circles = cv2.HoughCircles(gray_blurred,  
                       cv2.HOUGH_GRADIENT, 1.5, 1270, param1 = 70, 
                   param2 = 40, minRadius = 315, maxRadius = 324) 
    # Draw circles that are detected. 
    if detected_circles is not None: 
    
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            a += xBias
            b += yBias
            backGD_circle = np.zeros((imSizeY,imSizeX, 3), dtype="uint8")
            cv2.circle(backGD_circle, (a, b), r, (255,255,255), -1) 
            
            rectX = (a - r) 
            rectY = (b - r)

            raw = cv2.bitwise_and(backGD_circle, raw)
            img = raw[rectY:(rectY+2*r), rectX:(rectX+2*r)]
           

    
    # Draw circles that are detected. 
    if detected_circles is not None: 
    
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
                        
            a += xBias
            b += yBias

            backGD_circle = np.zeros((imSizeY,imSizeX, 3), dtype="uint8")
            cv2.circle(backGD_circle, (a, b), r, (255,255,255), -1) 
            
            rectX = (a - r) 
            rectY = (b - r)

            raw = cv2.bitwise_and(backGD_circle, raw)
            img = raw[rectY:(rectY+2*r), rectX:(rectX+2*r)]
            
            print(f'{os.path.basename(filePath)} saved')
            cv2.imwrite(PATH + 'cropped\\' + os.path.basename(filePath)[:-4] + PREFIX_PNG, img)
    else:
        fail_list.append(k)
        
print(f'failed: {fail_list}') 