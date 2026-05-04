def category_summary(df):
    return df.groupby("category")["amount"].sum()