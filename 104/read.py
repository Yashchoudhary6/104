import cv2
img=cv2.imread("solar-system.jpg")
text="Sun"
cv2.putText(img,text,(100,150),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(25,25,255))
text1="Mercury"
cv2.putText(img,text1,(120,250),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
text2="venus"
cv2.putText(img,text2,(190,250),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
text3="Earth"
cv2.putText(img,text3,(250,250),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
text4="Mars"
cv2.putText(img,text4,(350,250),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
text5="Jupiter"
cv2.putText(img,text5,(550,400),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
text6="Saturn"
cv2.putText(img,text6,(750,400),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
text7="Uranus"
cv2.putText(img,text7,(950,400),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))
text8="Neptune"
cv2.putText(img,text8,(1100,400),fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))

cv2.imshow("display",img)
cv2.waitKey(00)
