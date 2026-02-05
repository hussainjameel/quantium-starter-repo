import pandas as pd
import os

def process_sales_data():
    """
    Process all sales CSV files in the data folder.
    Filters for pink morsels, calculates sales, and combines into one output file.
    """
    
    print("Starting sales data processing...")
    print("=" * 50)
    
    # Define the data directory
    data_dir = 'data'
    
    # List to hold all processed DataFrames
    all_data = []
    
    # Process each CSV file
    for filename in sorted(os.listdir(data_dir)):
        if filename.endswith('.csv'):
            filepath = os.path.join(data_dir, filename)
            print(f"\nProcessing {filename}...")
            
            # Read the CSV file
            df = pd.read_csv(filepath)
            print(f"  Total records: {len(df)}")
            
            # Filter for pink morsels only (case-insensitive)
            df_filtered = df[df['product'].str.lower() == 'pink morsel']
            print(f"  Pink morsel records: {len(df_filtered)}")
            
            if df_filtered.empty:
                print(f"  ⚠️ No pink morsels found in {filename}")
                continue
            
            # Clean price column - remove $ and convert to float
            df_filtered = df_filtered.copy()  # Avoid SettingWithCopyWarning
            df_filtered['price'] = df_filtered['price'].str.replace('$', '', regex=False).astype(float)
            
            # Calculate sales (price × quantity)
            df_filtered['sales'] = df_filtered['price'] * df_filtered['quantity']
            
            # Round sales to 2 decimal places
            df_filtered['sales'] = df_filtered['sales'].round(2)
            
            # Keep only required columns: sales, date, region
            df_final = df_filtered[['sales', 'date', 'region']].copy()
            
            all_data.append(df_final)
    
    if not all_data:
        print("\n❌ No data was processed!")
        return
    
    # Combine all DataFrames
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Sort by date
    combined_df['date'] = pd.to_datetime(combined_df['date'])
    combined_df = combined_df.sort_values('date')
    
    # Format date back to string (YYYY-MM-DD)
    combined_df['date'] = combined_df['date'].dt.strftime('%Y-%m-%d')
    
    # Save to output file
    output_file = 'formatted_sales_data.csv'
    combined_df.to_csv(output_file, index=False)
    
    # Print summary
    print("\n" + "=" * 50)
    print("✅ PROCESSING COMPLETE!")
    print("=" * 50)
    print(f"Total pink morsel records processed: {len(combined_df)}")
    print(f"Date range: {combined_df['date'].min()} to {combined_df['date'].max()}")
    print(f"Regions found: {', '.join(sorted(combined_df['region'].unique()))}")
    print(f"Output file: {output_file}")
    
    # Show first few rows
    print("\nFirst 10 rows of output:")
    print(combined_df.head(10).to_string(index=False))
    
    return combined_df

if __name__ == "__main__":
    process_sales_data()