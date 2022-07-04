def from_imgdir_to_json(old_csv,imgdir,outimgdir,out_json):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", gpu_mem=1000, use_gpu=True, det_db_box_thresh=0.2)
    # ocr = PaddleOCR(use_angle_cls=True, lang="ch", gpu_mem=500,use_gpu=True,det_model_dir=r'E:\PaddleOCR\inference\det_east')

    with open(out_json, 'w', encoding='utf-8') as json_file:
        out_file={}#存放所有图像的json
        csv_data = pd.read_csv(old_csv)
        print(csv_data["原始数据"])
        for item in csv_data["原始数据"]:
            image_name = item.split("//")[-1].split("/")[-1].split("jpg")[0] + "jpg"
            print(image_name)
            image_name1=image_name.replace("%21","!")
            image_name1 = image_name1.replace("%25", "%")
            image_name1 = image_name1.replace("%28", "(")
            image_name1 = image_name1.replace("%29", ")")
            img_path=imgdir+image_name1

            all_transcriptionsList=[]#文本所有框中的内容
            all_pointsList=[]#文本所有框的坐标
            all_ignoreList=[]
            all_classesList=[]
            for line in result:
                print(line)
                line_text=line[1][0]#当前行文字内容
                line_coord=[line[0][0][0],line[0][0][1],line[0][1][0],line[0][1][1],line[0][2][0],line[0][2][1],line[0][3][0],line[0][3][1]]
                line_confidence=line[1][1]#当前行文字内容准确率，基于此可过滤一些错误内容
                if line_confidence>0.4:
                    print(line_text)
                    print(line_coord)
                    all_transcriptionsList.append(line_text)
                    all_pointsList.append(line_coord)
                    all_ignoreList.append(False)
                    all_classesList.append(1)
            out_file[image_name[:-4]]={"pointsList":all_pointsList,"transcriptionsList":all_transcriptionsList,"ignoreList":all_ignoreList,"classesList":all_classesList}
        json_file.write(json.dumps(out_file, ensure_ascii=False))

for i in range(0,3):
    old_csv = r'C:/Users/Administrator/Desktop/tianchi/Xeon1OCR_round1_test'+str(i)+'_20210528.csv'
    imgdir=r'C:/Users/Administrator/Desktop/tianchi/Xeon1OCR_round1_test'+str(i)+'_20210528/'
    outimgdir=r'C:/Users/Administrator/Desktop/tianchi/test'+str(i)+'_result/'
    out_json=r'C:/Users/Administrator/Desktop/tianchi/Xeon1OCR_round1_test'+str(i)+'_20210528.json'
    from_imgdir_to_json(old_csv,imgdir,outimgdir,out_json)
