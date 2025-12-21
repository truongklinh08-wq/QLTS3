from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
FILE = "data/ban.json"


def load_ban():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_ban(ds):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=4)


@app.route("/")
def danh_muc_ban():
    ds_ban = load_ban()
    return render_template("ban.html", ds_ban=ds_ban, ban_sua=None)


@app.route("/them", methods=["POST"])
def them_ban():
    ds = load_ban()

    ten_ban = request.form["ten_ban"]
    so_ban = int(ten_ban.replace("Bàn ", ""))
    vi_tri = request.form["vi_tri"]
    trang_thai = request.form["trang_thai"] == "Trống"

    # không cho trùng số bàn
    for b in ds:
        if b["so_ban"] == so_ban:
            return redirect("/")

    ds.append({
        "so_ban": so_ban,
        "ten_ban": ten_ban,
        "vi_tri": vi_tri,
        "trang_thai": trang_thai
    })

    save_ban(ds)
    return redirect("/")


@app.route("/sua/<int:so_ban>")
def sua_ban(so_ban):
    ds = load_ban()
    ban_sua = None

    for b in ds:
        if b["so_ban"] == so_ban:
            ban_sua = b
            break

    return render_template("ban.html", ds_ban=ds, ban_sua=ban_sua)


@app.route("/cap_nhat", methods=["POST"])
def cap_nhat():
    ds = load_ban()

    so_ban_cu = int(request.form["so_ban_cu"])
    ten_ban_moi = request.form["ten_ban"]
    so_ban_moi = int(ten_ban_moi.replace("Bàn ", ""))

    for b in ds:
        if b["so_ban"] == so_ban_cu:
            b["so_ban"] = so_ban_moi
            b["ten_ban"] = ten_ban_moi
            b["vi_tri"] = request.form["vi_tri"]
            b["trang_thai"] = request.form["trang_thai"] == "Trống"
            break

    save_ban(ds)
    return redirect("/")


@app.route("/xoa/<int:so_ban>")
def xoa_ban(so_ban):
    ds = [b for b in load_ban() if b["so_ban"] != so_ban]
    save_ban(ds)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
