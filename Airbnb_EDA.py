import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 1. LOAD DATA
# ============================================================

file_path = r"D:\🏠 Airbnb NYC Data Analytics & BI Project\data\cleaned\Airbnb_NYC_Cleaned_Analytics.csv"

df = pd.read_csv(file_path, sep="\t")

print("=" * 60)
print("AIRBNB NYC DATA ANALYSIS")
print("=" * 60)

print("\nRows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())


# ============================================================
# 2. BASIC INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("DATA INFORMATION")
print("=" * 60)

print(df.info())


# ============================================================
# 3. FIRST 5 ROWS
# ============================================================

print("\nFirst 5 Rows:")
print(df.head())


# ============================================================
# 4. STATISTICAL SUMMARY
# ============================================================

print("\nStatistical Summary:")
print(df.describe())


# ============================================================
# 5. MISSING VALUES
# ============================================================

print("\nMissing Values:")

missing = df.isnull().sum()

print(missing[missing > 0])


# ============================================================
# 6. DUPLICATE CHECK
# ============================================================

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Listing IDs:")
print(df["listing_id"].duplicated().sum())


# ============================================================
# 7. DATA TYPES
# ============================================================

print("\nData Types:")
print(df.dtypes)


# ============================================================
# 8. TOTAL LISTINGS
# ============================================================

print("\nTotal Listings:")
print(df["listing_id"].nunique())


# ============================================================
# 9. TOTAL HOSTS
# ============================================================

print("\nTotal Hosts:")
print(df["host_id"].nunique())


# ============================================================
# 10. LISTINGS BY BOROUGH
# ============================================================

borough_counts = df["borough"].value_counts()

print("\nListings by Borough:")
print(borough_counts)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=borough_counts.index,
    y=borough_counts.values
)

plt.title("Airbnb Listings by Borough")
plt.xlabel("Borough")
plt.ylabel("Number of Listings")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# ============================================================
# 11. ROOM TYPE DISTRIBUTION
# ============================================================

room_counts = df["room_type"].value_counts()

print("\nRoom Type Distribution:")
print(room_counts)

plt.figure(figsize=(9, 6))

sns.barplot(
    x=room_counts.index,
    y=room_counts.values
)

plt.title("Airbnb Listings by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Number of Listings")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# ============================================================
# 12. PRICE DISTRIBUTION
# ============================================================

print("\nAverage Price:")
print(round(df["price_usd"].mean(), 2))

print("\nMedian Price:")
print(df["price_usd"].median())

plt.figure(figsize=(10, 6))

sns.histplot(
    df["price_usd"],
    bins=50,
    kde=True
)

plt.title("Airbnb Price Distribution")
plt.xlabel("Price per Night (USD)")
plt.ylabel("Number of Listings")

plt.tight_layout()
plt.show()


# ============================================================
# 13. AVERAGE PRICE BY BOROUGH
# ============================================================

