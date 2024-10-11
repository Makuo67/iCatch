import os
import tensorflow as tf
# We need to track this


def load_densenet_model():
    # Load the pre-trained DenseNet201 model (h5 file)
    model = tf.keras.models.load_model(
        "models/densenet_model.h5")
    return model


def predict_disease(model, image):
    # Make predictions
    preds = model.predict(image)
    predicted_class = tf.argmax(preds, axis=1).numpy()[0]
    return predicted_class
