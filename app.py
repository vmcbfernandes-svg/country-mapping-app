import streamlit as st
import os
import pandas as pd

import data_processor
from data_processor import CountryMappingProcessor

print("USING FILE:", data_processor.__file__)


# Page configuration
st.set_page_config(
    page_title="Country Mapping App",
    page_icon="🌍",
    layout="wide"
)

# IBM-style light theme CSS
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #f4f4f4;
    }
    
    /* Force light background for all dataframes - more aggressive selectors */
    div[data-testid="stDataFrame"],
    div[data-testid="stDataFrame"] > div,
    div[data-testid="stDataFrame"] iframe,
    .stDataFrame,
    .stDataFrame > div,
    .stDataFrame iframe,
    .dataframe {
        background-color: #ffffff !important;
    }
    
    /* Target the actual table elements */
    div[data-testid="stDataFrame"] table,
    .stDataFrame table,
    .dataframe table {
        background-color: #ffffff !important;
        color: #161616 !important;
    }
    
    div[data-testid="stDataFrame"] th,
    .stDataFrame th,
    .dataframe th,
    .dataframe thead th {
        background-color: #e8f5e9 !important;
        color: #161616 !important;
        font-weight: 600 !important;
        border-bottom: 2px solid #24a148 !important;
    }
    
    div[data-testid="stDataFrame"] td,
    .stDataFrame td,
    .dataframe td,
    .dataframe tbody td {
        background-color: #ffffff !important;
        color: #161616 !important;
        border-bottom: 1px solid #e0e0e0 !important;
    }
    
    div[data-testid="stDataFrame"] tbody tr:hover,
    .stDataFrame tbody tr:hover,
    .dataframe tbody tr:hover {
        background-color: #f8f9fa !important;
    }
    
    /* Custom table styling for HTML tables */
    .comparison-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #ffffff;
        margin: 20px 0;
    }
    
    .comparison-table th {
        background-color: #e8f5e9;
        color: #161616;
        font-weight: 600;
        padding: 12px;
        text-align: left;
        border-bottom: 2px solid #24a148;
    }
    
    .comparison-table td {
        background-color: #ffffff;
        color: #161616;
        padding: 10px 12px;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .comparison-table tbody tr:hover {
        background-color: #f8f9fa;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #161616 !important;
        font-weight: 600 !important;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #0f62fe !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #525252 !important;
    }
    
    /* Metric delta (the small text below metrics) */
    [data-testid="stMetricDelta"] {
        background-color: transparent !important;
        color: #161616 !important;
    }
    
    [data-testid="stMetricDelta"] svg {
        fill: #24a148 !important;
    }
    
    [data-testid="stMetricDelta"] > div {
        background-color: transparent !important;
        color: #161616 !important;
    }
    
    /* Selectbox */
    .stSelectbox label {
        color: #393939 !important;
        font-weight: 500 !important;
    }
    
    /* Multiselect - add label styling */
    .stMultiSelect label {
        color: #393939 !important;
        font-weight: 500 !important;
    }
    
    /* Cards and containers */
    .stMarkdown {
        color: #161616;
    }
    
    /* Success/Info boxes */
    .stSuccess {
        background-color: #e8f5e9 !important;
        color: #161616 !important;
        border-left: 4px solid #24a148 !important;
        font-weight: 600 !important;
    }
    
    .stSuccess p {
        color: #161616 !important;
    }
    
    .stSuccess div {
        color: #161616 !important;
    }
    
    .stSuccess strong {
        color: #161616 !important;
    }
    
    /* Target the success alert content specifically */
    [data-testid="stAlert"] {
        background-color: #e8f5e9 !important;
    }
    
    [data-testid="stAlert"] p,
    [data-testid="stAlert"] div,
    [data-testid="stAlert"] strong {
        color: #161616 !important;
    }
    
    .stInfo {
        background-color: #d0e2ff !important;
        border-left: 4px solid #0f62fe !important;
    }
    
    .stWarning {
        background-color: #fcf4d6 !important;
        border-left: 4px solid #f1c21b !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 4px !important;
        color: #161616 !important;
        font-weight: 500 !important;
    }
    
    .streamlit-expanderContent {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        border-top: none !important;
    }
    
    /* Custom card styling */
    .custom-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 4px;
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
    }
    
    .system-item-yes {
        color: #24a148;
        font-weight: 500;
        padding: 8px 0;
    }
    
    .system-item-no {
        color: #8d8d8d;
        padding: 8px 0;
    }
    
    .info-item {
        padding: 6px 0;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .info-item:last-child {
        border-bottom: none;
    }
    
    /* Horizontal rule */
    hr {
        border-color: #e0e0e0 !important;
        margin: 30px 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🌍 Country Mapping Application")
st.markdown("---")

# File path to the Excel file
EXCEL_FILE = "Country Mapping File 28April2026 vs1.xlsx"

# Check if file exists
if not os.path.exists(EXCEL_FILE):
    st.error(f"❌ Excel file not found: {EXCEL_FILE}")
    st.info("Please place the 'Country Mapping File 28April2026 vs1.xlsx' file in the same directory as app.py")
    st.stop()

# Initialize the data processor
# Initialize the data processor
def load_data():
    """Load and cache the data processor"""
    try:
        processor = CountryMappingProcessor(EXCEL_FILE)
        return processor
    except Exception as e:
        import traceback
        st.error("Error loading data:")
        st.text(traceback.format_exc())
        return None




processor = load_data()

if processor is None:
    st.stop()

# Create four columns for the dropdowns (Geo, Sub-Region, Market, Country)
col1, col2, col3, col4 = st.columns(4)

# Geo dropdown
with col1:
    geos = processor.get_unique_geos()
    selected_geo = st.selectbox(
        "Select Geo",
        options=["All"] + geos,
        index=0
    )

# Sub-Region dropdown (filtered by Geo)
with col2:
    geo_filter = None if selected_geo == "All" else selected_geo
    subregions = processor.get_unique_subregions(geo_filter)
    
    if subregions:
        selected_subregion = st.selectbox(
            "Select Sub-Region",
            options=["All"] + subregions,
            index=0
        )
    else:
        selected_subregion = "All"
        st.selectbox(
            "Select Sub-Region",
            options=["All"],
            index=0,
            disabled=True
        )

# Market dropdown (filtered by Geo and Sub-Region)
with col3:
    geo_filter = None if selected_geo == "All" else selected_geo
    subregion_filter = None if selected_subregion == "All" else selected_subregion
    markets = processor.get_unique_markets(geo_filter, subregion_filter)
    selected_market = st.selectbox(
        "Select Market",
        options=["All"] + markets,
        index=0
    )

# Country multiselect (filtered by Geo, Sub-Region, and Market)
with col4:
    geo_filter = None if selected_geo == "All" else selected_geo
    subregion_filter = None if selected_subregion == "All" else selected_subregion
    market_filter = None if selected_market == "All" else selected_market
    countries = processor.get_countries(geo_filter, subregion_filter, market_filter)
    
    if not countries:
        st.warning("No countries available for the selected filters")
        selected_countries = []
    else:
        selected_countries = st.multiselect(
            "Select Country",
            options=countries,
            help="Select one or more countries to view details or compare"
        )

st.markdown("---")

# Handle single vs multiple country selection
if len(selected_countries) == 1:
    # Single country mode - show original detailed view
    selected_country = selected_countries[0]
    details = processor.get_country_details(selected_country)
    
    # Display basic information
    st.subheader(f"📍 {selected_country}")
    
    info_col1, info_col2 = st.columns(2)
    with info_col1:
        st.metric("Geo", details['geo'])
    with info_col2:
        st.metric("Market", details['market'])
    
    st.markdown("---")
    
    # Display ALL systems/offerings with Yes/No values
    # Get systems data and ensure it's a dictionary
    systems_data = details.get('all_systems', {})
    
    # Safety: convert list → dict if needed
    if isinstance(systems_data, list):
        systems_data = {str(i): v for i, v in enumerate(systems_data)}
    
    if systems_data:
        st.subheader("✅ Systems & Offerings")
        
        # Count enabled systems
        enabled_count = sum(1 for v in systems_data.values() if str(v).lower() == "yes")
        
        # Use custom styled div instead of st.success for better color control
        st.markdown(
            f"""
            <div style="background-color: #e8f5e9; padding: 16px; border-radius: 4px; border-left: 4px solid #24a148; margin-bottom: 16px;">
                <p style="color: #161616; font-weight: 600; margin: 0;">
                    <strong>{enabled_count}</strong> of <strong>{len(systems_data)}</strong> systems/offerings are enabled for this country
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Display in 3 columns with color indicators
        num_cols = 3
        cols = st.columns(num_cols)
        
        for idx, (system, value) in enumerate(systems_data.items()):
            col_idx = idx % num_cols
            with cols[col_idx]:
                if value == "Yes":
                    st.markdown(f'<div class="system-item-yes">✅ <strong>{system}</strong> — {value}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="system-item-no">⬜ <strong>{system}</strong> — {value}</div>', unsafe_allow_html=True)
    else:
        st.warning("No systems or offerings data available for this country")
    
    st.markdown("---")
    
   # Display Additional Information section
    info_fields = details.get("info_fields", {})

    st.markdown("---")
    st.subheader("📋 Additional Information")

    if info_fields:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)

        for field_name, field_value in info_fields.items():
            st.markdown(
                f'<div class="info-item"><strong>{field_name}</strong> — {field_value}</div>',
                unsafe_allow_html=True
            )

        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.info("No additional information available for this country")

elif len(selected_countries) > 1:
    # Multiple countries mode - show comparison tables
    st.subheader(f"🔍 Comparing {len(selected_countries)} Countries")
    
    # Build systems comparison table
    comparison_data = {}
    
    for country in selected_countries:
        details = processor.get_country_details(country)
        
        for system, value in details['all_systems'].items():
            if system not in comparison_data:
                comparison_data[system] = {}
            # Use Yes/No text instead of icons
            comparison_data[system][country] = value
    
    # Create DataFrame and sort by system name
    df_systems = pd.DataFrame(comparison_data).T
    df_systems = df_systems.sort_index()
    
    # Display systems comparison
    st.markdown("---")
    st.subheader("✅ Systems & Offerings Comparison")
    
    # Count enabled systems per country
    enabled_counts = {}
    for country in selected_countries:
        details = processor.get_country_details(country)
        enabled_counts[country] = sum(1 for v in details['all_systems'].values() if v == "Yes")
    
    # Display summary with custom styling
    st.markdown(
        f"""
        <div style="background-color: #e8f5e9; padding: 16px; border-radius: 4px; border-left: 4px solid #24a148; margin-bottom: 16px;">
            <p style="color: #161616; font-weight: 600; margin: 0;">
                Comparing systems across {len(selected_countries)} countries
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    summary_cols = st.columns(len(selected_countries))
    for idx, country in enumerate(selected_countries):
        with summary_cols[idx]:
            total_systems = len(comparison_data)
            st.metric(country, f"{enabled_counts[country]}/{total_systems}", "systems enabled")
    
    # Convert to HTML table for better styling control and no scrolling
    html_table = df_systems.to_html(classes='comparison-table', escape=False)
    st.markdown(html_table, unsafe_allow_html=True)
    
    # Build additional information comparison table
    info_data = {}
    
    for country in selected_countries:
        details = processor.get_country_details(country)
        
        for field, value in details["info_fields"].items():
            if field not in info_data:
                info_data[field] = {}
            info_data[field][country] = value
    
    # Display additional information comparison
    if info_data:
        st.markdown("---")
        st.subheader("📋 Additional Information Comparison")
        
        # Add custom styling banner
        st.markdown(
            f"""
            <div style="background-color: #d0e2ff; padding: 16px; border-radius: 4px; border-left: 4px solid #0f62fe; margin-bottom: 16px;">
                <p style="color: #161616; font-weight: 600; margin: 0;">
                    Additional information for {len(selected_countries)} countries
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        df_info = pd.DataFrame(info_data).T
        # Convert to HTML table for better styling control and no scrolling
        html_table_info = df_info.to_html(classes='comparison-table', escape=False)
        st.markdown(html_table_info, unsafe_allow_html=True)
    else:
        st.info("No additional information available for comparison")

else:
    # No countries selected
    st.info("👆 Please select one or more countries to view details or compare")


# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 20px;'>
        <small>Country Mapping Application | Built with Streamlit & Python</small>
    </div>
    """,
    unsafe_allow_html=True
)

# Made with Bob
