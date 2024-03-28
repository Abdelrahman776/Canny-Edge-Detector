import numpy as np
import cv2
import matplotlib.pyplot as plt

def canny_edge_detection():
  img_path = "D:\oneDrive\Desktop\Canny-Edge-Detector\static\images\peppers.png"
  img_rgb = preprocess_image(img_path)
  magnitude, angle = calculate_gradient(img_rgb)
  angle = round_angles(angle)
  edges = non_maxima_suppression(img_rgb)
  edges = double_thresholding(edges)
  edges = check_neighbors(edges)
  processed_image_path = save_image(edges)
  plt.imshow(edges, cmap='gray')
  plt.axis('off')
#   plt.show()
  return processed_image_path

def preprocess_image(img_path):
    img = cv2.imread(img_path)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rgb = cv2.GaussianBlur(img_rgb, (5, 5), 1)
    return img_rgb

def calculate_gradient(img_rgb):
    gx = cv2.Sobel(img_rgb, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(img_rgb, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(gx**2 + gy**2)
    angle = np.arctan2(gy, gx) * 180 / np.pi
    return magnitude, angle

def round_angles(angle):
    angle = np.round(angle / 45) * 45
    return angle

def non_maxima_suppression(img_rgb):
    suppressed = cv2.Canny(img_rgb, 100, 200)
    return suppressed

def double_thresholding(edges):
    edges[edges >= 100] = 255
    return edges

def check_neighbors(edges):
    for i in range(1, edges.shape[0] - 1):
        for j in range(1, edges.shape[1] - 1):
            if edges[i, j] == 255:
                if (edges[i-1:i+2, j-1:j+2] == 255).sum() < 2:
                    edges[i, j] = 0
    return edges

def save_image(edges):
    return cv2.imwrite("D:\oneDrive\Desktop\Canny-Edge-Detector\static\images\processed_image.png", edges)

canny_edge_detection()    