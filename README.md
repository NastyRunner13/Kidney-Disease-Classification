# Kidney Disease Classification Using Deep Learning

## Overview
This project implements an end-to-end deep learning solution for classifying kidney conditions (normal vs. tumor) using medical imaging data. Built with TensorFlow and VGG16, the model achieves 86% accuracy in distinguishing between healthy kidneys and those with tumors. The project incorporates MLOps best practices, including experiment tracking, version control, and automated deployment pipelines. A Flask web application provides an intuitive interface for model interaction and predictions.

## Tech Stack
- **Python**: Core programming language
- **Flask**: Web application framework
- **TensorFlow**: Deep learning framework
- **VGG16**: Pre-trained CNN architecture
- **MLflow**: Experiment tracking and model registry
- **DVC**: Data and model version control
- **GitHub Actions**: CI/CD pipeline
- **Docker**: Containerization
- **AWS**: Cloud deployment (optional)

## Key Features
1. **Deep Learning Model**
   - Custom-modified VGG16 architecture
   - Transfer learning with fine-tuning
   - 86% classification accuracy
   - Robust to various image qualities and conditions

2. **Web Application**
   - User-friendly interface for image upload
   - Real-time predictions
   - Visualization of model confidence scores
   - Prediction history tracking

3. **MLOps Implementation**
   - Automated data versioning with DVC
   - Experiment tracking using MLflow
   - Reproducible training pipeline
   - Model versioning and registry
   - Automated testing and deployment

4. **Data Pipeline**
   - Automated data ingestion
   - Preprocessing and augmentation
   - Train-validation split management
   - Data version control

5. **Monitoring & Logging**
   - Model performance metrics tracking
   - Training process monitoring
   - Prediction logging
   - System health monitoring

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Kidney-Disease-Classification.git
cd Kidney-Disease-Classification
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure DVC:
```bash
dvc init
dvc remote add -d storage s3://your-bucket/path  # Optional: for S3 storage
```

5. Set up MLflow:
```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 --port 5000
```

## Usage

### Running the Web Application
```bash
cd src/webapp
python app.py
```
Access the application at `http://localhost:5000`

### Training the Model
```bash
dvc repro               # Run the entire pipeline
```

Via Web Interface:
1. Navigate to `http://localhost:5000`
2. Upload an image through the web interface
3. View prediction results and confidence scores

### Monitoring Experiments
1. Start MLflow UI:
```bash
mlflow ui
```
2. Access the dashboard at `http://localhost:5000`

## Model Performance
- **Accuracy**: 86%

## CI/CD Pipeline
The project includes automated CI/CD using GitHub Actions:
- Automated testing on pull requests
- Model training validation
- Performance regression checks
- Automated deployment to production

## API Documentation
The model is served via a Flask REST API:

### Endpoint: `/predict`
- Method: POST
- Input: Image file (jpg/png)
- Output: JSON with prediction and confidence score

## Web Interface Routes
- `/`: Home page with image upload form
- `/predict`: Displays prediction results

## Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a Pull Request
