import pandas as pd

class SalesAnalysis:
    def __init__(self, df):
        self.df = df.copy()

    def clean_data(self):

        series_missing_val_sum =  self.df.isnull().sum() 
        missing_values_list = series_missing_val_sum[series_missing_val_sum > 0].index.tolist()

        row_missing_values  = self.df[self.df[missing_values_list].isnull().sum(axis=1) > 0][missing_values_list]

        mean_values = self.df[missing_values_list].mean(numeric_only=True)

        fill_values = {col: mean_values[col] if col in mean_values else "Unknown" for col in missing_values_list}

        filled_row_missing_values = row_missing_values.fillna(fill_values)

        
        return filled_row_missing_values, row_missing_values
    
    def revenue_by_region(self):
        revenue_sales = self.df.groupby("Region")["Sales"].sum().reset_index()
        print(revenue_sales)

        max_revenue_region = revenue_sales.loc[revenue_sales['Sales'].idxmax(), 'Region'] 
        print(max_revenue_region)

        min_revenue_region = revenue_sales.loc[revenue_sales['Sales'].idxmin(), 'Region']
        print(min_revenue_region)

        return revenue_sales, min_revenue_region, max_revenue_region
        
    def revenue_by_category(self):
        category_sales = self.df.groupby("Category")["Sales"].sum().reset_index()
        print(category_sales)
        max_category = category_sales.loc[category_sales['Sales'].idxmax()]
        print(max_category)

        min_category =  category_sales.loc[category_sales['Sales'].idxmin()]
        print(min_category)

        sub_category_sales = self.df.groupby("Sub-Category")["Sales"].sum().reset_index()
        print('sub_category_sales', sub_category_sales)

        max_sub_category = sub_category_sales.loc[sub_category_sales['Sales'].idxmax()]
        print('max_sub_category', max_sub_category)

        min_sub_category = sub_category_sales.loc[sub_category_sales['Sales'].idxmin()]
        print('min_sub_category', min_sub_category)


        return category_sales, min_category, max_category, sub_category_sales, min_sub_category, max_sub_category
    
    def customer_analysis(self):
        customer_sales = self.df.groupby('Customer ID')['Sales'].sum().reset_index()
        customer_orders = self.df['Customer ID'].value_counts().reset_index()
        customer_orders.columns = ['Customer ID', 'Order Count']
        
        # Customer has the highest total sales
        top_customer = customer_sales.loc[customer_sales['Sales'].idxmax()]
        
        # Group with the highest revenue
        segment_sales = self.df.groupby('Segment')['Sales'].sum().reset_index()
        top_segment = segment_sales.loc[segment_sales['Sales'].idxmax()]
        
        return customer_sales, customer_orders, top_customer, segment_sales, top_segment

    def time_analysis(self):
      
        # Convert Order Date and Ship Date to datetime
        self.df['Order Date'] = pd.to_datetime(self.df['Order Date'], format='%d/%m/%Y')
        self.df['Ship Date'] = pd.to_datetime(self.df['Ship Date'], format='%d/%m/%Y')
        
        # Calculate the average shipping days by each Ship Mode
        self.df['Shipping Days'] = (self.df['Ship Date'] - self.df['Order Date']).dt.days
        avg_shipping_days = self.df.groupby('Ship Mode')['Shipping Days'].mean().reset_index()
        
        # Determine the time period with the most orders
        self.df['Year-Month'] = self.df['Order Date'].dt.to_period('M')
        self.df['Quarter'] = self.df['Order Date'].dt.to_period('Q')
        self.df['Year'] = self.df['Order Date'].dt.year
        
        monthly_orders = self.df['Year-Month'].value_counts().reset_index()
        monthly_orders.columns = ['Year-Month', 'Order Count']
        
        quarterly_orders = self.df['Quarter'].value_counts().reset_index()
        quarterly_orders.columns = ['Quarter', 'Order Count']
        
        yearly_orders = self.df['Year'].value_counts().reset_index()
        yearly_orders.columns = ['Year', 'Order Count']
        
        return avg_shipping_days, monthly_orders, quarterly_orders, yearly_orders
    