avg_price_borough = (
    df.groupby("borough")["price_usd"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Price by Borough:")
print(round(avg_price_borough, 2))

plt.figure(figsize=(10, 6))

sns.barplot(
    x=avg_price_borough.index,
    y=avg_price_borough.values
)

plt.title("Average Airbnb Price by Borough")
plt.xlabel("Borough")
plt.ylabel("Average Price (USD)")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# ============================================================
# 14. AVERAGE PRICE BY ROOM TYPE
# ============================================================

avg_price_room = (
    df.groupby("room_type")["price_usd"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Price by Room Type:")
print(round(avg_price_room, 2))

plt.figure(figsize=(10, 6))

sns.barplot(
    x=avg_price_room.index,
    y=avg_price_room.values
)

plt.title("Average Price by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Average Price (USD)")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# ============================================================
# 15. TOP 15 NEIGHBORHOODS
# ============================================================

top_neighbourhoods = (
    df["neighbourhood"]
    .value_counts()
    .head(15)
)

print("\nTop 15 Neighborhoods:")
print(top_neighbourhoods)

plt.figure(figsize=(12, 7))

sns.barplot(
    x=top_neighbourhoods.values,
    y=top_neighbourhoods.index
)

plt.title("Top 15 Neighborhoods by Listings")
plt.xlabel("Number of Listings")
plt.ylabel("Neighborhood")

plt.tight_layout()
plt.show()


# ============================================================
# 16. REVIEWS ANALYSIS
# ============================================================

print("\nAverage Reviews:")
print(round(df["number_of_reviews"].mean(), 2))

plt.figure(figsize=(10, 6))

sns.histplot(
    df["number_of_reviews"],
    bins=50
)

plt.title("Distribution of Reviews")
plt.xlabel("Number of Reviews")
plt.ylabel("Number of Listings")

plt.tight_layout()
plt.show()


# ============================================================
# 17. REVIEW SCORE ANALYSIS
# ============================================================

print("\nAverage Review Score:")
print(round(df["review_score"].mean(), 2))

plt.figure(figsize=(10, 6))

sns.histplot(
    df["review_score"],
    bins=20
)

plt.title("Distribution of Review Scores")
plt.xlabel("Review Score")
plt.ylabel("Number of Listings")

plt.tight_layout()
plt.show()


# ============================================================
# 18. AVAILABILITY ANALYSIS
# ============================================================

avg_availability = (
    df.groupby("borough")["availability_365"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Availability by Borough:")
print(round(avg_availability, 2))

plt.figure(figsize=(10, 6))

sns.barplot(
    x=avg_availability.index,
    y=avg_availability.values
)

plt.title("Average Availability by Borough")
plt.xlabel("Borough")
plt.ylabel("Available Days")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# ============================================================
# 19. PROPERTY TYPE ANALYSIS
# ============================================================

property_counts = (
    df["property_type"]
    .value_counts()
)

print("\nProperty Types:")
print(property_counts)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=property_counts.values,
    y=property_counts.index
)

plt.title("Airbnb Listings by Property Type")
plt.xlabel("Number of Listings")
plt.ylabel("Property Type")

plt.tight_layout()
plt.show()


# ============================================================
# 20. HOST ANALYSIS
# ============================================================

top_hosts = (
    df.groupby(["host_id", "host_name"])
    .agg(
        listings=("listing_id", "count"),
        average_price=("price_usd", "mean"),
        average_rating=("review_score", "mean"),
        total_reviews=("number_of_reviews", "sum")
    )
    .sort_values(
        "listings",
        ascending=False
    )
    .head(10)
)

print("\nTop 10 Hosts:")
print(top_hosts)


# ============================================================
# 21. PRICE CATEGORY
# ============================================================

price_category = (
    df["price_category"]
    .value_counts()
)

print("\nPrice Category:")
print(price_category)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=price_category.index,
    y=price_category.values
)

plt.title("Listings by Price Category")
plt.xlabel("Price Category")
plt.ylabel("Number of Listings")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# ============================================================
# 22. HOST TYPE
# ============================================================

host_type = df["host_type"].value_counts()

print("\nHost Type:")
print(host_type)

plt.figure(figsize=(9, 6))

sns.barplot(
    x=host_type.index,
    y=host_type.values
)

plt.title("Listings by Host Type")
plt.xlabel("Host Type")
plt.ylabel("Number of Listings")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# ============================================================
# 23. INSTANT BOOKING
# ============================================================

instant_booking = df["instant_bookable"].value_counts()

print("\nInstant Booking:")
print(instant_booking)

plt.figure(figsize=(7, 5))

sns.barplot(
    x=instant_booking.index,
    y=instant_booking.values
)

plt.title("Instant Booking Availability")
plt.xlabel("Instant Bookable")
plt.ylabel("Number of Listings")

plt.tight_layout()
plt.show()


# ============================================================
# 24. CORRELATION ANALYSIS
# ============================================================

numeric_columns = [
    "price_usd",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
    "review_score",
    "availability_365",
    "number_of_reviews_ltm",
    "calculated_host_listings_count",
    "host_response_rate_pct",
    "accommodates",
    "beds",
    "bathrooms",
    "estimated_annual_revenue_usd"
]

correlation = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(14, 10))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f"
)

plt.title("Airbnb Correlation Matrix")

plt.tight_layout()
plt.show()


# ============================================================
# 25. REVENUE ANALYSIS
# ============================================================

revenue_by_borough = (
    df.groupby("borough")["estimated_annual_revenue_usd"]
    .sum()
    .sort_values(ascending=False)
)

print("\nEstimated Revenue by Borough:")
print(revenue_by_borough)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=revenue_by_borough.index,
    y=revenue_by_borough.values
)

plt.title("Estimated Annual Revenue by Borough")
plt.xlabel("Borough")
plt.ylabel("Estimated Revenue (USD)")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# ============================================================
# 26. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("FINAL PROJECT SUMMARY")
print("=" * 60)

print("Total Listings:", df["listing_id"].nunique())
print("Total Hosts:", df["host_id"].nunique())
print("Average Price:", round(df["price_usd"].mean(), 2))
print("Average Rating:", round(df["review_score"].mean(), 2))
print("Average Reviews:", round(df["number_of_reviews"].mean(), 2))
print("Average Availability:", round(df["availability_365"].mean(), 2))

print("\nMost Common Borough:")
print(df["borough"].mode()[0])

print("\nMost Common Room Type:")
print(df["room_type"].mode()[0])

print("\nMost Common Property Type:")
print(df["property_type"].mode()[0])

print("\nAnalysis Completed Successfully!")