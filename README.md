# 💼 Job Market Intelligence Dashboard

A real-time job analytics dashboard that scrapes, cleans, and visualizes listings from [RemoteOK](https://remoteok.com) and LinkedIn using Python, Pandas, and Streamlit.

🚀 **Live Demo**: [Click here to view the dashboard](https://job-market--intel-dashboard-a8d4czahkjhipf8rirhqys.streamlit.app/)

## 📌 Features

- 🔄 Real-time job scraping from RemoteOK and LinkedIn (via JSearch API)
- ⚙️ ETL pipeline to clean and standardize data
- 📊 Interactive dashboard with filters for:
  - Location
  - Tags
  - Title
  - Posting recency
- 📈 Visualizations of:
  - Top hiring companies
  - Job trends over time by source
- ☁️ Deployed live on Streamlit Cloud

---

## 🗂️ Project Structure
job-market-intel-dashboard/
│
├── data/
│ └── clean_jobs.csv # Final cleaned dataset
│
├── dashboard/
│ └── dashboard.py # Streamlit UI
│
├── etl/
│ └── clean_job_data.py # ETL pipeline
│
└── README.md

## 💡 Future Improvements
- Add database or S3 integration to persist job history
- Integrate more job APIs (e.g., Levels.fyi, Indeed)
- Enable filters by experience level, salary, remote/hybrid

