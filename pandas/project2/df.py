import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./pandas/project2/chi_tieu.csv", parse_dates=["Ngày"])


nhom_loai = df.groupby("Loại")["Giá Trị"].sum().reset_index()

df["Tháng"] = df["Ngày"].dt.month

chi_tieu_theo_thang = df.groupby("Tháng")["Giá Trị"].sum().reset_index()


# with pd.ExcelWriter("./pandas/project2/bao_cao_chi_tieu.xlsx") as writer:
#     df.to_excel(writer, sheet_name="Dữ liệu chi tiêu", index=False)
#     nhom_loai.to_excel(writer, sheet_name="Chi tiêu theo danh mục")
#     chi_tieu_theo_thang.to_excel(writer, sheet_name="Chi tiêu theo tháng")

# print("Đã lưu file chi_tieu.xlsx")

# vẻ biểu đồ

nhom_loai.plot(kind="bar", title="Chi tiêu theo danh mục", ylabel="VNĐ")
plt.xticks(rotation=45)
plt.show()

chi_tieu_theo_thang.plot(kind="line", marker="o", title="Chi tiêu theo tháng", ylabel="VNĐ")
plt.xticks(rotation=45)
plt.show()