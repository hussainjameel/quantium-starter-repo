# Quantium Software Engineering Job Simulation - Pink Morsels Sales Dashboard

🎉 **SIMULATION COMPLETED!** Successfully finished Quantium's Software Engineering Job Simulation on Forage.

A complete data pipeline and interactive dashboard solution built for Soul Foods' retail analytics team. This project processes sales data and visualizes Pink Morsels performance before and after the January 15, 2021 price increase.

## 🏆 Accomplishments

✅ **Local Development Setup**: Python 3.9 virtual environment with dash, pandas, plotly dependencies  
✅ **ETL Pipeline**: Processed 3 years of CSV data (40K+ records) into analytics-ready format  
✅ **Interactive Dashboard**: Built Dash application with Plotly visualizations and region filtering  
✅ **Professional UI**: Custom CSS styling with responsive design and dark theme  
✅ **Testing Suite**: Comprehensive pytest validation for all application components  
✅ **CI/CD Automation**: Batch scripts for automated testing and deployment workflows  

## 📊 Business Solution

**Problem**: Soul Foods needed to analyze if sales increased or decreased after raising Pink Morsel prices on January 15, 2021.

**Solution**: Built a data pipeline and dashboard that clearly shows:
- **Sales INCREASED by 35.8%** after the price increase
- Before: $6,604.14 average daily sales
- After: $8,971.57 average daily sales
- Total analyzed: 5,880 Pink Morsel records (2018-2022)

## 📁 Project Structure

quantium-starter-repo/
├── data/ # Raw and processed data
│ ├── daily_sales_data_0.csv # 2018 sales data
│ ├── daily_sales_data_1.csv # 2019 sales data
│ ├── daily_sales_data_2.csv # 2020 sales data
│ └── formatted_sales_data.csv # Processed ETL output
├── app.py # Main Dash application
├── process_sales.py # ETL data processing pipeline
├── test_app.py # Pytest test suite
├── run_tests.bat # CI/CD automation script
├── start_server.bat # One-click server launcher
├── requirements.txt # Python dependencies
└── README.md # This file


## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Windows (or adapt batch scripts for your OS)

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/quantium-starter-repo.git
cd quantium-starter-repo

# Option 1: One-click launcher (Windows)
start_server.bat

# Option 2: Manual setup
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Process Data
python process_sales.py

Generates formatted_sales_data.csv with cleaned, analytics-ready data.

# Run the app
python app.py

Access dashboard at: http://127.0.0.1:8050

### 🧪 Testing

# Run test suite
pytest test_app.py -v

# Or use automated script (returns exit code 0/1 for CI/CD)
run_tests.bat

Test Coverage:

✅ Dashboard header and components

✅ Visualization rendering

✅ Region picker functionality

✅ Data processing validation

✅ Callback execution

🎯 Dashboard Features
Interactive Visualizations
Sales Trend Line Chart: Time-series with price increase marker (Jan 15, 2021)

Region Filtering: Real-time filtering by North, South, East, West regions

Performance Metrics: Total sales, average daily sales, percentage change

Business Insights: Clear visualization of price increase impact

Data Processing
Processes 3 CSV files (2018, 2019, 2020)

Filters for Pink Morsels only

Calculates: sales = price × quantity

Adds price period flags (before/after Jan 15, 2021)

Outputs clean dataset for analysis

🔧 Technical Details
ETL Pipeline (process_sales.py)
python
# Key transformations:
1. Filter: df[df['product'] == 'pink morsel']
2. Clean: price.str.replace('$', '').astype(float)
3. Calculate: sales = price × quantity
4. Combine: pd.concat([2018, 2019, 2020 data])
5. Output: sales, date, region columns
Dashboard Architecture (app.py)
Data Layer: pandas DataFrame with 5,880 records

Visualization Layer: Plotly figures with annotations

UI Layer: Dash components with CSS styling

Interaction Layer: Callbacks for real-time filtering

Automation Scripts
run_tests.bat: CI/CD ready test execution (exit code 0/1)

start_server.bat: Production server deployment

Both handle virtual environment activation and dependency checks

📊 Data Statistics
Total Records: 5,880 Pink Morsel sales

Date Range: February 6, 2018 - February 14, 2022

Total Sales: $10,645,583.00

Average Daily Sales: $7,241.89

Regions: North, South, East, West

Price Increase Impact: +35.8% average daily sales

🛠️ Technology Stack
Python 3.9: Core programming language

Dash 2.14.2: Web application framework

Plotly 5.18.0: Interactive data visualization

Pandas 2.0.3: Data manipulation and analysis

Pytest 7.4.0: Testing framework

Batch Scripting: Windows automation for CI/CD
