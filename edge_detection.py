import numpy as np
import cv2
import matplotlib.pyplot as plt

def canny_edge_detection( image ,lower=-1, upper=-1):
    # img_path = r"D:/oneDrive/Desktop/Canny-Edge-Detector/static/images/Pyramids2.jpg"  # Using raw string or forward slashes
    # img = cv2.imread(img_path)  
    nparr = np.fromstring(image, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = preprocess_image(img)
    magnitude, angle = gradient_magnitude_angle(img)
    edges = non_maxima_suppression(magnitude, angle)
    if lower==-1 and upper==-1:
        edges = double_thresholding(edges, low=0.2*np.max(edges), high= 0.7*np.max(edges))
    else:
        edges = double_thresholding(edges, low=lower, high= upper)
    edges = check_neighbors(edges)
    plt.imshow(edges, cmap='gray')
    plt.axis('off')
    plt.show()
    return edges

def gaussian_kernel(size, sigma=1):
    kernel = np.fromfunction(lambda x, y: (1 / (2 * np.pi * sigma ** 2)) * np.exp(-((x - (size - 1) ** 2 + (y - (size - 1) ** 2)) / (2 * sigma ** 2))), (size, size))
    return kernel / np.sum(kernel)

def preprocess_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    rows = img.shape[0]
    cols = img.shape[1]
    size = 5
    sigma = 1
    gaussian_filter = gaussian_kernel(size, sigma)
    img = np.pad(img, (size-1, size-1), mode='constant')
    gaussian_img = np.zeros((rows, cols))
    for i in range(rows-size):
        for j in range(cols-size):
            gaussian_img[i, j] = np.sum(img[i:i+size, j:j+size] * gaussian_filter) 
    return gaussian_img

def gradient_magnitude_angle(img):
    sobel_kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    rows = img.shape[0]
    cols = img.shape[1]
    size = 3
    img = np.pad(img, (size-1, size-1), mode='constant')
    gx = np.zeros((rows, cols))
    gy = np.zeros((rows, cols))
    for i in range(rows-size):
        for j in range(cols-size):
            gx[i, j] = np.sum(img[i:i+size, j:j+size] * sobel_kernel_x)
            gy[i, j] = np.sum(img[i:i+size, j:j+size] * sobel_kernel_y)
    magnitude = np.sqrt(gx**2 + gy**2)
    angle = np.arctan2(gy, gx) * 180 / np.pi 
    angle = np.round((angle%360) / 45) * 45 
    return magnitude, angle

def non_maxima_suppression(magnitude, angle):
    suppressed = np.zeros(magnitude.shape)
    for i in range(1, magnitude.shape[0] - 1):
        for j in range(1, magnitude.shape[1] - 1):
            if angle[i, j] == 0 or angle[i, j] == 180 :
                if magnitude[i, j] == max(magnitude[i, j], magnitude[i, j+1], magnitude[i, j-1]):
                    suppressed[i, j] = magnitude[i, j]
            elif angle[i, j] == 45 or angle[i, j] == 225:
                if magnitude[i, j] == max(magnitude[i, j], magnitude[i+1, j-1], magnitude[i-1, j+1]):
                    suppressed[i, j] = magnitude[i, j]
            elif angle[i, j] == 90 or angle[i, j] == 270:
                if magnitude[i, j] == max(magnitude[i, j], magnitude[i+1, j], magnitude[i-1, j]):
                    suppressed[i, j] = magnitude[i, j]
            elif angle[i, j] == 135 or angle[i, j] == 315:
                if magnitude[i, j] == max(magnitude[i, j], magnitude[i+1, j+1], magnitude[i-1, j-1]):
                    suppressed[i, j] = magnitude[i, j]
    return suppressed

def double_thresholding(img:np.ndarray, lower_threshold:float, upper_threshold:float):
    [n,m] = img.shape
    marking = np.zeros(img.shape)
    for x in range(n):
        for y in range(m):
            if img[x,y] > upper_threshold:
                marking[x,y] = 255
            elif img[x,y] < lower_threshold:
                marking[x,y] = 0
            else:
                marking[x,y] = 25
    return marking

def check_neighbors(edges):
    [rows, cols] = edges.shape
    for x in range(rows-1):
        for y in range(cols-1):
            if edges[x,y] == 25:
                if ((edges[x+1,y] == 255) or (edges[x-1,y] == 255) or (edges[x+1,y+1] == 255) or (edges[x+1,y-1] == 255) or
                (edges[x-1,y+1] == 255) or (edges[x-1,y-1] == 255) or (edges[x,y+1] == 255) or (edges[x,y-1] == 255)):
                    edges[x,y] = 255
                else:
                    edges[x,y] = 0
    return edges


