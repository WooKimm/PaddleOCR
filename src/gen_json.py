import pandas as pd
import json

#生成训练数据的标准json文件
def gen_det_label(input_csv, out_json):
    with open(out_json, 'w',encoding='utf-8') as out_file:
        df = pd.read_csv(input_csv)
        print(len(df))
        for i, tup in enumerate(df.itertuples()):
            # print(tup[3])
            label=[]
            img_path="http://"+tup[2].split("//")[-1].split("jpg")[0]+'jpg'#图片名称
            # img_path=img_path.replace("http://hongsheng-sma2.oss-cn-zhangjiakou.aliyuncs.com/DataSets/general/data/images/book", "C:/Users/Administrator/Desktop/tianchi/round1_train1")
            img_path=img_path.replace("http://hongsheng-sma2.oss-cn-zhangjiakou.aliyuncs.com/DataSets/general/data/images/invoice", "D:/Woo/study/TianChi/OCR/round1_train")
            # img_path = img_path.replace("http://hongsheng-sma2.oss-cn-zhangjiakou.aliyuncs.com/DataSets/general/data/images/npx","C:/Users/Administrator/Desktop/tianchi/round1_train2")
            img_path=img_path.replace("%21","!")
            img_path = img_path.replace("%25", "%")
            img_path = img_path.replace("%28", "(")
            img_path = img_path.replace("%29", ")")

            img_path1 = str(i+1) + '.jpg'

            jsLoads = json.loads(tup[3])#转换成json格式解析
            for i in range(len(jsLoads[0])):
                allcontent=jsLoads[0][i]
                text_content=allcontent["text"]
                text_content=text_content.strip("/{")
                text_content=text_content.strip("}")
                text = text_content.split(":")[1]
                # print(text)
                text = text.strip(" ")
                text = text.strip("\\\"")

                # text=text_content.replace("text", "transcription")#"transcription": "xxx"
                coord_content=allcontent["coord"]
                points=[[float(coord_content[0]),float(coord_content[1])],[float(coord_content[2]),float(coord_content[3])],
                        [float(coord_content[4]),float(coord_content[5])],[float(coord_content[6]),float(coord_content[7])]]
                result = {"transcription": text, "points": points}
                label.append(result)
            out_file.write(img_path1 + '\t' + json.dumps(label, ensure_ascii=False) + '\n')

gen_det_label(r'../Xeon1OCR_round1_test1_20210528.csv', r'../test1_json')