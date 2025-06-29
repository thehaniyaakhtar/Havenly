## 🏥 Havenly – Your AI-Powered Health Insurance Advisor

**Havenly** is a smart, intuitive platform that helps you **find, compare, and understand** health insurance plans that truly match your needs. Built using **Streamlit**, **React**, and powered by **Google Gemini AI**, Havenly brings a personalized, conversational experience to insurance — an industry known for being complicated and impersonal.

---

## ✨ Why Havenly?

✔️ Personalized plan suggestions based on your age, location, income, and coverage needs  
✔️ Friendly AI chatbot that answers your insurance questions in real-time  
✔️ Side-by-side plan comparisons with visual insights  
✔️ Clean, minimal UI with a warm, trustworthy design  
✔️ Built to run fast — even on large datasets

---

## 🧠 Key Features

### 🎯 Core Functionality
- **Smart Plan Search**: Enter your basic info, get filtered insurance plans
- **AI-Powered Recommendations**: Gemini AI explains *why* a plan is recommended
- **Interactive Dashboard**: Visualize plan coverage, cost trends, and filters
- **Plan Explorer**: Deep dive into each plan’s benefits and features
- **Chatbot Assistant**: Ask about coverage terms, premium impact, eligibility, and more

### 🎨 Beautiful, Minimal Design
- Earthy green & brown palette for a grounded, calming experience
- Responsive across devices — works great on phones, tablets, and desktops
- Card-based layout for easy comparison and readability

### 🚀 Optimized for Performance
- Uses trimmed datasets for faster load time
- Memory-efficient processing with no caching conflicts
- Streamlit Cloud ready with minimal setup

---

## 📊 Data Sources

We use public health insurance data sourced from **Kaggle**:

