import kaggle
import os
import pandas as pd
from handler import SalesAnalysis

download_path = "/Users/collins/Documents/Python/LESSON01/pandas/project4/"

def dowload_dataset():
    file_to_check = os.path.join(download_path, "train.csv")
    if os.path.exists(file_to_check):
        print(f"✅ File {file_to_check} đã tồn tại")
    else:
        kaggle.api.dataset_download_files("rohitsahoo/sales-forecasting", path=download_path, unzip=True)
        print(f"✅ Dataset đã được tải về thư mục: {download_path}")
        print(os.listdir(download_path))

dowload_dataset()

df = pd.read_csv(os.path.join(download_path, "train.csv"))



tool = SalesAnalysis(df)

tool.revenue_by_category()

# df1 = pd.DataFrame({
#     'Riem': ['A', 'B', None, 'D', 'E'],
#     'Tuan': [10, 20, None, 40, 50],
#     'Minh': [None, None, None, 80, 100]  # Cột này toàn NaN
# })

# mean_values = df1.mean(numeric_only=True)  # Chỉ tính trung bình cho số
# print("\n🔹 Trung bình của các cột số:")
# print(mean_values)

# fill_values = {}

# for col in df1.columns:
#     print(type(col))

# print(fill_values)