import cv2
import glob 

for image in glob.glob('*.jpg'): # 반복해라 내가 모아둔 사진 중에 jpg로 끝나는 것을
    
    fname = image # image를 불러와라 
    img_gray = cv2.imread(fname, 0) # 0: gray; 1, RGB; -1: transparency
    img_color = cv2.imread(fname, 1)
    # 이름값
    
    img_gnew = cv2.resize(img_gray, (300, 300))
    img_cnew = cv2.resize(img_color, (300, 300))
    #이미지 사이즈
    
    # cv2.imshow('Gray', img_gray)
    # cv2.imshow('Color', img_color)
    cv2.imshow('Gray', img_gnew)
    cv2.imshow('Color', img_cnew)
    # 흑백/컬러 

    fname_new = image + "_resized.jpg"
    cv2.imwrite(fname_new, img_cnew)
    cv2.waitKey(2000) # 0: press button; 2000: 2 seconds
    cv2.destroyAllWindows()
    # 1000 = 1초 