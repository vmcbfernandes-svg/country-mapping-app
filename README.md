# Country Mapping Application

A Streamlit-based web application for viewing country mapping data from Excel files.

## Features

- **Dynamic Filtering**: Filter countries by Geo and Market
- **Interactive Dropdowns**: Cascading dropdowns that update based on selections
- **System Display**: View enabled systems and offerings for each country
- **Clean UI**: Modern, responsive interface built with Streamlit

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Navigate to the project directory**:
   ```bash
   cd country-mapping-app
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Place the Excel file** in the project directory:
   - File name: `Country Mapping File 28April2026 vs1.xlsx`
   - Location: Same directory as `app.py`

2. **Verify the file structure**:
   ```
   country-mapping-app/
   ├── app.py
   ├── data_processor.py
   ├── requirements.txt
   ├── README.md
   └── Country Mapping File 28April2026 vs1.xlsx
   ```

## Running the Application

1. **Start the Streamlit server**:
   ```bash
   streamlit run app.py
   ```

2. **Access the application**:
   - The app will automatically open in your default browser
   - Default URL: `http://localhost:8501`

3. **Stop the application**:
   - Press `Ctrl+C` in the terminal

## Usage

1. **Select Geo**: Choose a geographic region or "All"
2. **Select Market**: Choose a market (filtered by Geo selection)
3. **Select Country**: Choose a country (filtered by Geo and Market)
4. **View Details**: See enabled systems and offerings for the selected country

## Excel File Format

The application expects an Excel file with the following structure:

- **Column 1**: `Geo` - Geographic region
- **Column 2**: `Market` - Market name
- **Column 3**: `Country` - Country name
- **Remaining Columns**: System/Offering names with Y/Yes values indicating enabled status

## Troubleshooting

### File Not Found Error
- Ensure the Excel file is in the same directory as `app.py`
- Check the file name matches exactly: `Country Mapping File 28April2026 vs1.xlsx`

### Import Errors
- Run `pip install -r requirements.txt` again
- Ensure you're using Python 3.8 or higher

### Port Already in Use
- If port 8501 is busy, Streamlit will automatically try the next available port
- Or specify a different port: `streamlit run app.py --server.port 8502`

## Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **openpyxl**: Excel file reading

## Project Structure

```
country-mapping-app/
├── app.py                 # Main Streamlit application
├── data_processor.py      # Data processing logic
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Development

To modify the application:

1. Edit `app.py` for UI changes
2. Edit `data_processor.py` for data processing logic
3. Restart the Streamlit server to see changes

Streamlit supports hot-reloading, so most changes will be reflected automatically.

## License

This project is provided as-is for internal use.