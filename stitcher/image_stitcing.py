from Stitcher import Stitcher
import cv2

# 图片读取，从左到右
imageA = cv2.imread("left1.jpg")
imageB = cv2.imread("right1.jpg")

# 图像拼接
stitcher = Stitcher()
result = stitcher.stitch([imageA, imageB])

# 展示
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Result", result)
cv2.imwrite('image_stitched.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
