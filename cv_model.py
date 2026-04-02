import cv2
import tensorflow as tf

class CVModel:
    def __init__(self, model_path):
        """Initialize the model."""
        self.model = tf.keras.models.load_model(model_path)

    def preprocess_image(self, image):
        """Preprocess the image for the model."""
        image = cv2.resize(image, (224, 224))  # Resize to model input
        image = image / 255.0  # Normalize the image
        return image

    def predict(self, image):
        """Predict the class of the automotive part in the image."""
        processed_image = self.preprocess_image(image)
        processed_image = processed_image.reshape(1, 224, 224, 3)  # Reshape for the model input
        predictions = self.model.predict(processed_image)
        return predictions

# Example usage:
# model = CVModel('path/to/your/model.h5')
# image = cv2.imread('path/to/image.jpg')
# predictions = model.predict(image)