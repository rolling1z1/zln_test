import pandas as pd
import os
import glob


#train
cvs_path = r'zdataset/images/train'
# txt_train_path = 'train'
# txt_test_path = 'test'

label = ["A10", "AG600", "B1", "B2", "B52", "Be200", "C130", "C17", "C5", "E2", "EF2000", "F117", "F14", "F15", "F16",
         "F18", "F22", "F35", "F4", "J20", "JAS39", "Mi310", "MQ29", "Mirage", "RQ4", "Rafale", "SR71", "A12", "Su57",
         "Tu160", "Tu95", "Tu142", "U2", "US2", "V22", "XB70", "YF23", "MQ9", "Mig31", "Mirage2000"]

# for 循环每个cvs文件并保存为指定目录的TXT文件
cvs_list = files = sorted(glob.glob(os.path.join(cvs_path, '*.csv')))
count = 0
class_num0 = 0
zln_class_tongji = []
for file in cvs_list:
    count = count + 1
    # print(file)
    imgNamePath = file[:-4]
    out_txt_path = os.path.join(imgNamePath + '.txt')  # 保存到csv的目录
    if count <= len(cvs_list):
        df = pd.read_csv(file)

        the_class = df.iloc[0]['class']
        if the_class not in zln_class_tongji:
            # print(df.iloc[0]['class'])
            zln_class_tongji.append(the_class)
        if the_class not in label:
            print("###############")
            print(df.iloc[0]['class'])
            print("###############")

zln_class_tongji = sorted(zln_class_tongji)
print("zln_class_tongji:", zln_class_tongji)


###进行归一化操作
def convert(size, box):
    dw = 1.0 / (size[0])
    dh = 1.0 / (size[1])
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


count = 0
for file in cvs_list:
    count = count + 1
    # print(file)
    imgNamePath = file[:-4]
    out_txt_path = os.path.join(imgNamePath + '.txt')  # 保存到csv的目录
    if count <= len(cvs_list):
        df = pd.read_csv(file)
        w = df.iloc[0]['width']
        h = df.iloc[0]['height']
        the_cls = None
        for i in range(0, len(zln_class_tongji)):
            if df.iloc[0]['class'] == zln_class_tongji[i]:
                the_cls = i

        x_min = df.iloc[0]['xmin']
        y_min = df.iloc[0]['ymin']
        x_max = df.iloc[0]['xmax']
        y_max = df.iloc[0]['ymax']

        out_file = open(out_txt_path, 'w', encoding='UTF-8')  # 以写入的方式打开TXT
        box = convert((int(w), int(h)), (int(float(x_min)), int(float(x_max)), int(float(y_min)), int(float(y_max))))
        out_file.write(str(the_cls) + ' ' + ' '.join([str(round(a, 6)) for a in box]) + '\n')  # 把内容写入TXT中

#test
cvs_path_test = r'zdataset/images/test'
# for 循环每个cvs文件并保存为指定目录的TXT文件
cvs_list_test = files = sorted(glob.glob(os.path.join(cvs_path_test, '*.csv')))
count = 0
for file in cvs_list_test:
    count = count + 1
    # print(file)
    imgNamePath = file[:-4]
    out_txt_path = os.path.join(imgNamePath + '.txt')  # 保存到csv的目录
    if count <= len(cvs_list_test):
        df = pd.read_csv(file)
        w = df.iloc[0]['width']
        h = df.iloc[0]['height']
        the_cls = None
        for i in range(0, len(zln_class_tongji)):
            if df.iloc[0]['class'] == zln_class_tongji[i]:
                the_cls = i

        x_min = df.iloc[0]['xmin']
        y_min = df.iloc[0]['ymin']
        x_max = df.iloc[0]['xmax']
        y_max = df.iloc[0]['ymax']

        out_file = open(out_txt_path, 'w', encoding='UTF-8')  # 以写入的方式打开TXT
        box = convert((int(w), int(h)), (int(float(x_min)), int(float(x_max)), int(float(y_min)), int(float(y_max))))
        out_file.write(str(the_cls) + ' ' + ' '.join([str(round(a, 6)) for a in box]) + '\n')  # 把内容写入TXT中




def makeSureTxt():
    zlnpath = '/home/data/'
    num = 0
    for root, dirs, files in os.walk(zlnpath):
        for name in files:
            if name.endswith(".txt"):
                num = num + 1
                if num < 10:
                    with open(str(root) + '/' + str(name), encoding='utf-8') as file:
                        content = file.read()
                        print(content.rstrip())  ##rstrip()删除字符串末尾的空行
    print('save txt file :', num)















