from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models.densenet_model import load_densenet_model, predict_disease
from models.groq_model import get_text_explanation
from gradcam.gradcam_pp import generate_gradcam
from utils.image_utils import save_image, load_image
import os

app = FastAPI()

# Setup CORS
origins = [
    "http://localhost:5500",
    # other allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (images) from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="../templates")

# Load the DenseNet201 model
densenet_model = load_densenet_model()
# Define the class names for disease classification
class_names = ['Age-related Macular Degeneration', 'Cataract',
               'Diabetic retinopathy', 'Glaucoma', 'Normal Fundus']


@app.get("/", response_class=HTMLResponse)
async def render_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Rendering other html file


@app.get("/dashboard", response_class=HTMLResponse)
async def render_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/consultdoctor", response_class=HTMLResponse)
async def render_consultdoctor(request: Request):
    return templates.TemplateResponse("consultdoctor.html", {"request": request})


@app.get("/appointment", response_class=HTMLResponse)
async def render_appointment(request: Request):
    return templates.TemplateResponse("appointment.html", {"request": request})


@app.get("/bookappointment", response_class=HTMLResponse)
async def render_bookappointment(request: Request):
    return templates.TemplateResponse("bookappointment.html", {"request": request})


@app.get("/doctorprofile(appointment)", response_class=HTMLResponse)
async def render_doctorprofileappointment(request: Request):
    return templates.TemplateResponse("doctorprofile(appointment).html", {"request": request})


@app.get("/doctorprofile(consultation)", response_class=HTMLResponse)
async def render_doctorprofileconsultation(request: Request):
    return templates.TemplateResponse("doctorprofile(consultation).html", {"request": request})


@app.get("/index", response_class=HTMLResponse)
async def render_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/myhospitals", response_class=HTMLResponse)
async def render_myhospitals(request: Request):
    return templates.TemplateResponse("myhospitals.html", {"request": request})


@app.get("/newappointment", response_class=HTMLResponse)
async def render_newappointment(request: Request):
    return templates.TemplateResponse("newappointment.html", {"request": request})


@app.get("/newconsultation", response_class=HTMLResponse)
async def render_newconsultation(request: Request):
    return templates.TemplateResponse("newconsultation.html", {"request": request})


@app.get("/requestconsultation", response_class=HTMLResponse)
async def render_requestconsultation(request: Request):
    return templates.TemplateResponse("requestconsultation.html", {"request": request})


@app.get("/upload_form", response_class=HTMLResponse)
async def render_upload_form(request: Request):
    return templates.TemplateResponse("upload_form.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict_image(request: Request, file: UploadFile = File(...)):
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
        densenet_model, image, class_index)

    # Generate AI text explanation
    explanation = get_text_explanation(disease_prediction)

    # Remove temp file if needed
    # os.remove(image_path)

    # Serve the results page
    return templates.TemplateResponse(
        "results.html",
        {
            "request": request,
            "prediction": disease_prediction,
            "original_image": f"/{image_path}",
            "gradcam_image": f"/{gradcam_image_path}",
            "explanation": explanation
        }
    )
