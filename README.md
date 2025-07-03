# Kombucha Growth Analysis Repository

This repository contains scripts, and results for analyzing SCOBY (kombucha culture) growth via image-based methods. Below is an overview of each folder and notebook, along with instructions for getting started.


---

## Setup and Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/kombucha-growth-analysis.git
   cd kombucha-growth-analysis


2. **Create and activate a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # on Windows: venv\Scripts\activate

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

---
## Folder Descriptions
1. Cropping_images:
Contains Python scripts and utilities to crop raw images and extract Regions of Interest (ROI). These scripts standardize the field of view for downstream analysis.

2. Data:
Images captured during experiments.

3. Data_acquisition:
Scripts responsible for image capture and real-time data logging, pH sensor connection.

4. Df_created_from_images:
Dataframes created from the color analysis.

5. data_experiments:
Digital Twin data and the collected measurments during the experiments. 

6. masks:
Binary mask images corresponding to segmented regions of the SCOBY film. 

7. Scipts in the main folder:
Color and growth analysis of SCOBY culture in separate scipts.
