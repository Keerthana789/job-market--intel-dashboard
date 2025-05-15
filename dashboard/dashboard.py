import streamlit as st
import pandas as pd
import plotly.express as px

# Load cleaned data
df = pd.read_csv("data/clean_jobs.csv")

st.title("💼 Job Market Intelligence Dashboard")
st.markdown("### 📍 Real-time job analytics from RemoteOK and LinkedIn")
st.markdown("---")

# Sidebar filters
locations = df["location"].dropna().unique().tolist()
tags = sorted(set(tag.strip() for sublist in df["tags"].dropna().apply(eval) for tag in sublist))

st.sidebar.header("Filter Jobs")
selected_locations = st.sidebar.multiselect("Locations", locations)
selected_tags = st.sidebar.multiselect("Tags", tags)
search_query = st.sidebar.text_input("Search Job Title")
max_days = st.sidebar.slider("Posted in last N days", 1, 30, 7)

# Apply filters
filtered_df = df.copy()

if selected_locations:
    filtered_df = filtered_df[filtered_df["location"].isin(selected_locations)]

if selected_tags:
    filtered_df = filtered_df[filtered_df["tags"].apply(lambda tag_list: any(t in tag_list for t in eval(tag_list)))]

if search_query:
    filtered_df = filtered_df[filtered_df["title"].str.contains(search_query, case=False)]

filtered_df = filtered_df[filtered_df["days_since_posted"] <= max_days]

# KPIs
col1, col2 = st.columns(2)
col1.metric("Total Jobs", len(filtered_df))
col2.metric("Unique Companies", filtered_df["company"].nunique())

# Top companies
st.markdown("### 🏢 Top Hiring Companies")
top_companies = filtered_df["company"].value_counts().head(10).reset_index()
top_companies.columns = ["company", "count"]  # rename columns

fig = px.bar(top_companies, x="company", y="count",
             labels={"company": "Company", "count": "Job Count"},
             title="Top Hiring Companies")

fig.update_layout(dragmode=False)
st.plotly_chart(fig, use_container_width=True)

# Job postings over time
st.markdown("### 📆 Job Posts by Date (Grouped by Source)")
filtered_df["date_only"] = pd.to_datetime(filtered_df["date_posted"]).dt.date
date_counts = filtered_df.groupby("date_only").size().reset_index(name="count")
filtered_df["date_only"] = pd.to_datetime(filtered_df["date_posted"]).dt.date
date_counts = (
    filtered_df.groupby(["date_only", "source"])
    .size()
    .reset_index(name="count")
)

# Line chart by date and source
fig2 = px.line(
    date_counts,
    x="date_only",
    y="count",
    color="source",
    markers=True,
    labels={"date_only": "Date", "count": "Job Count", "source": "Source"}
)

fig2.update_layout(dragmode=False)
st.plotly_chart(fig2, use_container_width=True)
st.markdown("🔍 Note: LinkedIn shows a spike because it returns the latest 75 jobs at scrape time, while RemoteOK reflects historical postings.")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)
