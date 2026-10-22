from pathlib import Path
from typing import Tuple

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Page Configuration
st.set_page_config(
    page_title="E-Commerce Performance & RFM Dashboard",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styling theme
sns.set_theme(style='dark')


# ==========================================
# Helper Functions (Data Preparation)
# ==========================================
def create_daily_orders_df(df: pd.DataFrame) -> pd.DataFrame:
    """Menyiapkan DataFrame ringkasan order harian dan total revenue."""
    daily_orders_df = df.resample(rule='D', on='order_date').agg({
        "order_id": "nunique",
        "total_price": "sum"
    }).reset_index()
    
    daily_orders_df.rename(columns={
        "order_id": "order_count",
        "total_price": "revenue"
    }, inplace=True)
    
    return daily_orders_df


def create_sum_order_items_df(df: pd.DataFrame) -> pd.DataFrame:
    """Menghitung total kuantitas penjualan per produk."""
    sum_order_items_df = (
        df.groupby("product_name")["quantity_x"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    return sum_order_items_df


def create_bygender_df(df: pd.DataFrame) -> pd.DataFrame:
    """Menghitung jumlah customer unik berdasarkan gender."""
    bygender_df = (
        df.groupby(by="gender")["customer_id"]
        .nunique()
        .reset_index()
        .rename(columns={"customer_id": "customer_count"})
    )
    return bygender_df


def create_byage_df(df: pd.DataFrame) -> pd.DataFrame:
    """Menghitung jumlah customer unik berdasarkan kelompok usia."""
    byage_df = (
        df.groupby(by="age_group")["customer_id"]
        .nunique()
        .reset_index()
        .rename(columns={"customer_id": "customer_count"})
    )
    byage_df['age_group'] = pd.Categorical(
        byage_df['age_group'],
        categories=["Youth", "Adults", "Seniors"]
    )
    return byage_df


def create_bystate_df(df: pd.DataFrame) -> pd.DataFrame:
    """Menghitung jumlah customer unik berdasarkan state/wilayah."""
    bystate_df = (
        df.groupby(by="state")["customer_id"]
        .nunique()
        .reset_index()
        .rename(columns={"customer_id": "customer_count"})
    )
    return bystate_df


def create_rfm_df(df: pd.DataFrame) -> pd.DataFrame:
    """Menghitung metrik RFM (Recency, Frequency, Monetary) per customer."""
    rfm_df = df.groupby(by="customer_id", as_index=False).agg({
        "order_date": "max",  # Tanggal order terakhir
        "order_id": "nunique",
        "total_price": "sum"
    })
    rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]
    
    rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
    recent_date = df["order_date"].dt.date.max()
    rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)
    rfm_df.drop("max_order_timestamp", axis=1, inplace=True)
    
    return rfm_df


# ==========================================
# Load Dataset with Cache
# ==========================================
@st.cache_data
def load_all_data() -> pd.DataFrame:
    """Memuat dan memproses dataset all_data.csv dengan caching Streamlit."""
    current_dir = Path(__file__).resolve().parent
    file_path = current_dir / "all_data.csv"
    
    if not file_path.exists():
        # Fallback jika dijalankan di working directory lain
        file_path = Path("all_data.csv")
        
    df = pd.read_csv(file_path)
    
    datetime_columns = ["order_date", "delivery_date"]
    for column in datetime_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column])
            
    df.sort_values(by="order_date", inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


def main() -> None:
    # Load dataset
    all_df = load_all_data()
    
    # Rentang tanggal dari dataset
    min_date = all_df["order_date"].min().date()
    max_date = all_df["order_date"].max().date()
    
    # ==========================================
    # Sidebar Filter & Info
    # ==========================================
    with st.sidebar:
        st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=200)
        st.title("Navigasi & Filter")
        
        # Penanganan pemilihan tanggal yang aman dari unpack error
        date_input_result = st.date_input(
            label="Pilih Rentang Waktu:",
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
        
        if isinstance(date_input_result, (list, tuple)) and len(date_input_result) == 2:
            start_date, end_date = date_input_result
        else:
            start_date, end_date = min_date, max_date
            st.info("Pilih rentang tanggal lengkap (awal & akhir).")
            
        st.markdown("---")
        st.markdown(f"**Dataset Overview:**")
        st.markdown(f"- Total Transaksi: `{len(all_df):,}`")
        st.markdown(f"- Rentang Data: `{min_date}` s/d `{max_date}`")

    # Filter data utama berdasarkan rentang tanggal terpilih
    main_df = all_df[
        (all_df["order_date"].dt.date >= start_date) & 
        (all_df["order_date"].dt.date <= end_date)
    ]
    
    if main_df.empty:
        st.warning("Tidak ada transaksi pada rentang tanggal yang dipilih.")
        return

    # Siapkan dataframe agregasi
    daily_orders_df = create_daily_orders_df(main_df)
    sum_order_items_df = create_sum_order_items_df(main_df)
    bygender_df = create_bygender_df(main_df)
    byage_df = create_byage_df(main_df)
    bystate_df = create_bystate_df(main_df)
    rfm_df = create_rfm_df(main_df)

    # Header Dashboard
    st.title("🛍️ E-Commerce Sales & Customer Analytics")
    st.markdown(f"*Menampilkan data dari tanggal **{start_date}** hingga **{end_date}***")
    st.markdown("---")

    # ==========================================
    # Section 1: Daily Orders & Revenue
    # ==========================================
    st.subheader('📈 Daily Orders & Revenue')
    col1, col2 = st.columns(2)
    
    with col1:
        total_orders = daily_orders_df["order_count"].sum()
        st.metric("Total Orders", value=f"{total_orders:,}")
        
    with col2:
        total_revenue = format_currency(daily_orders_df["revenue"].sum(), "AUD", locale='es_CO')
        st.metric("Total Revenue", value=total_revenue)
        
    fig, ax = plt.subplots(figsize=(16, 7))
    ax.plot(
        daily_orders_df["order_date"],
        daily_orders_df["order_count"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.set_xlabel("Order Date", fontsize=16)
    ax.set_ylabel("Number of Orders", fontsize=16)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("---")

    # ==========================================
    # Section 2: Best & Worst Performing Product
    # ==========================================
    st.subheader("📦 Best & Worst Performing Product")
    
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(28, 10))
    colors_best = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    
    top_5_products = sum_order_items_df.head(5)
    sns.barplot(
        x="quantity_x",
        y="product_name",
        data=top_5_products,
        hue="product_name",
        palette=colors_best[:len(top_5_products)],
        legend=False,
        ax=ax[0]
    )
    ax[0].set_ylabel(None)
    ax[0].set_xlabel("Number of Sales", fontsize=22)
    ax[0].set_title("Best Performing Product", loc="center", fontsize=28)
    ax[0].tick_params(axis='y', labelsize=20)
    ax[0].tick_params(axis='x', labelsize=18)
    
    bottom_5_products = sum_order_items_df.sort_values(by="quantity_x", ascending=True).head(5)
    sns.barplot(
        x="quantity_x",
        y="product_name",
        data=bottom_5_products,
        hue="product_name",
        palette=colors_best[:len(bottom_5_products)],
        legend=False,
        ax=ax[1]
    )
    ax[1].set_ylabel(None)
    ax[1].set_xlabel("Number of Sales", fontsize=22)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Worst Performing Product", loc="center", fontsize=28)
    ax[1].tick_params(axis='y', labelsize=20)
    ax[1].tick_params(axis='x', labelsize=18)
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("---")

    # ==========================================
    # Section 3: Customer Demographics
    # ==========================================
    st.subheader("👥 Customer Demographics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sorted_gender = bygender_df.sort_values(by="customer_count", ascending=False)
        gender_colors = ["#90CAF9" if i == 0 else "#D3D3D3" for i in range(len(sorted_gender))]
        
        fig, ax = plt.subplots(figsize=(14, 8))
        sns.barplot(
            y="customer_count",
            x="gender",
            data=sorted_gender,
            hue="gender",
            palette=gender_colors,
            legend=False,
            ax=ax
        )
        ax.set_title("Number of Customer by Gender", loc="center", fontsize=24)
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=18)
        ax.tick_params(axis='y', labelsize=16)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
        
    with col2:
        sorted_age = byage_df.sort_values(by="age_group", ascending=False)
        age_colors = ["#D3D3D3", "#90CAF9", "#D3D3D3"]
        
        fig, ax = plt.subplots(figsize=(14, 8))
        sns.barplot(
            y="customer_count",
            x="age_group",
            data=sorted_age,
            hue="age_group",
            palette=age_colors[:len(sorted_age)],
            legend=False,
            ax=ax
        )
        ax.set_title("Number of Customer by Age", loc="center", fontsize=24)
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=18)
        ax.tick_params(axis='y', labelsize=16)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
        
    sorted_state = bystate_df.sort_values(by="customer_count", ascending=False)
    state_colors = ["#90CAF9" if i == 0 else "#D3D3D3" for i in range(len(sorted_state))]
    
    fig, ax = plt.subplots(figsize=(18, 8))
    sns.barplot(
        x="customer_count",
        y="state",
        data=sorted_state,
        hue="state",
        palette=state_colors,
        legend=False,
        ax=ax
    )
    ax.set_title("Number of Customer by States", loc="center", fontsize=24)
    ax.set_ylabel(None)
    ax.set_xlabel("Customer Count", fontsize=16)
    ax.tick_params(axis='y', labelsize=16)
    ax.tick_params(axis='x', labelsize=14)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("---")

    # ==========================================
    # Section 4: RFM Analysis
    # ==========================================
    st.subheader("🎯 Best Customers Based on RFM Parameters")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_recency = round(rfm_df["recency"].mean(), 1)
        st.metric("Average Recency (days)", value=f"{avg_recency} days")
        
    with col2:
        avg_frequency = round(rfm_df["frequency"].mean(), 2)
        st.metric("Average Frequency", value=f"{avg_frequency} orders")
        
    with col3:
        avg_monetary = format_currency(rfm_df["monetary"].mean(), "AUD", locale='es_CO')
        st.metric("Average Monetary", value=avg_monetary)
        
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(32, 10))
    top_rfm_color = ["#90CAF9"] * 5
    
    # Recency
    top_recency = rfm_df.sort_values(by="recency", ascending=True).head(5)
    sns.barplot(
        y="recency",
        x="customer_id",
        data=top_recency,
        hue="customer_id",
        palette=top_rfm_color,
        legend=False,
        ax=ax[0]
    )
    ax[0].set_ylabel(None)
    ax[0].set_xlabel("Customer ID", fontsize=22)
    ax[0].set_title("By Recency (days)", loc="center", fontsize=28)
    ax[0].tick_params(axis='y', labelsize=18)
    ax[0].tick_params(axis='x', labelsize=18, rotation=25)
    
    # Frequency
    top_frequency = rfm_df.sort_values(by="frequency", ascending=False).head(5)
    sns.barplot(
        y="frequency",
        x="customer_id",
        data=top_frequency,
        hue="customer_id",
        palette=top_rfm_color,
        legend=False,
        ax=ax[1]
    )
    ax[1].set_ylabel(None)
    ax[1].set_xlabel("Customer ID", fontsize=22)
    ax[1].set_title("By Frequency", loc="center", fontsize=28)
    ax[1].tick_params(axis='y', labelsize=18)
    ax[1].tick_params(axis='x', labelsize=18, rotation=25)
    
    # Monetary
    top_monetary = rfm_df.sort_values(by="monetary", ascending=False).head(5)
    sns.barplot(
        y="monetary",
        x="customer_id",
        data=top_monetary,
        hue="customer_id",
        palette=top_rfm_color,
        legend=False,
        ax=ax[2]
    )
    ax[2].set_ylabel(None)
    ax[2].set_xlabel("Customer ID", fontsize=22)
    ax[2].set_title("By Monetary", loc="center", fontsize=28)
    ax[2].tick_params(axis='y', labelsize=18)
    ax[2].tick_params(axis='x', labelsize=18, rotation=25)
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    
    st.caption('Dicoding Academy — Belajar Analisis Data dengan Python')


if __name__ == "__main__":
    main()