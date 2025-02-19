import pandas as pd

df = pd.read_csv("./pandas/project2/chi_tieu.csv", parse_dates=["Ngày"])

nhom_du_lieu_theo_loai = df.groupby(["Loại"])["Giá Trị"].sum().reset_index()


df["Tháng"] = df["Ngày"].dt.to_period("M")


chi_tieu_theo_thang = df.groupby(["Tháng"])["Giá Trị"].sum().reset_index()

print(chi_tieu_theo_thang)

with pd.ExcelWriter("./pandas/project2/bao_cao_chi_tieu2.xlsx") as writer:
    df.to_excel(writer, sheet_name="Dữ liệu chi tiêu", index=False)
    nhom_du_lieu_theo_loai.to_excel(writer, sheet_name="Chi tiêu theo danh mục", index=False)
    chi_tieu_theo_thang.to_excel(writer, sheet_name="Chi tiêu theo tháng", index=False)

print("Đã lưu file bao_cao_chi_tieu2.xlsx")
