from fastapi import FastAPI, UploadFile, File
from models.densenet_model import load_densenet_model, predict_disease
from models.groq_model import get_text_explanation
from gradcam.gradcam_pp import generate_gradcam
from utils.image_utils import save_image, load_image
from utils.response_utils import real_time_text_generator

app = FastAPI()

# Load the DenseNet201 model
densenet_model = load_densenet_model()
# Define the class names for disease classification
class_names = ['Normal Fundus', 'Diabetic Retinopathy',
               'Cataract', 'Glaucoma', 'Age-related Macular Degeneration']


@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    # Save uploaded image
    image_path = save_image(file)

    # Load image for prediction and GradCAM++
    image = load_image(image_path)

    # Predict the disease (assumes predict_disease returns the class index)
    class_index = predict_disease(densenet_model, image)

    # Get the disease name from the class index
    disease_prediction = class_names[class_index]

    # Generate GradCAM++ heatmap
    gradcam_image_path = generate_gradcam(
        densenet_model, image, disease_prediction)

    # Generate AI text explanation
    explanation = get_text_explanation(disease_prediction)

    # Stream text like ChatGPT
    text_stream = real_time_text_generator(explanation)

    return {"prediction": disease_prediction, "gradcam_image": gradcam_image_path, "explanation": text_stream}
