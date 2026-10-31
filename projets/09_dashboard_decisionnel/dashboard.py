import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Olist E-commerce Dashboard", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    df_customers = pd.read_csv('data/olist_customers_dataset.csv')
    df_orders = pd.read_csv('data/olist_orders_dataset.csv')
    df_products = pd.read_csv('data/olist_products_dataset.csv')
    df_order_items = pd.read_csv('data/olist_order_items_dataset.csv')
    df_order_payments = pd.read_csv('data/olist_order_payments_dataset.csv')
    df_category_translation = pd.read_csv('data/product_category_name_translation.csv')
    
    date_cols = ['order_purchase_timestamp', 'order_approved_at', 
                 'order_delivered_carrier_date', 'order_delivered_customer_date',
                 'order_estimated_delivery_date']
    for col in date_cols:
        df_orders[col] = pd.to_datetime(df_orders[col], errors='coerce')
    
    df_orders_delivered = df_orders[df_orders['order_status'] == 'delivered'].copy()
    df_products = df_products.merge(df_category_translation, on='product_category_name', how='left')
    
    df_sales = df_orders_delivered.merge(df_order_items, on='order_id', how='left')
    df_sales = df_sales.merge(df_products[['product_id', 'product_category_name_english']], on='product_id', how='left')
    df_sales = df_sales.merge(df_customers, on='customer_id', how='left')
    df_sales = df_sales.merge(df_order_payments[['order_id', 'payment_type']], on='order_id', how='left')
    
    df_sales['order_month'] = df_sales['order_purchase_timestamp'].dt.to_period('M').astype(str)
    df_sales['order_year'] = df_sales['order_purchase_timestamp'].dt.year
    
    return df_sales

df = load_data()

st.title(" Olist E-commerce Analytics Dashboard")
st.markdown("---")

st.sidebar.header(" Filters")
years = st.sidebar.multiselect("Year:", options=sorted(df['order_year'].unique()), default=sorted(df['order_year'].unique()))
states = st.sidebar.multiselect("State:", options=sorted(df['customer_state'].unique()), default=sorted(df['customer_state'].unique())[:5])
categories = st.sidebar.multiselect("Category:", options=sorted(df['product_category_name_english'].dropna().unique()), default=sorted(df['product_category_name_english'].dropna().unique())[:5])

df_filtered = df[
    (df['order_year'].isin(years)) & 
    (df['customer_state'].isin(states)) &
    (df['product_category_name_english'].isin(categories))
]

st.subheader(" Key Performance Indicators")
col1, col2, col3, col4, col5 = st.columns(5)

total_revenue = df_filtered['price'].sum()
total_orders = df_filtered['order_id'].nunique()
avg_order_value = df_filtered.groupby('order_id')['price'].sum().mean()
total_customers = df_filtered['customer_id'].nunique()
avg_orders_per_customer = total_orders / total_customers if total_customers > 0 else 0

col1.metric(" Total Revenue", f"R$ {total_revenue:,.0f}")
col2.metric(" Avg Order", f"R$ {avg_order_value:.2f}")
col3.metric(" Orders", f"{total_orders:,}")
col4.metric(" Customers", f"{total_customers:,}")
col5.metric(" Orders/Customer", f"{avg_orders_per_customer:.2f}")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader(" Monthly Revenue Trend")
    monthly = df_filtered.groupby('order_month')['price'].sum().reset_index()
    fig_monthly = px.line(monthly, x='order_month', y='price', markers=True)
    fig_monthly.update_layout(xaxis_title="Month", yaxis_title="Revenue (R$)")
    st.plotly_chart(fig_monthly, use_container_width=True)

with col2:
    st.subheader(" Top 10 Categories")
    cat_rev = df_filtered.groupby('product_category_name_english')['price'].sum().sort_values(ascending=False).head(10).reset_index()
    fig_cat = px.bar(cat_rev, x='product_category_name_english', y='price', color='price', color_continuous_scale='Blues')
    fig_cat.update_layout(xaxis_title="Category", yaxis_title="Revenue (R$)", xaxis_tickangle=45)
    st.plotly_chart(fig_cat, use_container_width=True)

st.subheader(" Revenue by State")
state_rev = df_filtered.groupby('customer_state')['price'].sum().sort_values(ascending=False).reset_index()
fig_state = px.bar(state_rev, x='customer_state', y='price', color='price', color_continuous_scale='Viridis')
fig_state.update_layout(xaxis_title="State", yaxis_title="Revenue (R$)")
st.plotly_chart(fig_state, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader(" Order Value Distribution")
    order_vals = df_filtered.groupby('order_id')['price'].sum()
    fig_dist = px.histogram(order_vals, x='price', nbins=50)
    fig_dist.update_layout(xaxis_title="Order Value (R$)", yaxis_title="Number of Orders")
    st.plotly_chart(fig_dist, use_container_width=True)

with col2:
    st.subheader(" Payment Methods")
    payment_counts = df_filtered.groupby('order_id')['payment_type'].first().value_counts().reset_index()
    payment_counts.columns = ['payment_type', 'count']
    fig_pay = px.pie(payment_counts, values='count', names='payment_type', hole=0.4)
    st.plotly_chart(fig_pay, use_container_width=True)

st.markdown("---")
st.subheader(" Business Recommendations")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("** Growth Strategy**\n- Focus marketing on peak months\n- Increase inventory before seasonal peaks\n- Target high-value customer segments")

with col2:
    st.success("** Category Focus**\n- Expand health_beauty offering\n- Create bundles with watches_gifts\n- Optimize bed_bath_table logistics")

with col3:
    st.warning("** Geographic Expansion**\n- Concentrate on SP and RJ markets\n- Test underperforming regions\n- Optimize delivery times")

st.markdown("---")
st.caption(f"Dashboard | Data: Olist Brazilian E-commerce | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")