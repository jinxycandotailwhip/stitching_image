# stitching_image
程序实现了输入两幅图像进行拼接的任务。
Stitcher.py定义了 Stitcher类\n

stitch()方法实现了两个图像的拼接\n

detectAndDescribe()方法实现了sift描述子的建立\n

matchKeypoints()方法实现了特征点的匹配\n

image_stitching.py实例化并使用Stitcher类进行拼接\n



注意:使用python3，opencv3.4.2.16\n
     图像的输入顺序为从左到右\n
     显示module 'cv2.cv2' has no attribute 'xfeatures2d' 错误解决\n
     报错原因：sift算法已经申请专利，开源OpenCV没有版权，新的OpenCV去掉了这个算法。\n
     解决方法：卸掉目前的包，安装3.4.2.16版本\n
     pip uninstall opencv-python\n
     pip install opencv-python==3.4.2.16\n
     pip install opencv-contrib-python==3.4.2.16\n
     图像像素过多显示不全的话可以在文件夹路径下查看保存的拼接图像\n
