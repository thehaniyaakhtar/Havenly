# 📁 Havenly Project Structure

```
poly/
├── 🏠 Core Application Files
│   ├── Home.py                    # Main Streamlit application entry point
│   ├── start_app.py              # Application startup script
│   ├── utils.py                  # Utility functions and AI integration
│   └── setup_env.py              # Environment setup script
│
├── 📄 Data Files (Optimized for Deployment)
│   ├── filtered_plan2.csv        # Insurance plan data (1,000+ plans)
│   ├── filtered_rate2.csv        # Premium rates and pricing data
│   ├── filtered_benefits2.csv    # Coverage benefits information
│   ├── filtered_service_area.csv # Geographic service areas
│   └── filtered_plans.csv        # Original comprehensive plan data (31MB)
│
├── 📊 Data Processing Scripts
│   ├── load_plans.py             # Plan data loading and filtering
│   ├── filtered_rate2.py         # Rate data processing
│   ├── filtered_services.py      # Service area data processing
│   ├── trim_benefits.py          # Benefits data optimization
│   ├── trim_rate.py              # Rate data optimization
│   ├── trim_service.py           # Service area optimization
│   ├── trim_business_rules.py    # Business rules processing
│   └── update_plan_names.py      # Plan name generation script
│
├── 🎯 Streamlit Pages
│   ├── pages/
│   │   ├── Dashboard.py          # Analytics and market insights
│   │   ├── Find_a_Plan.py        # Plan search and comparison
│   │   ├── Details.py            # Detailed plan information
│   │   ├── You_and_your_Plan.py  # AI chatbot assistant
│   │   └── About_Us.py           # About page and information
│
├── ⚛️ React Frontend (Optional)
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
├── 🔧 Configuration Files
│   ├── requirements.txt          # Python dependencies
│   ├── .gitignore               # Git ignore patterns
│   ├── .streamlit/              # Streamlit configuration
│   └── venv/                    # Python virtual environment
│
├── 📚 Documentation
│   ├── README.md                # Main project documentation
│   ├── DEPLOYMENT.md            # Deployment instructions
│   ├── GIT_FILES_SUMMARY.md     # Git repository summary
│   └── PROJECT_STRUCTURE.md     # This file structure guide
│
├── 🧪 Testing & Development
│   ├── test_chat.py             # Chatbot testing script
│   └── __pycache__/             # Python cache files
│
└── 🖼️ Assets
    ├── img.jfif                 # Application images
    └── imgg.jfif                # Additional images
```

## 🔍 Key File Descriptions

### **Core Application**
- **`Home.py`**: Main application with landing page, metrics, and navigation
- **`utils.py`**: AI integration, data loading, and utility functions
- **`start_app.py`**: Application startup and configuration

### **Data Files**
- **`filtered_plan2.csv`**: Optimized plan data with realistic plan names
- **`filtered_rate2.csv`**: Premium rates and pricing information
- **`filtered_benefits2.csv`**: Coverage benefits and features
- **`filtered_service_area.csv`**: Geographic coverage areas

### **Streamlit Pages**
- **`Dashboard.py`**: Interactive analytics and market insights
- **`Find_a_Plan.py`**: Plan search with filtering and comparison
- **`Details.py`**: Detailed plan information explorer
- **`You_and_your_Plan.py`**: AI chatbot with plan recommendations
- **`About_Us.py`**: About page and company information

### **Data Processing**
- **`update_plan_names.py`**: Generates realistic insurance plan names
- **`load_plans.py`**: Loads and processes plan data
- **`trim_*.py`**: Optimizes large datasets for deployment

### **Frontend (Optional)**
- **`src/components/`**: React components for enhanced UI
- **`package.json`**: Node.js dependencies and scripts
- **`tailwind.config.js`**: Tailwind CSS styling configuration

## 🚀 Quick Start Files

1. **`requirements.txt`** - Install Python dependencies
2. **`Home.py`** - Run the main application
3. **`utils.py`** - Core functionality and AI integration
4. **`filtered_plan2.csv`** - Main plan data source

## 📊 Data Flow

```
Original Data → Processing Scripts → Optimized CSV → Application
     ↓              ↓                    ↓              ↓
filtered_plans.csv → trim_*.py → filtered_plan2.csv → Home.py
```

## 🔧 Configuration

- **Environment**: Python 3.8+ with Streamlit
- **AI Integration**: Google Gemini API
- **Styling**: Tailwind CSS + Custom CSS
- **Deployment**: Streamlit Cloud
- **Data**: Optimized CSV files for performance 