- [🗂 Health Insurance Marketplace Datasets (Kaggle)](https://www.kaggle.com/datasets/hhs/health-insurance-marketplace)

These include:
- **Plans** – Insurance plans and provider information
- **Rates** – Premium costs for different user demographics
- **Benefits** – Coverage details for wellness, maternity, etc.
- **Service Areas** – Geographical plan availability

All files are optimized as CSVs for efficient performance.

---

## ⚙️ Configuration & Setup

### File Structure
6. **Deployment**: Hosted on Streamlit Cloud with optimized memory and no caching issues.

---

## 📁 Project Structure

```
havenly/
├──  Core Application Files
│   ├── Home.py                    # Main Streamlit application entry point
│   ├── start_app.py              # Application startup script
│   ├── utils.py                  # Utility functions and AI integration
│   └── setup_env.py              # Environment setup script
│
├──  Data Files (Optimized for Deployment)
│   ├── filtered_plan2.csv        # Insurance plan data (1,000+ plans)
│   ├── filtered_rate2.csv        # Premium rates and pricing data
│   ├── filtered_benefits2.csv    # Coverage benefits information
│   ├── filtered_service_area.csv # Geographic service areas
│   └── filtered_plans.csv        # Original comprehensive plan data (31MB)
│
├──  Data Processing Scripts
│   ├── load_plans.py             # Plan data loading and filtering
│   ├── filtered_rate2.py         # Rate data processing
│   ├── filtered_services.py      # Service area data processing
│   ├── trim_benefits.py          # Benefits data optimization
│   ├── trim_rate.py              # Rate data optimization
│   ├── trim_service.py           # Service area optimization
│   └── trim_business_rules.py    # Business rules processing
│
├──  Streamlit Pages
│   ├── pages/
│   │   ├── Dashboard.py          # Analytics and market insights
│   │   ├── Find_a_Plan.py        # Plan search and comparison
│   │   ├── Details.py            # Detailed plan information
│   │   ├── You_and_your_Plan.py  # AI chatbot assistant
│   │   └── About_Us.py           # About page and information
│
├──  React Frontend (Optional)
│   ├── src/
│   │   ├── components/           # React components
│   │   │   ├── HomePage.js       # Home page component
│   │   │   ├── Dashboard.js      # Dashboard component
│   │   │   ├── PlanFinder.js     # Plan finder component
│   │   │   ├── About.js          # About component
│   │   │   └── Navbar.js         # Navigation component
│   │   ├── App.js                # Main React application
│   │   ├── index.js              # React entry point
│   │   └── index.css             # Global styles
│   ├── public/
│   │   └── index.html            # HTML template
│   ├── package.json              # Node.js dependencies
│   ├── tailwind.config.js        # Tailwind CSS configuration
│   └── postcss.config.js         # PostCSS configuration
│
├──  Configuration Files
│   ├── requirements.txt          # Python dependencies
│   ├── .gitignore               # Git ignore patterns
│   ├── .streamlit/              # Streamlit configuration
│   └── venv/                    # Python virtual environment
│
├──  Documentation
│   ├── README.md                # Main project documentation
│   ├── DEPLOYMENT.md            # Deployment instructions
│   ├── GIT_FILES_SUMMARY.md     # Git repository summary
│   └── PROJECT_STRUCTURE.md     # File structure guide
│
├──  Testing & Development
│   ├── test_chat.py             # Chatbot testing script
│   └── __pycache__/             # Python cache files
│
└──  Assets
    ├── img.jfif                 # Application images
    └── imgg.jfif                # Additional images
```

### **Key File Descriptions**

- **`Home.py`**: Main application with landing page, metrics, and navigation
- **`utils.py`**: AI integration, data loading, and utility functions
- **`filtered_plan2.csv`**: Optimized plan data with realistic plan names
- **`Dashboard.py`**: Interactive analytics and market insights
- **`Find_a_Plan.py`**: Plan search with filtering and comparison
- **`You_and_your_Plan.py`**: AI chatbot with plan recommendations

---

## 🛠️ Tech Stack
### 🔧 System Requirements
- Python 3.10+
- Node.js (optional, for frontend React components)
- Git
- Streamlit CLI

---

### 💻 Local Setup

1. **Clone the repository**
   
```bash
   git clone https://github.com/yourusername/Havenly.git
   cd Havenly
````

2. **Set up Python environment**

   ```bash
   python -m venv venv
   source venv/bin/activate       # For Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**

   ```bash
   streamlit run Home.py
   ```

4. *(Optional)* **Set up React Frontend**

   ```bash
   npm install
   npm start
   ```

---

## ☁️ Deploying to Streamlit Cloud

1. Push your code to GitHub:

   ```bash
   git add .
   git commit -m "Deploy Havenly"
   git push origin master
   ```

2. Visit: [https://share.streamlit.io](https://share.streamlit.io)

3. Connect your GitHub repository.

4. Choose `master` as the branch and `Home.py` as the entry file.

5. Click **Deploy** and you're live! 🚀

> ⚠️ Ensure all required CSV files are in the **root directory** for successful deployment.

---

## 📈 How It Works (Under the Hood)

1. **User Input**: You enter age, location, income, and preferences.
2. **Plan Matching**: We filter plans by location and score them by coverage, features, and cost.
3. **AI Interaction**: Gemini AI answers your questions and explains why a plan is a good match.
4. **Dashboard**: Use filters and charts to compare plans visually.
5. **Plan Explorer**: View detailed features and benefits of selected plans.
6. **Deployment**: Hosted on Streamlit Cloud with optimized memory and no caching issues.

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **Streamlit** – App framework
* **Pandas** – Data wrangling
* **Google Gemini API** – Conversational intelligence

### Frontend (Optional)

* **React** – UI components
* **Tailwind CSS** – Clean, responsive styling
* **JavaScript** – Interactivity

### Data

* Optimized CSVs (from Healthcare.gov / Kaggle)
* Real-time filtering and plan scoring

---

## 🐛 Troubleshooting

| Problem                 | Solution                                                                         |
| ----------------------- | -------------------------------------------------------------------------------- |
| **Port already in use** | Run: `streamlit run Home.py --server.port 8502`                                  |
| **File Not Found**      | Ensure all CSVs are in root folder, check `Details.py` uses `filtered_plan2.csv` |
| **Memory Errors**       | Use trimmed CSVs, avoid using large unfiltered datasets                          |
| **HTML Not Rendering**  | Check `About_Us.py`, use basic HTML tags                                         |
| **Duplicate Labels**    | Groupby fix already applied in `Home.py`, `Dashboard.py`                         |

💡 **Clear cache if needed**:

```bash
streamlit cache clear
```

---

## 🆕 Recent Updates

### ✅ v2.1 – Bug Fixes & Stability

* Fixed file path issues in `Details.py`
* Resolved duplicate group labels
* Cleaned up HTML rendering across components
* Improved error handling and stability on Streamlit Cloud

### ✨ v2.0 – Performance + UI Overhaul

* Switched to trimmed, optimized datasets
* Redesigned UI with green-brown color palette
* Improved chatbot experience
* “Why this plan?” explanations added
* Better visual comparisons in dashboard

---

## 🤝 Contributing

We welcome collaboration!

1. Fork the repo
2. Create a new feature branch
3. Make and test your changes
4. Open a pull request with clear description

---

## 💬 Need Help?

If you run into any issues:

* Check the **Troubleshooting** section above
* Open an issue on GitHub
* Or contact the team

---

## 🔗 Useful Links

* 🔴 **Live Demo**: *[(Click Here!)](https://havenly-9jzwuwesaf5w4nca7a4khs.streamlit.app/)*
* 🧠 **GitHub Repository**: *([Click Here!](https://github.com/thehaniyaakhtar/Havenly/tree/master))*

---

# Screenshots (visit page for a more comprehensive look!)
![Screenshot (382)](https://github.com/user-attachments/assets/1de5283d-4f1f-463e-99ea-3dc516412d3f)
Home Page


![Screenshot (383)](https://github.com/user-attachments/assets/22161511-3934-4299-aeb6-278cdb1e3510)
About Us


![Screenshot (384)](https://github.com/user-attachments/assets/e46ab352-135b-4c87-b285-fed5bb43beba)
Dashboard


![Screenshot (385)](https://github.com/user-attachments/assets/ae7444de-072b-438e-9808-940550f27b9c)
Dashboard


![Screenshot (389)](https://github.com/user-attachments/assets/02a2e0e8-66e4-4214-a039-a72337bff13a)
Learn About Plans


![Screenshot (387)](https://github.com/user-attachments/assets/c262d81c-f2ae-4730-b318-2d2cc1acc534)
Find A Plan based on a Criteria


![Screenshot (390)](https://github.com/user-attachments/assets/10ef7f01-b545-4c86-bb62-f2bfc672bb1c)
AI Chatbot

---

**Built with ❤️ to make insurance less painful — one plan at a time.**

```

