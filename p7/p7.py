
import cv2
import matplotlib.pyplot as plt

# Read the color image
img = cv2.imread("road.png")  # Load image in BGR format (default in OpenCV)

# Check if the image loaded successfully
if img is None:
    print("Error: Image not found or path is incorrect.")
else:
    # Convert the image from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)    
    # Split into H, S, V channels
    h, s, v = cv2.split(hsv)

    # Apply histogram equalization on the V (brightness) channel
    v_eq = cv2.equalizeHist(v)

    # Merge the channels back
    hsv_eq = cv2.merge([h, s, v_eq])

    # Convert back to BGR (for OpenCV display) or RGB (for matplotlib)
    img_eq_bgr = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)
    img_eq_rgb = cv2.cvtColor(img_eq_bgr, cv2.COLOR_BGR2RGB)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert original image to RGB for display

    # Show original and equalized images
    plt.subplot(1, 2, 1)
    plt.title('Original RGB')
    plt.imshow(img_rgb)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Equalized RGB')
    plt.imshow(img_eq_rgb)
    plt.axis('off')

    plt.tight_layout()
    
    # Save the comparison image
    plt.savefig('histogram_equalization_result.png', dpi=300, bbox_inches='tight')
    
    plt.show()