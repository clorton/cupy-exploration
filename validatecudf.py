import cudf

tips_df = cudf.read_csv("https://github.com/plotly/datasets/raw/master/tips.csv")
tips_df["tip_percentage"] = tips_df["tip"] / tips_df["total_bill"] * 100

# display average tip by dining party size
print(tips_df.groupby("size").tip_percentage.mean())
