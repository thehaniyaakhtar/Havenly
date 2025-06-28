# Havenly Insurance Advisor - Deployment Guide

## Overview
This guide explains how to deploy the Havenly Insurance Advisor application to Streamlit Cloud using the trimmed datasets for optimal performance.

## Prerequisites
- GitHub account
- Streamlit Cloud account (free tier available)
- Google AI API key (for AI chatbot functionality)

## File Structure for Deployment

### Core Application Files
- `Home.py` - Main application entry point
- `utils.py` - Utility functions and data loading
- `requirements.txt` - Python dependencies

### Pages
- `pages/Dashboard.py` - Analytics dashboard
- `pages/Find_a_Plan.py` - Plan search and comparison
- `pages/You_and_your_Plan.py` - AI chatbot interface
- `pages/About_Us.py` - Company information
- `pages/Details.py` - Plan details page

### Data Files (Trimmed for Deployment)
- `filtered_plan2.csv` - 1,000 insurance plans (21MB → 1MB)
- `filtered_rate2.csv` - 1,000 rate records (960MB → 1MB)
- `filtered_benefits2.csv` - 2,000 benefit records (690MB → 1MB)
- `filtered_service_area.csv` - 1,000 service areas (992KB → 1MB)

### Configuration Files
- `.gitignore` - Excludes large files and sensitive data
- `DEPLOYMENT.md` - This deployment guide
- `README.md` - Project documentation

## Deployment Steps

### 1. Prepare Your Repository
```bash
# Ensure all trimmed datasets are in the root directory
ls -la *.csv
# Should show: filtered_plan2.csv, filtered_rate2.csv, filtered_benefits2.csv, filtered_service_area.csv
```

### 2. Set Up Environment Variables
In Streamlit Cloud, add these secrets:
- `GOOGLE_API_KEY` - Your Google AI API key for chatbot functionality

### 3. Deploy to Streamlit Cloud
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set the main file path to: `Home.py`
5. Deploy

### 4. Verify Deployment
- Check that all pages load correctly
- Test the AI chatbot functionality
- Verify data loading and visualizations work
- Test plan search and comparison features

## Performance Optimizations

### Data Size Reduction
- **Before**: ~2GB total data files
- **After**: ~4MB total data files
- **Improvement**: 99.8% size reduction

### Memory Usage
- Trimmed datasets load in seconds instead of minutes
- No more MemoryError issues
- Faster page navigation and interactions

### Caching Strategy
- Removed Streamlit caching to prevent memory issues
- Implemented efficient data loading in `utils.py`
- Fallback to sample data if files are missing

## Troubleshooting

### Common Issues
1. **Import Errors**: Ensure all dependencies are in `requirements.txt`
2. **Data Loading Errors**: Check that trimmed CSV files are in the repository
3. **API Key Issues**: Verify Google AI API key is set in Streamlit secrets
4. **Memory Issues**: All large files should be excluded via `.gitignore`

### Debug Commands
```bash
# Check file sizes
ls -lh *.csv

# Verify data loading
python -c "import pandas as pd; print(pd.read_csv('filtered_plan2.csv').shape)"

# Test local deployment
streamlit run Home.py
```

## File Descriptions

### Core Files
- **Home.py** (11KB): Main landing page with metrics and navigation
- **utils.py** (6.2KB): Data loading, AI integration, and utility functions
- **requirements.txt** (152B): Python package dependencies

### Page Files
- **Dashboard.py** (16KB): Analytics dashboard with charts and metrics
- **Find_a_Plan.py** (12KB): Plan search with AI-powered matching
- **You_and_your_Plan.py** (12KB): AI chatbot for insurance guidance
- **About_Us.py** (9.1KB): Company information and mission
- **Details.py** (2.4KB): Detailed plan information display

### Data Files
- **filtered_plan2.csv** (1MB): Insurance plan details and metadata
- **filtered_rate2.csv** (1MB): Premium rates and pricing information
- **filtered_benefits2.csv** (1MB): Coverage benefits and copays
- **filtered_service_area.csv** (1MB): Geographic service areas

### Configuration
- **.gitignore**: Excludes large files, virtual environments, and sensitive data
- **DEPLOYMENT.md**: This deployment guide
- **README.md**: Project overview and setup instructions

## Support
For deployment issues, check:
1. Streamlit Cloud logs for error messages
2. GitHub repository for file structure
3. Environment variables in Streamlit secrets
4. Data file integrity and format

## Performance Metrics
- **Load Time**: <5 seconds (vs 30+ seconds with large files)
- **Memory Usage**: <512MB (vs 2GB+ with large files)
- **Data Records**: 1,000 plans, 1,000 rates, 2,000 benefits
- **File Size**: 4MB total (vs 2GB+ original) 