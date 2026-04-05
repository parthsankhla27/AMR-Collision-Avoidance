\# Collision Hazard Detection for AMRs Using YOLOv8n

\[cite\_start]\*\*Author:\*\* Parth Sankhla \[cite: 2]  

\[cite\_start]\*\*Course:\*\* MMAE 500 - Data Driven Modelling \[cite: 3]  

\[cite\_start]\*\*Date:\*\* May 2025 \[cite: 4]



\## 🎯 Project Overview

\[cite\_start]Autonomous Mobile Robots (AMRs) are increasingly deployed in dynamic industrial environments, necessitating robust collision avoidance systems for safe operation alongside human workers and equipment\[cite: 6]. \[cite\_start]This project addresses the challenge of visual hazard detection by employing a data-driven approach utilizing the YOLOv8n deep learning model\[cite: 8]. \[cite\_start]By training on a custom-curated dataset of common shopfloor obstacles, the system provides real-time visual hazard awareness\[cite: 11].



\## 🛠️ Technical Stack

\* \[cite\_start]\*\*Model:\*\* YOLOv8n (Nano version) was selected to balance detection accuracy and inference speed on resource-constrained platforms\[cite: 45, 46].

\* \[cite\_start]\*\*Framework:\*\* Ultralytics YOLOv8 framework\[cite: 49].

\* \[cite\_start]\*\*Language:\*\* Python 3.12.5\[cite: 63].

\* \[cite\_start]\*\*Hardware:\*\* NVIDIA RTX 3050 Laptop GPU with 4GB VRAM\[cite: 60, 65].

\* \[cite\_start]\*\*Environment:\*\* Developed within a Python environment using VS Code\[cite: 49].



\## 📊 Dataset \& Preprocessing

\[cite\_start]The dataset was curated from publicly available sources on Roboflow Universe\[cite: 28]. \[cite\_start]It consists of approximately 12,000 images organized into training, validation, and test subsets\[cite: 41].



\### \[cite\_start]Detected Hazard Classes\[cite: 9, 23]:

\* 📦 \*\*Cardboard Boxes\*\*

\* 🪵 \*\*Pallets\*\*

\* 🏗️ \*\*Shelves\*\*

\* 🚧 \*\*Safety Cones\*\*

\* 🚜 \*\*Forklifts\*\*



\### Development Workflow:

\* \[cite\_start]\*\*Custom Relabeling:\*\* A Python script was developed to systematically relabel bounding box annotations according to a unified class schema\[cite: 39].

\* \[cite\_start]\*\*Format Conversion:\*\* Annotation formats were standardized to the YOLO format\[cite: 40].

\* \[cite\_start]\*\*Integrity Checks:\*\* Basic checks ensured label files corresponded to image files and coordinates remained within boundaries\[cite: 42].



\## 🚀 Training \& Results

\[cite\_start]The training involved an initial 50-epoch phase followed by 30 epochs of fine-tuning using the Adam optimizer\[cite: 52, 53, 59].



\### \[cite\_start]Performance Metrics on Unseen Test Set\[cite: 81]:

| Metric | Result |

| :--- | :--- |

| \*\*mAP50-95\*\* | 38.9% |

| \*\*mAP50\*\* | 67.4% |

| \*\*Precision\*\* | 74.7% |

| \*\*Recall\*\* | 60.8% |



\### Key Observations:

\* \[cite\_start]\*\*Best Performance:\*\* The model performed best on Cardboard Boxes (52.8% mAP50-95) and Shelves (50.1% mAP50-95)\[cite: 83, 100].

\* \[cite\_start]\*\*Challenges:\*\* Forklift detection was notably lower (26.3% mAP50-95), likely due to lower sample diversity and larger variations in vehicle models\[cite: 83, 101, 102].



\## 🔍 Discussion \& Future Work

\[cite\_start]This project demonstrates the feasibility of deep learning for AMR hazard detection\[cite: 96]. Future improvements could include:

\* \[cite\_start]\*\*Improved Data:\*\* Increasing image variety and using augmentation to improve model learning\[cite: 112].

\* \[cite\_start]\*\*Model Scaling:\*\* Testing larger YOLO variants (e.g., YOLOv8m or YOLOv8l) for higher accuracy\[cite: 113].

\* \[cite\_start]\*\*Depth Information:\*\* Integrating depth data to better understand the 3D geometry and distance of hazards\[cite: 116].



\---

\[cite\_start]\*This work serves as a practical demonstration of applying machine learning and deep learning methodologies to perception and safety challenges in robotic systems\[cite: 24].\*

