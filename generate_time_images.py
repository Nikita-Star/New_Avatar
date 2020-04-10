import utils
import cv2
import numpy as np
from datetime import datetime, timedelta
def get_black_background():
    return np.zeros((500, 500))
start_time = datetime.strptime("2019-01-01", "%Y-%m-%d")  # Можете выбрать любую дату
end_time = start_time + timedelta(days=1)

def generate_image_with_text(text):
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (int(image.shape[0]*0.35), int(image.shape[1]*0.5)), font, 1.5, (255, 255, 0), 2, cv2.LINE_AA)
    return image

while start_time < end_time:
    text = utils.convert_time_to_string(start_time)
    image = generate_image_with_text(text)
    cv2.imwrite(f"time_images/{text}.jpg", image)
    start_time += timedelta(minutes=1)