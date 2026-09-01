# Smart Garbage Segregation

**A deep learning-powered image classification project for real-time waste sorting, built with TensorFlow/Keras and deployed using Streamlit.**

---

## Overview

This project is aimed at automating waste segregation using artificial intelligence. By leveraging computer vision and convolutional neural networks (CNNs), it can classify waste images (e.g., cardboard, glass, metal, paper, plastic, trash) to promote accurate recycling and sustainable waste management.

---

## Features

- 💡 **Image Classification:** Recognizes 6 waste categories from photos
- 🟢 **End-to-End Pipeline:** Data preprocessing, model training (Jupyter), live web app deployment (Streamlit)
- 🚀 **User Interface:** Easy-to-use web app for drag-and-drop image prediction
- 📈 **Customizable & Extensible:** Easily retrain with new data or classes

---

## Demo

<img width="1410" height="872" alt="image" src="https://github.com/user-attachments/assets/55facc85-137b-4b92-9906-80d5ade14c3c" />
<img width="526" height="927" alt="image" src="https://github.com/user-attachments/assets/3e9a65db-ee3a-40f4-9226-65c9f8f6bf71" />
<img width="858" height="636" alt="Screenshot 2025-09-07 093711" src="https://github.com/user-attachments/assets/838e9abf-864d-4053-aede-c44febcd5af2" />
<img width="859" height="738" alt="image" src="https://github.com/user-attachments/assets/ae63fdc2-1074-4bb8-a7dc-8baf6f607daf" />
<img width="963" height="936" alt="Screenshot 2025-09-07 092355" src="https://github.com/user-attachments/assets/ab5fc874-3376-4afb-b616-4df39f70b7f3" />




Try it locally:

streamlit run Deployment/app.py

text

---
```
## Project Structure

Smart-Garbage-Segregation/
│
├── Data/
│ ├── Train/
│ └── Test/
│
├── Deployment/
│ ├── app.py
│ ├── utils.py
│ └── requirements.txt
│
├── weights/
│ └── modelnew.h5
├── smart_garbage.ipynb
└── README.md

text

---
```
## How to Use

1. **Clone the repository**
    ```
    git clone https://github.com/<your-username>/Smart-Garbage-Segregation.git
    cd Smart-Garbage-Segregation
    ```

2. **Set up the environment**
    ```
    pip install -r Deployment/requirements.txt
    ```

3. **Run the Web App**
    ```
    cd Deployment
    streamlit run app.py
    ```

---

## Model Training

- Model is built and trained in [`smart_garbage.ipynb`](smart_garbage.ipynb).
- Training uses a Convolutional Neural Network (CNN) with Keras/TensorFlow.
- Training and test datasets should be placed inside `Data/Train` and `Data/Test` folders respectively.
- Trained weights are saved as `weights/modelnew.h5` and loaded by the web app.

---

## Results

- Achieves strong performance on test images.
- Typical accuracy: 70%
- Handles real-world confusion between similar categories (e.g., paper vs cardboard).

---

## Limitations & Future Work

- Some classes (like paper and cardboard) may be visually similar and occasionally confused.
- More training images can improve accuracy.
- Future ideas: integrate with IoT hardware, real-time camera input, or deploy as a public web demo.
  <img width="857" height="475" alt="image" src="https://github.com/user-attachments/assets/64e1a162-1274-4963-8294-8d19401b76f8" />


---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- Based on an open-source project by [raison024](https://github.com/raison024/Smart-Garbage-Segregation)
- Dataset and training approach inspired by public computer vision resources

---

*Built by Team Roboinators, NIT Sikkim, 2025*

