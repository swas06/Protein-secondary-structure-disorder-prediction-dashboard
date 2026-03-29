# 🧬 Protein Structure Visualization Dashboard

A **bioinformatics web application** built using **Streamlit** that allows users to analyze protein sequences, predict structural properties, and visualize 3D protein structures using PDB data.

---

## 🚀 Features

* 🔍 Input protein sequence or UniProt ID
* 🧪 Secondary structure prediction (basic)
* ⚡ Disorder region visualization
* 📊 Interactive data visualization
* 🧱 3D Protein Structure Viewer (PDB integration)
* 📂 Multi-page dashboard interface

---

## 🏗️ Project Structure

```
protein-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── fetch_data.py
│   ├── analysis.py
│   └── visualization/
│       ├── __init__.py
│       └── structure_viewer.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
└── pages/
    ├── 1_Analysis.py
    ├── 2_Visualization.py
    └── 3_3D_Structure.py
```

---

## 🧠 Technologies Used

* Python
* Streamlit
* Biopython
* Pandas & NumPy
* Requests
* py3Dmol

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/protein-dashboard.git
cd protein-dashboard
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

---

### 3️⃣ Activate Environment

#### Windows (CMD)

```
venv\Scripts\activate
```

#### Windows (PowerShell)

```
venv\Scripts\Activate.ps1
```

#### Mac/Linux

```
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 5️⃣ Run the Application

```
streamlit run app.py
```

---

## 🌐 Deployment

This project can be deployed easily using **Streamlit Cloud**:

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Select repository
4. Set main file as `app.py`
5. Deploy

---

## 🧪 How It Works

1. User inputs a protein sequence or UniProt ID
2. Backend fetches related data
3. Analysis is performed (structure/disorder)
4. PDB IDs are retrieved
5. User selects a structure
6. 3D model is rendered using py3Dmol

---

## ⚠️ Common Issues

* ❌ 3D viewer not loading → Check internet / PDB ID
* ❌ Module error → Run `pip install -r requirements.txt`
* ❌ App not running → Ensure virtual environment is active

---

## 🎯 Future Improvements

* Integration with real APIs (UniProt, PDB, IUPred)
* Advanced structure prediction tools
* Downloadable reports
* Improved UI/UX

---

## 👨‍💻 Author

Developed as a bioinformatics project for learning and visualization purposes.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
