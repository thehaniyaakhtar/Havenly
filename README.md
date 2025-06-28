# 🏥 Havenly - Insurance Plan Finder

A modern, user-friendly insurance plan comparison and recommendation platform built with Streamlit and React. Find the perfect health insurance plan tailored to your needs with our intelligent AI assistant.

## ✨ Features

### 🎯 **Core Functionality**
- **Smart Plan Search**: Find insurance plans based on location, age, income, and preferences
- **AI-Powered Recommendations**: Get personalized plan suggestions with detailed explanations
- **Interactive Dashboard**: Visualize plan statistics, costs, and coverage options
- **Plan Details Explorer**: Deep dive into specific plan features and benefits
- **Intelligent Chatbot**: Ask questions about plans, coverage, and insurance terms

### 🎨 **Modern UI/UX**
- **Earthy Color Scheme**: Beautiful greens and browns for a natural, trustworthy feel
- **Minimal Design**: Clean, consistent interface across all pages
- **Responsive Layout**: Works seamlessly on desktop and mobile devices
- **Card-Based Results**: Easy-to-scan plan comparisons with key information

### 🚀 **Performance Optimized**
- **Trimmed Datasets**: Optimized CSV files for faster loading and deployment
- **Memory Efficient**: No caching issues or memory errors
- **Streamlined Backend**: Efficient data processing and analysis

## 🛠️ Technology Stack

### **Backend**
- **Streamlit**: Main application framework
- **Pandas**: Data manipulation and analysis
- **Python**: Core programming language

### **Frontend**
- **React**: Modern UI components
- **Tailwind CSS**: Utility-first styling
- **JavaScript**: Interactive functionality

### **Data**
- **CSV Files**: Optimized insurance datasets
- **AI Integration**: Intelligent plan recommendations

## 📁 Project Structure

```
poly/
├── Home.py                 # Main Streamlit application
├── pages/                  # Streamlit pages
│   ├── Dashboard.py        # Analytics dashboard
│   ├── Details.py          # Plan details explorer
│   ├── Find_a_Plan.py      # Plan search and comparison
│   ├── You_and_your_Plan.py # AI chatbot assistant
│   └── About_Us.py         # About page
├── src/                    # React frontend
│   ├── components/         # React components
│   ├── App.js             # Main React app
│   └── index.js           # React entry point
├── filtered_plan2.csv     # Optimized plan data
├── filtered_rate2.csv     # Optimized rate data
├── filtered_benefits2.csv # Optimized benefits data
├── filtered_service_area.csv # Service area data
├── requirements.txt       # Python dependencies
├── package.json          # Node.js dependencies
└── README.md            # This file
```

## 🚀 Quick Start

### **Local Development**

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Havenly.git
   cd Havenly
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run Home.py
   ```

4. **Set up React frontend (optional)**
   ```bash
   npm install
   npm start
   ```

### **Deployment on Streamlit Cloud**

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin master
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Set branch to **master** (not main)
   - Deploy!

## 📊 Data Sources

The application uses optimized insurance datasets:
- **Plans**: Health insurance plan information and features
- **Rates**: Premium rates and pricing data
- **Benefits**: Coverage details and benefits information
- **Service Areas**: Geographic coverage information

All datasets have been trimmed for optimal performance and deployment.

## 🎯 Key Features Explained

### **Smart Plan Finder**
- Enter your location, age, and income
- Get personalized plan recommendations
- Compare costs, coverage, and features
- View "Why this plan?" explanations

### **Interactive Dashboard**
- Visualize plan statistics by metal level
- Compare average premiums across categories
- Explore coverage trends and patterns
- Interactive charts and graphs

### **AI Chatbot Assistant**
- Ask questions about insurance terms
- Get plan recommendations
- Understand coverage options
- Receive personalized advice

### **Plan Details Explorer**
- Deep dive into specific plans
- View all plan features and benefits
- Compare plan types and metal levels
- Understand coverage limitations

## 🎨 Design Philosophy

### **Earthy Color Palette**
- **Primary Green**: #228B22 (Forest Green)
- **Secondary Brown**: #8B4513 (Saddle Brown)
- **Accent Colors**: Various shades of green and brown
- **Background**: Clean whites and light grays

### **Minimal UI Principles**
- Clean, uncluttered interfaces
- Consistent spacing and typography
- Card-based information display
- Intuitive navigation

## 🔧 Configuration

### **Streamlit Configuration**
The app uses default Streamlit settings with optimized performance:
- No caching to prevent memory issues
- Efficient data loading
- Responsive design

### **Environment Variables**
No sensitive environment variables required - all data is public insurance information.

## 🐛 Troubleshooting

### **Common Issues**

1. **Port Already in Use**
   ```bash
   streamlit run Home.py --server.port 8502
   ```

2. **Memory Errors**
   - The app now uses optimized datasets
   - No caching to prevent memory issues
   - Efficient data processing

3. **File Not Found Errors**
   - All files use the correct trimmed dataset names
   - Ensure all CSV files are in the root directory
   - Fixed Details.py to use `filtered_plan2.csv`

4. **Duplicate Labels Error**
   - Fixed groupby operations in Home.py and Dashboard.py
   - Proper data merging to avoid duplicate indices

5. **HTML Rendering Issues**
   - Fixed About_Us.py HTML rendering
   - Simplified HTML in Find_a_Plan.py and You_and_your_Plan.py

### **Performance Tips**
- Use the trimmed datasets for faster loading
- Clear browser cache if experiencing issues
- Restart the app if memory issues occur
- Clear Streamlit cache if needed: `streamlit cache clear`

### **Deployment Issues**
- Ensure you're using the **master** branch (not main) for Streamlit Cloud
- All CSV files must be in the root directory
- Check that all file paths are correct

## 📈 Recent Updates

### **v2.1 - Bug Fixes & Stability**
- ✅ Fixed Details.py FileNotFoundError (filtered_plan2.csv)
- ✅ Resolved duplicate labels in groupby operations
- ✅ Fixed HTML rendering issues in About_Us.py
- ✅ Improved error handling across all pages
- ✅ Enhanced deployment stability

### **v2.0 - Performance & UI Overhaul**
- ✅ Switched to trimmed datasets for faster performance
- ✅ Implemented earthy green/brown color scheme
- ✅ Added minimal, consistent UI design
- ✅ Fixed all memory and caching issues
- ✅ Enhanced AI chatbot capabilities
- ✅ Improved plan comparison interface
- ✅ Added "Why this plan?" explanations
- ✅ Optimized for Streamlit Cloud deployment

### **v1.0 - Initial Release**
- Basic plan search functionality
- Simple dashboard
- Plan details viewer

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Review the error logs
3. Create an issue on GitHub
4. Contact the development team

## 🔗 Links

- **Live Demo**: [Streamlit Cloud Deployment](your-streamlit-url)
- **GitHub Repository**: [Havenly](https://github.com/yourusername/Havenly)
- **Documentation**: See DEPLOYMENT.md for detailed setup instructions

---

**Built with ❤️ for better insurance experiences**
