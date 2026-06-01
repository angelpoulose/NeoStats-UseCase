# %%
import pandas as pd
import hashlib

# %%
df1 = pd.read_csv("retail_data1.csv")
df2 = pd.read_csv("retail_data2.csv")
product_dim = pd.read_csv("product_details.csv")

print(df1.shape, df2.shape, product_dim.shape)

# %%
df = pd.concat([df1, df2], ignore_index=True)
print("Combined rows:", len(df))

# %%
df

# %%
df.info()

# %%
df=pd.DataFrame(df)
df.head()
column_list=list(df.columns)
column_list

# %%
df.isna().sum()

# %%
df = df[df['payment_status'] == 'successful']
df = df.drop_duplicates(subset='transaction_id', keep='first')
df = df.reset_index(drop=True)
print("Rows after removing duplicates:", len(df))

# %%
price_map = product_dim.set_index('product_id')['price'].to_dict()

for i in range(len(df)):
    if pd.isna(df.loc[i, 'price']):
        pid = df.loc[i, 'product_id']
        if pid in price_map:
            df.loc[i, 'price'] = price_map[pid]

print("Null prices remaining:", df['price'].isna().sum())

# %%
df = df.dropna(subset=['price'])

# %%
df.isna().sum()

# %%
df.duplicated().sum()

# %%
def fix_date(val):
    val = str(val).strip()
    if val.replace('.', '').isdigit():
        return pd.Timestamp('1899-12-30') + pd.Timedelta(days=int(float(val)))
    try:
        return pd.to_datetime(val, dayfirst=True)
    except:
        return pd.NaT

# %%
category_map = {
    'elec': 'Electronics',
    'electronics': 'Electronics',
    'furn': 'Furniture',
    'furniture': 'Furniture',
    'cloth': 'Clothing',
    'clothing': 'Clothing',
    'home': 'Home Appliances',
    'home appliances': 'Home Appliances'
}

df['category'] = df['category'].str.strip().str.lower().map(category_map)
print(df['category'].value_counts())

# %%
df

# %%
df['product_name'] = df['product_name'].str.strip().str.title()
df['city'] = df['city'].str.strip().str.title()
df['purchase_location'] = df['purchase_location'].str.strip().str.lower()
df['payment_method'] = df['payment_method'].str.strip().str.title()
df['customer_name'] = df['customer_name'].str.strip().str.title()

# %%
print("Rows with qty <= 0:", len(df[df['quantity'] <= 0]))
df = df[df['quantity'] > 0]
df = df.reset_index(drop=True)

# %%
def mask(value):
    return hashlib.sha256(str(value).encode()).hexdigest()[:16]

df['email'] = df['email'].apply(mask)
df['phone'] = df['phone'].apply(mask)

# %%
df.head()

# %%
df['revenue'] = df['price'] * df['quantity'] * (1 - df['discount'])
df['revenue'] = df['revenue'].round(2)
df.head()

# %%
df = df.merge(
    product_dim[['product_id', 'product_name', 'category']].rename(columns={
        'product_name': 'standard_product_name',
        'category': 'standard_category'
    }),
    on='product_id',
    how='left'
)

# %%
df.head()

# %%
print("Final shape:", df.shape)
print("\nNull check:")
print(df.isna().sum())
print("\nSample:")
df.head()

# %%
total_revenue = df['revenue'].sum()
print(f"Total Revenue: {total_revenue:,.2f}")

revenue_by_category = df.groupby('standard_category')['revenue'].sum().reset_index()
revenue_by_category.columns = ['category', 'total_revenue']
revenue_by_category = revenue_by_category.sort_values('total_revenue', ascending=False)
print(revenue_by_category)

revenue_by_city = df.groupby('city')['revenue'].sum().reset_index()
revenue_by_city.columns = ['city', 'total_revenue']
revenue_by_city = revenue_by_city.sort_values('total_revenue', ascending=False)
print(revenue_by_city)

# %%
df.to_csv("curated_retail_data.csv", index=False)
revenue_by_category.to_csv("kpi_by_category.csv", index=False)
revenue_by_city.to_csv("kpi_by_city.csv", index=False)

print("Done")

# %% [markdown]
# # Visualisations

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# %%
plt.figure(figsize=(7,7))
plt.pie(revenue_by_category['total_revenue'],
        labels=revenue_by_category['category'],
        autopct='%1.1f%%',
        startangle=140)
plt.title('Revenue by Category')
plt.show()

# %%
plt.figure(figsize=(8,5))
plt.bar(revenue_by_city['city'], revenue_by_city['total_revenue'], color='steelblue')
plt.title('Revenue by City')
plt.xlabel('City')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(8,5))
plt.barh(revenue_by_category['category'], revenue_by_category['total_revenue'], color='coral')
plt.title('Revenue by Category')
plt.xlabel('Total Revenue')
plt.tight_layout()
plt.show()

# %%
df['month'] = df['transaction_date'].dt.to_period('M')
monthly_revenue = df.groupby('month')['revenue'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker='o', color='tomato')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(8,5))
plt.scatter(df['discount'], df['revenue'], alpha=0.3, color='darkorange')
plt.title('Revenue vs Discount')
plt.xlabel('Discount')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='standard_category', hue='standard_category', palette='Set2', legend=False)
plt.title('Number of Transactions by Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# %%
location_revenue = df.groupby('purchase_location')['revenue'].sum()

plt.figure(figsize=(6,6))
plt.pie(location_revenue,
        labels=location_revenue.index,
        autopct='%1.1f%%',
        colors=['#66b3ff','#ff9999'],
        startangle=90)
plt.title('Online vs Offline Revenue')
plt.show()

# %%



