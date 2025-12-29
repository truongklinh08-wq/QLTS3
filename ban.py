from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)

# ================== FILE DATA ==================
DATA_BAN = "data/ban.json"
DATA_MENU = "data/menu.json"


# ================== HÀM DÙNG CHUNG ==================
def doc_json(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def ghi_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ================== MÀN HÌNH CHÍNH ==================
@app.route("/")
def home():
    return redirect("/main")


@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        role = request.form.get("role")

        if not username or not password:
            return redirect("/register")

        path = "data/users.json"
        users = doc_json(path)

        users.append({
            "username": username,
            "password": password,
            "role": role
        })

        ghi_json(path, users)

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        users = doc_json("data/users.json")

        for u in users:
            if u["username"] == username and u["password"] == password:
                return redirect("/main")  # ✅ đăng nhập đúng

        return redirect("/login")  # ❌ sai tài khoản

    return render_template("login.html")



# ================== DANH MỤC BÀN ==================
@app.route("/ban")
def danh_muc_ban():
    ds_ban = doc_json(DATA_BAN)
    return render_template("ban.html", ds_ban=ds_ban)


@app.route("/ban/luu", methods=["POST"])
def luu_ban():
    ds = doc_json(DATA_BAN)

    action = request.form.get("action")
    so_ban = request.form.get("so_ban")
    suc_raw = request.form.get("suc_chua")
    trang_thai = request.form.get("trang_thai") == "1"

    if not so_ban or not suc_raw:
        return redirect("/ban")

    try:
        suc_chua = int(suc_raw)
    except:
        return redirect("/ban")

    # ===== THÊM =====
    if action == "them":
        ds.append({
            "so_ban": so_ban,
            "suc_chua": suc_chua,
            "trang_thai": trang_thai
        })
        ghi_json(DATA_BAN, ds)
        return redirect("/ban?msg=them_ok")

    # ===== SỬA =====
    if action == "sua":
        ma_cu = request.form.get("ma_cu")
        for b in ds:
            if b["so_ban"] == ma_cu:
                b["so_ban"] = so_ban
                b["suc_chua"] = suc_chua
                b["trang_thai"] = trang_thai
                break
        ghi_json(DATA_BAN, ds)
        return redirect(f"/ban?msg=sua_ok&ban={so_ban}")

    return redirect("/ban")


@app.route("/ban/xoa/<so_ban>")
def xoa_ban(so_ban):
    ds = [b for b in doc_json(DATA_BAN) if b["so_ban"] != so_ban]
    ghi_json(DATA_BAN, ds)
    return redirect(f"/ban?msg=xoa_ok&ban={so_ban}")


# ================== DANH MỤC MÓN ==================
@app.route("/menu")
def danh_muc_mon():
    ds_mon = doc_json(DATA_MENU)
    return render_template("menu.html", ds_mon=ds_mon)


@app.route("/menu/luu", methods=["POST"])
def luu_mon():
    ds = doc_json(DATA_MENU)

    action = request.form.get("action")
    ma = request.form.get("ma_mon")
    ten = request.form.get("ten_mon")
    gia_raw = request.form.get("gia")
    loai = request.form.get("loai")

    if not ma or not ten or not gia_raw:
        return redirect("/menu")

    try:
        gia = int(gia_raw)
    except:
        return redirect("/menu")

    if action == "them":
        ds.append({
            "ma_mon": ma,
            "ten_mon": ten,
            "gia": gia,
            "loai": loai
        })

    if action == "sua":
        for m in ds:
            if m["ma_mon"] == ma:
                m["ten_mon"] = ten
                m["gia"] = gia
                m["loai"] = loai
                break

    ghi_json(DATA_MENU, ds)
    return redirect("/menu")


@app.route("/menu/xoa/<ma>")
def xoa_mon(ma):
    ds = [m for m in doc_json(DATA_MENU) if m["ma_mon"] != ma]
    ghi_json(DATA_MENU, ds)
    return redirect("/menu")


# ================== HÓA ĐƠN ==================
@app.route("/order")
def order():
    return render_template("order.html")


# ================== ĐĂNG XUẤT ==================
@app.route("/logout")
def logout():
    return redirect("/")

# ================== THỐNG KÊ – LỊCH SỬ HÓA ĐƠN ==================
@app.route("/statistic")
def statistic():
    path = "data/invoices.json"

    if not os.path.exists(path):
        invoices = []
    else:
        with open(path, encoding="utf-8") as f:
            invoices = json.load(f)

    tong_doanh_thu = sum(hd.get("total", 0) for hd in invoices)

    return render_template(
        "statistic.html",
        invoices=invoices,
        tong_doanh_thu=tong_doanh_thu
    )

# ================== CHẠY APP ==================
if __name__ == "__main__":
    app.run(debug=True)
