print("LOADED CORRECT data_processor.py")
import pandas as pd

class CountryMappingProcessor:

    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)

        # Clean column names
        self.df.columns = [col.strip() for col in self.df.columns]

        # Auto-detect columns
        country_col = next((col for col in self.df.columns if "country" in col.lower()), None)
        geo_col = next((col for col in self.df.columns if "geo" in col.lower()), None)
        subregion_col = next((col for col in self.df.columns if "sub-region" in col.lower() or "subregion" in col.lower()), None)
        market_col = next((col for col in self.df.columns if "market" in col.lower()), None)

        if not country_col or not geo_col or not market_col:
            raise Exception(f"Columns not found. Available columns: {self.df.columns.tolist()}")

        # Rename to standard names
        rename_dict = {
            country_col: "Country",
            geo_col: "Geo",
            market_col: "Market"
        }
        
        if subregion_col:
            rename_dict[subregion_col] = "Sub-Region"
        
        self.df = self.df.rename(columns=rename_dict)

        # Clean values
        self.df["Country"] = self.df["Country"].astype(str).str.strip()
        self.df["Geo"] = self.df["Geo"].astype(str).str.strip()
        self.df["Market"] = self.df["Market"].astype(str).str.strip()
        
        if "Sub-Region" in self.df.columns:
            self.df["Sub-Region"] = self.df["Sub-Region"].astype(str).str.strip()

        # Remove empty rows
        self.df = self.df[self.df["Country"] != ""]

        # Fill missing values
        self.df = self.df.fillna("")

        # Identify system columns (Yes/No values) and info columns (text/metadata)
        self.system_columns = []
        self.info_columns = []
        
        for col in self.df.columns:
            if col not in ["Country", "Geo", "Market", "Sub-Region"]:
                # Check if column contains Yes/No values
                unique_values = self.df[col].astype(str).str.strip().str.lower().unique()
                # Filter out empty strings
                unique_values = [v for v in unique_values if v and v != 'nan']
                
                # If all non-empty values are yes/no/y/n, it's a system column
                if unique_values and all(v in ['yes', 'no', 'y', 'n'] for v in unique_values):
                    self.system_columns.append(col)
                else:
                    self.info_columns.append(col)

    def get_unique_geos(self):
        return sorted(self.df["Geo"].unique())
    
    def get_unique_subregions(self, geo_filter=None):
        """Get unique sub-regions, optionally filtered by geo"""
        df: Any = self.df.copy()

        if geo_filter and geo_filter != "All":
            df = df[df["Geo"] == geo_filter]
        
        if "Sub-Region" in df.columns:
            subregions = df["Sub-Region"].dropna().unique()
            return sorted([sr for sr in subregions if sr and str(sr).strip()])
        return []

    def get_unique_markets(self, geo_filter=None, subregion_filter=None):
        """Get unique markets, optionally filtered by geo and sub-region"""
        df = self.df
        if geo_filter and geo_filter != "All":
            df = df[df["Geo"] == geo_filter]
        if subregion_filter and "Sub-Region" in df.columns:
            df = df[df["Sub-Region"] == subregion_filter]
        return sorted(df["Market"].unique())

    def get_countries(self, geo_filter=None, subregion_filter=None, market_filter=None):
        """Get countries, optionally filtered by geo, sub-region, and market"""
        df = self.df.copy()

        
        if geo_filter and geo_filter != "All":
            df = df[df["Geo"] == geo_filter]

        
        if subregion_filter and subregion_filter != "All" and "Sub-Region" in df.columns:
            df = df[df["Sub-Region"] == subregion_filter]

        if market_filter and market_filter != "All":
            df = df[df["Market"] == market_filter]

        return sorted(df["Country"].unique())

    def get_country_details(self, country):
        """Get all details for a specific country"""
        row = self.df[self.df["Country"] == country].iloc[0]

        # Get all systems with their Yes/No values
        all_systems = {}
        for col in self.system_columns:
            value = str(row[col]).strip().lower()
            if value in ["y", "yes"]:
                all_systems[col] = "Yes"
            elif value in ["n", "no"]:
                all_systems[col] = "No"
            else:
                all_systems[col] = "No"  # Default to No if unclear

        # Get all info fields with their values
        info_fields = {}
        for col in self.info_columns:
            value = str(row[col]).strip()
            if value and value.lower() != 'nan':
                info_fields[col] = value

        return {
            "geo": row["Geo"],
            "market": row["Market"],
            "all_systems": all_systems,
            "info_fields": info_fields
        }

    def get_all_system_columns(self):
        return self.system_columns
    
    def get_system_columns(self):
        """Return list of system columns (Yes/No values)"""
        return self.system_columns
    
    def get_info_columns(self):
        """Return list of info columns (text/metadata)"""
        return self.info_columns
