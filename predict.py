from model import GoogLeNet
from PIL import Image
import numpy as np
import json
import matplotlib.pyplot as plt


def prediction(img):
    im_height = 224
    im_width = 224
    car_types = 4
    # 读入图片
    #
    # img = Image.open("C:/Users/a3513/Desktop/truck.jpg")  # 这是我的路径，要根据自己的根目录来改
    # resize成224x224的格式
    img = img.resize((im_width, im_height))
    plt.imshow(img)
    # 对原图标准化处理
    img = ((np.array(img) / 255.) - 0.5) / 0.5
    # Add the image to a batch where it's the only member.
    img = (np.expand_dims(img, 0))
    # 读class_indict文件
    try:
        json_file = open('./car_class_indices.json', 'r')
        class_indict = json.load(json_file)
    except Exception as e:
        print(e)
        exit(-1)
    model = GoogLeNet(class_num=car_types, aux_logits=False)  # 重新构建网络
    model.summary()
    model.load_weights("./car_save_weights/car_myGoogLeNet.h5", by_name=True)  # 加载模型参数
    # model.load_weights("./save_weights/myGoogLeNet.ckpt")  # ckpt format
    result = model.predict(img)
    predict_class = np.argmax(result)
    print('预测出的类别是：', class_indict[str(predict_class)])  # 打印显示出预测类别

    result={'v_type':class_indict[str(predict_class)]}
    return result
