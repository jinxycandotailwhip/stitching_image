# stitching_image
程序实现了输入两幅图像进行拼接的任务。
Stitcher.py定义了 Stitcher类
stitch()方法实现了两个图像的拼接
detectAndDescribe()方法实现了sift描述子的建立
matchKeypoints()方法实现了特征点的匹配

image_stitching.py实例化并使用Stitcher类进行拼接



注意:使用python3，opencv3.4.2.16
     图像的输入顺序为从左到右
     显示module 'cv2.cv2' has no attribute 'xfeatures2d' 错误解决
     报错原因：sift算法已经申请专利，开源OpenCV没有版权，新的OpenCV去掉了这个算法。
     解决方法：卸掉目前的包，安装3.4.2.16版本
     pip uninstall opencv-python
     pip install opencv-python==3.4.2.16
     pip install opencv-contrib-python==3.4.2.16
     
     图像像素过多显示不全的话可以在文件夹路径下查看保存的拼接图像
