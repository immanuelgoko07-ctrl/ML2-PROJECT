

You focus on:

clarity

interactivity

explainable visuals

decision support design

The application must be suitable for policymakers, researchers, and energy planners.

 APPLICATION PURPOSE

Build an interactive Streamlit dashboard that:

explores historical electricity access data

visualizes spatial and temporal patterns

displays AI-based electrification forecasts

explains results in plain language

supports data-driven infrastructure planning decisions

The dashboard is a front end interface for a Kubeflow-powered ML system.

 DATA CONTEXT

The dataset includes:

Country

Year

Electricity access (%)

Rural electricity access (%)

Urban electricity access (%)

Population (optional)

Assume data is loaded from a CSV or model endpoint.

 DASHBOARD STRUCTURE (MANDATORY)
 1. Sidebar Controls

Include:

Country selector (multi-select)

Region selector (optional)

Year range slider

Toggle: Total / Rural / Urban electricity access

Forecast horizon selector (e.g. 5 to 15 years)

Model selector (ARIMA, LSTM, ML)

 2. Project Overview Section

Display:

Project title and brief description

Explanation of the Kubeflow + AI pipeline

Clear statement of the dashboard purpose

Use simple language but professional tone.

 3. Exploratory Data Analysis (EDA) Section
Visuals:

Line charts showing electricity access over time

Rural vs urban comparison plots

Growth rate plots

Explanations:

Automatically generated text explaining trends

Highlight key insights and anomalies

Explain implications for electrification planning

 4. Heat Map and Pattern Analysis Section
Visuals:

Country and Year electricity access heat map

Rural electrification heat map

Electrification gap heat map

Interactivity:

Dynamic filtering by country and year

Hover tooltips with values

Explanations:

What the heat map reveals

Why certain regions lag

How gaps evolve over time

 5. Forecasting and Prediction Section
Visuals:

Historical vs predicted electricity access plots

Confidence interval bands

Multi model comparison graphs

Controls:

Forecast horizon slider

Model selection dropdown

Explanations:

Model assumptions

Forecast uncertainty

Real-world interpretation of predictions

 6. Model Performance and Trust Section

Display:

RMSE, MAE, MAPE

Backtesting results

Visual error diagnostics

Explain:

Why these metrics matter

How reliable the predictions are

Where the model may fail

 7. AI Insights and Recommendations Section

Use GenAI outputs to:

Summarize key findings

Identify high-risk countries

Recommend grid vs off-grid solutions

Highlight urgent investment needs

Present insights as:

Bullet points

Callout boxes

Policy friendly language

 8. Download & Export Section

Allow users to:

Download forecasts as CSV

Export charts as images

Save country level reports

 VISUALIZATION REQUIREMENTS

Use clean, readable charts

Label all axes clearly

Include legends and tooltips

Avoid clutter

Prioritize interpretability over decoration

 TECHNICAL REQUIREMENTS

Use Streamlit

Use Plotly or Matplotlib for visualizations

Modular and clean code structure

Clearly separated data loading, modeling, and visualization logic

Ready to integrate with Kubeflow model endpoints

 ERROR HANDLING & UX

Handle missing data gracefully

Show warnings for low data countries

Provide user guidance when selections are invalid

Ensure fast, responsive UI

 FINAL OUTPUT

The final Streamlit app must:

Be interactive and intuitive

Clearly explain electrification trends and forecasts

Support real planning decisions

Reflect a production-ready Kubeflow AI system

 QUALITY BAR

Do not produce:

toy dashboards

unexplained plots

raw model outputs without interpretation

This is a decision-support system, not a demo.
