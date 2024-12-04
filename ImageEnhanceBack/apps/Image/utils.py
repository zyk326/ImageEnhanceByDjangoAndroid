import os
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont

def image_enhance(path):
    # 这里是图片增强的逻辑
    filename = os.path.split(path)[-1]
    file_path = settings.ENHANCED_ROOT / filename
    out_path = settings.ENHANCED_URL + filename
    # 水印
    watermark_text = "Enhanced watermark"

    try:
        # 确保保存目录存在
        os.makedirs(settings.ENHANCED_ROOT, exist_ok=True)

        # 打开原始图片
        img = Image.open(path)
        img = img.convert("RGBA")  # 转换为 RGBA 模式以支持透明度

        # 创建可以在上面绘制的图层
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()  # 使用默认字体

        # 计算水印位置（右下角），使用 textbbox 方法
        bbox = draw.textbbox((0, 0), watermark_text, font=font)  # 获取文本边界框
        text_width = bbox[2] - bbox[0]  # bbox[2] 是右边界，bbox[0] 是左边界
        text_height = bbox[3] - bbox[1]  # bbox[3] 是下边界，bbox[1] 是上边界
        position = (img.width - text_width - 10, img.height - text_height - 10)  # 边距10像素
        print(position, text_width, text_height)

        # 在图片上添加水印
        draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)  # 白色半透明文字

        # 调试信息：打印文件保存路径
        print(f"Saving file to: {file_path}")

        # 检查图像模式，如果是 RGBA 则转换为 RGB
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # 保存增强后的图片
        img.save(file_path)
        img.close()  # 显式关闭图像对象以释放资源
    except Exception as e:
        return f"写入失败！错误信息: {e}"
    return str(out_path)
