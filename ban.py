from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)

# ================== FILE DATA ==================
<<<<<<< HEAD
DATA_FILE = "data/ban.json"
MENU_FILE = "data/menu.json"


# ================== HÀM DÙNG CHUNG ==================
def doc_ban():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, encoding="utf-8") as f:
=======
DATA_BAN = "data/ban.json"
DATA_MENU = "data/menu.json"


# ================== HÀM DÙNG CHUNG ==================
def doc_json(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
>>>>>>> origin/memberC
        return json.load(f)


def ghi_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


<<<<<<< HEAD
def doc_mon():
    if not os.path.exists(MENU_FILE):
        return []
    with open(MENU_FILE, encoding="utf-8") as f:
        return json.load(f)


def ghi_mon(ds):
    with open(MENU_FILE, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=2)


=======
>>>>>>> origin/memberC
# ================== MÀN HÌNH CHÍNH ==================
@app.route("/")
def home():
    return redirect("/main")


@app.route("/main")
def main():
    return render_template("main.html")


# ================== DANH MỤC BÀN ==================
@app.route("/ban")
def danh_muc_ban():
<<<<<<< HEAD
    return render_template("ban.html", ds_ban=doc_ban())


@app.route("/luu", methods=["POST"])
def luu_ban():
    ds = doc_ban()
=======
    ds_ban = doc_json(DATA_BAN)
    return render_template("ban.html", ds_ban=ds_ban)


@app.route("/ban/luu", methods=["POST"])
def luu_ban():
    ds = doc_json(DATA_BAN)
>>>>>>> origin/memberC

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
<<<<<<< HEAD
        ghi_ban(ds)
=======
        ghi_json(DATA_BAN, ds)
>>>>>>> origin/memberC
        return redirect("/ban?msg=them_ok")

    # ===== SỬA =====
    if action == "sua":
        ma_cu = request.form.get("ma_cu")
        for b in ds:
            if b["so_ban"] == ma_cu:
<<<<<<< HEAD
                b["suc_chua"] = suc_chua
                b["trang_thai"] = trang_thai
                break
        ghi_ban(ds)
        return redirect(f"/ban?msg=sua_ok&ban={ma_cu}")
=======
                b["so_ban"] = so_ban
                b["suc_chua"] = suc_chua
                b["trang_thai"] = trang_thai
                break
        ghi_json(DATA_BAN, ds)
        return redirect(f"/ban?msg=sua_ok&ban={so_ban}")
>>>>>>> origin/memberC

    return redirect("/ban")


@app.route("/ban/xoa/<so_ban>")
def xoa_ban(so_ban):
<<<<<<< HEAD
    ds = [b for b in doc_ban() if b["so_ban"] != so_ban]
    ghi_ban(ds)
=======
    ds = [b for b in doc_json(DATA_BAN) if b["so_ban"] != so_ban]
    ghi_json(DATA_BAN, ds)
>>>>>>> origin/memberC
    return redirect(f"/ban?msg=xoa_ok&ban={so_ban}")


# ================== DANH MỤC MÓN ==================
@app.route("/menu")
def danh_muc_mon():
<<<<<<< HEAD
    return render_template("menu.html", ds_mon=doc_mon())


@app.route("/luu_mon", methods=["POST"])
def luu_mon():
    ds = doc_mon()
    action = request.form.get("action")
    ma = request.form.get("ma_mon")
    ten = request.form.get("ten_mon")
    gia_raw = request.form.get("gia")
    loai = request.form.get("loai")

    if not ma or not ten or not gia_raw:
        return redirect("/menu")

    try:
        gia = int(gia_raw)
    except ValueError:
=======
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
>>>>>>> origin/memberC
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

<<<<<<< HEAD
    ghi_mon(ds)
    return redirect("/menu")


@app.route("/xoa_mon/<ma>")
def xoa_mon(ma):
    ds = [m for m in doc_mon() if m["ma_mon"] != ma]
    ghi_mon(ds)
    return redirect("/menu")


=======
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


>>>>>>> origin/memberC
# ================== ĐĂNG XUẤT ==================
@app.route("/logout")
def logout():
    return redirect("/")

<<<<<<< HEAD
@app.route("/main")
def main_screen():
    return render_template("main.html")

# ================== CHẠY APP (LUÔN Ở CUỐI FILE) ==================
=======
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
>>>>>>> origin/memberC
if __name__ == "__main__":
    app.run(debug=True)
