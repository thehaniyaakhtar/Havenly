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

**Built with ❤️ to make insurance less painful — one plan at a time.**

```

