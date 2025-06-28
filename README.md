# 🛡️ Havenly — Your Personalized AI Insurance Advisor

> _“Not just policies — a plan that fits right. For every walk of life.”_

Havenly is a GenAI-powered insurance guidance platform built to simplify the complex world of insurance for everyone — whether you're newly married, self-employed, a parent, a senior, or just starting out.

## ✨ What You Can Do with Havenly

- 🔍 **Find plans tailored to your life stage** — from age, family size, budget, to wellness and maternity needs.
- 🧠 **Get human-like plan explanations** — thanks to Gemini AI’s intelligent reasoning.
- 📑 **Understand your options clearly** — compare plans side-by-side without jargon.
- 💬 **Ask follow-ups or “what-if” questions** — just like you'd ask a real advisor.
- 💾 **Bookmark and revisit plans you like** — save your shortlist easily.

## 🧭 How It Works

1. **Plan Finder** — A friendly form collects basic info: age group, type of coverage, location, preferences.
2. **Plan Matching** — Plans are scored and filtered from real insurance datasets.
3. **Chat Advisor** — Gemini-powered AI gives human-style recommendations and explains them clearly.
4. **Plan Details & Comparison** — You can dive deeper into each plan or compare multiple plans.
5. **Modular Pages** — All accessible from a clean, navigable sidebar.

---

## 🗂️ Project Structure

```

📁 havenly/                        ← your main project folder (root of Git repo)
├── Home.py                       ← Main landing page
├── About Us.py                   ← About the platform
├── Find a Plan.py                ← Questionnaire-based plan finder
├── You and your Plan.py          ← Chatbot interface
├── Details.py                    ← Plan detail viewer
├── utils.py                      ← Gemini + data logic
├── requirements.txt              ← Dependencies
├── README.md                     ← Project overview
├── img.jfif                      ← Hero/landing image
├── imgg.jfif                     ← About page image

# Cleaned datasets (used across app)
├── filtered_plan2.csv            ← Main plan dataset
├── filtered_rate_clean.csv       ← Cleaned rate info (costs by age, tobacco)
├── filtered_service_area_clean.csv  ← State & service area details

# Optional extras (if needed later)
├── .streamlit/
│   └── config.toml   

````

---

## 🧠 Tech Stack

- **Python + Streamlit** for app UI
- **Google Gemini API (1.5 Flash)** for conversational reasoning
- **Pandas** for data filtering and scoring
- **CSV datasets** [from Healthcare Marketplace](https://www.kaggle.com/datasets/hhs/health-insurance-marketplace)
                    / Kaggle (13GB+ raw data trimmed to a few MBs)
- **Virtual Environment** for clean package management

---

## 🚀 Running Locally

```bash
# Clone the repo
git clone https://github.com/thehaniyaakhtar/Havenly.git
cd havenly

# Set up virtual env
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key to utils.py (line 5)
genai.configure(api_key="YOUR_API_KEY")

# Run the app
streamlit run Home.py
````

---

## 🔒 API Key Note

This project requires a **Google Gemini API key**. For now, it's directly added in `utils.py` for simplicity. 

---

## 💬 Why Havenly?

Insurance is overwhelming. Havenly makes it personal, conversational, and empowering — not just about policies, but **your life, your risks, your goals**.

---

## Screenshots

![Screenshot (376)](https://github.com/user-attachments/assets/e5387ee8-6b1b-46c1-b1a9-c5177ad594d2)
Home.py

![Screenshot (377)](https://github.com/user-attachments/assets/2ba09bf8-ea22-40be-8ccf-ee52ff97a54b)
About Us.py

![Screenshot (378)](https://github.com/user-attachments/assets/32d45bd5-be58-4186-b1f5-2fcb0dee1f4e)
Details.py

![Screenshot (379)](https://github.com/user-attachments/assets/908fb28a-0e1f-4a0d-9870-3f4ddc3b0380)
Find a Plan.py

![Screenshot (380)](https://github.com/user-attachments/assets/44e6d7d9-e730-4a5c-b30e-06fcd1619255)
You and your Plan.py

![Screenshot (381)](https://github.com/user-attachments/assets/72ce36f0-74d7-4db8-aaa8-d94d65bf162e)
You and your Plan.py

---

## 🤝 Credits

Built with care, submitted for the **DSW GenAI Agent Hackathon 2024**.

---

## 📌 Disclaimer

This project is for demonstration and educational purposes. The insurance recommendations and datasets are **simulated** and not intended for real-world decision-making.

```

