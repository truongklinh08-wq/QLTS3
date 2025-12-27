from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)

# ================== FILE DATA ==================
DATA_FILE = "data/ban.json"
MENU_FILE = "data/menu.json"


# ================== HÀM DÙNG CHUNG ==================
def doc_ban():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def ghi_ban(ds):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=2)


def doc_mon():
    if not os.path.exists(MENU_FILE):
        return []
    with open(MENU_FILE, encoding="utf-8") as f:
        return json.load(f)


def ghi_mon(ds):
    with open(MENU_FILE, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=2)


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
    return render_template("ban.html", ds_ban=doc_ban())


@app.route("/luu", methods=["POST"])
def luu_ban():
    ds = doc_ban()
    action = request.form.get("action")
    so_ban = request.form.get("so_ban")
    suc_raw = request.form.get("suc_chua")
    trang_thai = request.form.get("trang_thai") == "1"

    if not so_ban or not suc_raw:
        return redirect("/ban")

    try:
        suc_chua = int(suc_raw)
    except ValueError:
        return redirect("/ban")

    if action == "them":
        ds.append({
            "so_ban": so_ban,
            "suc_chua": suc_chua,
            "trang_thai": trang_thai
        })

    if action == "sua":
        for b in ds:
            if b["so_ban"] == so_ban:
                b["suc_chua"] = suc_chua
                b["trang_thai"] = trang_thai
                break

    ghi_ban(ds)
    return redirect("/ban")


@app.route("/xoa/<so_ban>")
def xoa_ban(so_ban):
    ds = [b for b in doc_ban() if b["so_ban"] != so_ban]
    ghi_ban(ds)
    return redirect(f"/ban?msg=xoa_ok&ban={so_ban}")


# ================== DANH MỤC MÓN ==================
@app.route("/menu")
def danh_muc_mon():
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

    ghi_mon(ds)
    return redirect("/menu")


@app.route("/xoa_mon/<ma>")
def xoa_mon(ma):
    ds = [m for m in doc_mon() if m["ma_mon"] != ma]
    ghi_mon(ds)
    return redirect("/menu")


# ================== ĐĂNG XUẤT ==================
@app.route("/logout")
def logout():
    return redirect("/")

@app.route("/main")
def main_screen():
    return render_template("main.html")

# ================== CHẠY APP (LUÔN Ở CUỐI FILE) ==================
if __name__ == "__main__":
    app.run(debug=True)
