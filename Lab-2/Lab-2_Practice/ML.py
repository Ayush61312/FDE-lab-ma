from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data_warehouse/processed_sales_data.csv")

agg_df = df.groupby('customer_id').agg(
    total_purchase_amount=('total_revenue', 'sum'),
    purchase_frequency=('sale_id', 'count'),
)
agg_df['avg_transaction_value'] = (
    agg_df['total_purchase_amount'] / agg_df['purchase_frequency']
)

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(agg_df)

agg_df = df.groupby('customer_id').agg(
    total_purchase_amount=('total_revenue', 'sum'),
    purchase_frequency=('sale_id', 'count'),
)
agg_df['avg_transaction_value'] = (
    agg_df['total_purchase_amount'] / agg_df['purchase_frequency']
)

kmeans = KMeans(n_clusters=2, random_state=42)
agg_df['cluster'] = kmeans.fit_predict(X_scaled)

# Decide which cluster is VIP
vip_cluster = agg_df.groupby('cluster')['total_purchase_amount'].mean().idxmax()
agg_df['VIP_status'] = (agg_df['cluster'] == vip_cluster).astype(int)

raw_df = pd.read_csv("raw_data/sale_price.csv")
enriched_df = raw_df.merge(
    agg_df[['VIP_status']], 
    on='customer_id', 
    how='left'
)

# Save back to CSV or DB
enriched_df.to_csv("sales_with_vip.csv", index=False)
