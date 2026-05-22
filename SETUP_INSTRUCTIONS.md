# Quick Setup Instructions

## Step 1: Install Dependencies

Open a terminal in the `country-mapping-app` directory and run:

```bash
pip install -r requirements.txt
```

This will install:
- streamlit (web framework)
- pandas (data processing)
- openpyxl (Excel file reading)

## Step 2: Add Excel File

Place your Excel file in the project directory:
- **File name**: `Country Mapping File 28April2026 vs1.xlsx`
- **Location**: Same folder as `app.py`

## Step 3: Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`

## Quick Test

After starting the app:
1. Select a **Geo** from the dropdown
2. Select a **Market** (filtered by Geo)
3. Select a **Country** (filtered by Geo and Market)
4. View the enabled systems and offerings

## Troubleshooting

**Problem**: "Excel file not found"
- **Solution**: Ensure the Excel file is in the same directory as `app.py`

**Problem**: "Import errors"
- **Solution**: Run `pip install -r requirements.txt` again

**Problem**: "Port already in use"
- **Solution**: Streamlit will automatically use the next available port

## File Structure

```
country-mapping-app/
├── app.py                                      # Main application
├── data_processor.py                           # Data processing logic
├── requirements.txt                            # Dependencies
├── README.md                                   # Full documentation
├── SETUP_INSTRUCTIONS.md                       # This file
└── Country Mapping File 28April2026 vs1.xlsx  # Your Excel file (add this)
```

## Commands Summary

```bash
# Navigate to project
cd country-mapping-app

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py

# Stop application
# Press Ctrl+C in terminal
```

That's it! Your Country Mapping App should now be running.