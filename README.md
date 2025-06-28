# 🛡️ Havenly - AI Insurance Advisor

A modern, AI-powered insurance recommendation platform with a React frontend and Streamlit backend.

## 🚀 Features

### React Frontend
- **Modern UI/UX**: Beautiful, responsive design with Tailwind CSS
- **Interactive Components**: Charts, animations, and real-time updates
- **AI Integration**: Seamless connection to Streamlit backend
- **Mobile Responsive**: Works perfectly on all devices

### Streamlit Backend
- **AI-Powered Matching**: Advanced plan recommendation engine
- **Interactive Dashboards**: Comprehensive analytics and visualizations
- **Real-time Data**: Live updates and insights
- **Multi-page App**: Organized navigation and features

## 📁 Project Structure

```
poly/
├── src/                    # React frontend
│   ├── components/         # React components
│   ├── index.js           # React entry point
│   └── index.css          # Tailwind styles
├── public/                # React public assets
├── pages/                 # Streamlit pages
├── Home.py               # Enhanced Streamlit homepage
├── utils.py              # AI utilities
├── requirements.txt      # Python dependencies
├── package.json          # Node.js dependencies
└── README.md            # This file
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### 1. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd poly

# Create Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Setup React Frontend

```bash
# Install Node.js dependencies
npm install

# Start React development server
npm start
```

The React app will run on `http://localhost:3000`

### 3. Setup Streamlit Backend

```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run Streamlit app
streamlit run Home.py
```

The Streamlit app will run on `http://localhost:8501`

### 4. Integration

The React frontend is configured to proxy requests to the Streamlit backend. The integration allows:

- React handles the UI/UX and user interactions
- Streamlit provides the AI backend and data processing
- Seamless communication between frontend and backend

## 🎯 Key Features

### React Frontend Features
- **Homepage**: Modern landing page with interactive elements
- **Plan Finder**: Advanced search and filtering interface
- **Dashboard**: Comprehensive analytics and insights
- **About Page**: Company information and team details
- **Responsive Design**: Mobile-first approach
- **Animations**: Smooth transitions and micro-interactions

### Streamlit Backend Features
- **AI Plan Matching**: Intelligent recommendation engine
- **Interactive Charts**: Plotly visualizations
- **Real-time Analytics**: Live data updates
- **Multi-page Navigation**: Organized feature structure
- **Data Processing**: Efficient CSV handling
- **User Authentication**: Secure access control

## 📊 Data Sources

The application uses several CSV files for insurance data:
- `filtered_plans.csv`: Plan information and metadata
- `filtered_rate.csv`: Pricing and rate data
- `filtered_benefits.csv`: Benefit details and coverage
- `filtered_business_rules.csv`: Business logic and rules

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key
STREAMLIT_SERVER_PORT=8501
REACT_APP_API_URL=http://localhost:8501
```

### Customization
- **Colors**: Modify `tailwind.config.js` for brand colors
- **Charts**: Update chart configurations in Streamlit components
- **Data**: Replace CSV files with your own insurance data
- **AI**: Configure Google Generative AI settings in `utils.py`

## 🚀 Deployment

### React Frontend Deployment
```bash
# Build for production
npm run build

# Deploy to your preferred platform (Vercel, Netlify, etc.)
```

### Streamlit Backend Deployment
```bash
# Deploy to Streamlit Cloud or your preferred platform
streamlit deploy Home.py
```

## 📈 Performance Optimization

- **React**: Code splitting and lazy loading
- **Streamlit**: Caching with `@st.cache_data`
- **Data**: Efficient CSV processing and filtering
- **Charts**: Optimized Plotly configurations

## 🔒 Security

- **API Keys**: Secure environment variable handling
- **Data Privacy**: Local data processing
- **HTTPS**: Production deployment with SSL
- **Input Validation**: Sanitized user inputs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- 📧 Email: hello@havenly.com
- 📞 Phone: 1-800-HAVENLY
- 🌐 Website: havenly.com

## 🎉 Acknowledgments

- **React Team**: For the amazing frontend framework
- **Streamlit Team**: For the powerful data app framework
- **Tailwind CSS**: For the utility-first CSS framework
- **Plotly**: For the interactive charting library
- **Google AI**: For the generative AI capabilities

---

**Made with ❤️ by the Havenly Team**
