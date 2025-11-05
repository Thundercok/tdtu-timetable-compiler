import pytesseract
import cv2
from PIL import Image

#%%
def check_tesseract():
    try:
        version = pytesseract.get_tesseract_version()
        print(f"Tesseract version: {version}")
    except pytesseract.TesseractNotFoundError:
        print("Lỗi: Tesseract Engine chưa được cài đặt!")
#%%
def prepare_image(image_path):
    # 1. Đọc ảnh - OpenCV trả về numpy array mặc định
    img = cv2.imread(image_path) 
    
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    # 2. Chuyển sang ảnh xám (Lúc này img đang là numpy array)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 3. Tăng độ tương phản & khử nhiễu
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)
    return thresh

def extract_text_from_cell(cell_img):
  
    # Cấu hình psm 6: Coi block ảnh là một đoạn văn bản thô
    # 'vie' cho tiếng Việt, 'eng' cho các con số và mã môn
    text = pytesseract.image_to_string(cell_img, lang='vie+eng', config='--psm 6')
    return text.strip()
