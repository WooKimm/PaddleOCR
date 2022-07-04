from paddleocr import PaddleOCR, draw_ocr
ocr = PaddleOCR(det_model_dir='/home/wuxin/scratch/OCR/PaddleOCR/inference/det_db/',rec_model_dir='/home/wuxin/scratch/OCR/PaddleOCR/inference/rec_crnn',use_angle_cls=True, lang="ch",gpu_mem=1000,use_gpu=False) 
img_path = "/home/wuxin/scratch/OCR/PaddleOCR/eval_shots/1.jpg"
result = ocr.ocr(img_path, cls=True)