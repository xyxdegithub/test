# -*- coding = utf-8 -*-
# @Time : 2022/3/17 13:01
# @Author : 谢扬筱
# @File : voc2yolo.py

#把用xml标注的转化成yolo格式
from bs4 import BeautifulSoup
import os
import shutil

id = {"without_mask": 0, "mask_weared_incorrect": 1, "with_mask": 2}
def getYoloFormat(filename,label_path, img_path, yolo_path, newname):
    with open(label_path + filename, 'r') as f:
        soup = BeautifulSoup(f.read(), 'xml')
        imgname = soup.select_one('filename').text
        image_w = int(soup.select_one('width').text)
        image_h = int(soup.select_one('height').text)
        ary = []
        for obj in soup.select('object'):
            xmin = int(obj.select_one('xmin').text)
            xmax = int(obj.select_one('xmax').text)
            ymin = int(obj.select_one('ymin').text)
            ymax = int(obj.select_one('ymax').text)
            objclass = id.get(obj.select_one('name').text)

            x = (xmin + (xmax - xmin) / 2) * 1.0 / image_w
            y = (ymin + (ymax - ymin) / 2) * 1.0 / image_h
            w = (xmax - xmin) * 1.0 / image_w
            h = (ymax - ymin) * 1.0 / image_h
            ary.append(' '.join([str(objclass), str(x), str(y), str(w), str(h)]))
        if os.path.exists(img_path + imgname):
            shutil.copyfile(img_path + imgname, yolo_path + newname + '.png')
            with open(yolo_path + newname + '.txt', 'w') as f:
                f.write('\n'.join(ary))


if __name__ == '__main__':
    labelpath = 'E://数据//voc2yolo-dataset//annotations//'
    imgpath   = 'E://数据//voc2yolo-dataset//images//'
    yolopath  = 'E://数据//voc2yolo-dataset//yolo//'
    ary = []
    for idx, f in enumerate(os.listdir(labelpath)):
        try:
            getYoloFormat(f, labelpath,imgpath, yolopath, str(idx))
        except Exception as e:
            print(e)