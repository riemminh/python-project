import pandas as pd

df = pd.read_csv("./pandas/project1/diem_sv.csv")
# Tính điểm trung bình & xếp loại sinh viên
df["Trung binh"] = df[["Toán", "Anh", "Văn"]].mean(axis=1)

trung_binh = df["Trung binh"]


def xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"


df["Xep loai"] = trung_binh.apply(xep_loai)

# Lọc danh sách sinh viên có điểm trên khá

df_kha = df.loc[df["Trung binh"] >= 6.5]

df_trungbinh = df[df["Trung binh"] <= 6.5]

print(df_trungbinh)

# Lưu kết quả ra file CSV hoặc Excel
df.to_csv("./pandas/project1/diem_sv_ket_qua.csv", index=False)

# print(df)
