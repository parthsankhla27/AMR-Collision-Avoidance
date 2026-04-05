\# Collision Hazard Detection for AMRs Using YOLOv8n

\*\*Author:\*\* Parth Sankhla  

\*\*Course:\*\* MMAE 500 - Data Driven Modelling  

\*\*Date:\*\* May 2025



\## 🎯 Project Overview

Autonomous Mobile Robots (AMRs) are increasingly deployed in dynamic industrial environments, necessitating robust collision avoidance systems for safe operation alongside human workers and equipment. This project addresses the challenge of visual hazard detection by employing a data-driven approach utilizing the YOLOv8n deep learning model. By training on a custom-curated dataset of common shopfloor obstacles, the system provides real-time visual hazard awareness.



\## 🛠️ Technical Stack

\* \*\*Model:\*\* YOLOv8n (Nano version) was selected to balance detection accuracy and inference speed on resource-constrained platforms.

\* \*\*Framework:\*\* Ultralytics YOLOv8 framework.

\* \*\*Language:\*\* Python 3.12.5.

\* \*\*Hardware:\*\* NVIDIA RTX 3050 Laptop GPU with 4GB VRAM.

\* \*\*Environment:\*\* Developed within a Python environment using VS Code.



\## 📊 Dataset \& Preprocessing

The dataset was curated from publicly available sources on Roboflow Universe. It consists of approximately 12,000 images organized into training, validation, and test subsets.



\### Detected Hazard Classes:

\* 📦 \*\*Cardboard Boxes\*\*

\* 🪵 \*\*Pallets\*\*

\* 🏗️ \*\*Shelves\*\*

\* 🚧 \*\*Safety Cones\*\*

\* 🚜 \*\*Forklifts\*\*



\### Development Workflow:

\* \*\*Custom Relabeling:\*\* A Python script was developed to systematically relabel bounding box annotations according to a unified class schema.

\* \*\*Format Conversion:\*\* Annotation formats were standardized to the YOLO format.

\* \*\*Integrity Checks:\*\* Basic checks ensured label files corresponded to image files and coordinates remained within boundaries.



\## 🚀 Training \& Results

The training involved an initial 50-epoch phase followed by 30 epochs of fine-tuning using the Adam optimizer.



\### Performance Metrics on Unseen Test Set:

| Metric | Result |

| :--- | :--- |

| \*\*mAP50-95\*\* | 38.9% |

| \*\*mAP50\*\* | 67.4% |

| \*\*Precision\*\* | 74.7% |

| \*\*Recall\*\* | 60.8% |



\### Key Observations:

\* \*\*Best Performance:\*\* The model performed best on Cardboard Boxes (52.8% mAP50-95) and Shelves (50.1% mAP50-95).

\* \*\*Challenges:\*\* Forklift detection was notably lower (26.3% mAP50-95), likely due to lower sample diversity and larger variations in vehicle models.



\## 🔍 Discussion \& Future Work

This project demonstrates the feasibility of deep learning for AMR hazard detection. Future improvements could include:

\* \*\*Improved Data:\*\* Increasing image variety and using augmentation to improve model learning.

\* \*\*Model Scaling:\*\* Testing larger YOLO variants (e.g., YOLOv8m or YOLOv8l) for higher accuracy.

\* \*\*Depth Information:\*\* Integrating depth data to better understand the 3D geometry and distance of hazards.



\---

\*This work serves as a practical demonstration of applying machine learning and deep learning methodologies to perception and safety challenges in robotic systems.\*

