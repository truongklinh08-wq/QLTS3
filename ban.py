from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
DATA_FILE = "data/ban.json"


def doc_ban():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def ghi_ban(ds):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=2)


@app.route("/ban")
def danh_muc_ban():
    ds_ban = doc_ban()
    return render_template("ban.html", ds_ban=ds_ban, ban_sua=None)


@app.route("/them", methods=["POST"])
def them_ban():
    ds_ban = doc_ban()

    ten_ban = request.form["ten_ban"]
    vi_tri = request.form["vi_tri"]
    trang_thai = request.form["trang_thai"] == "1"

    so_ban = f"B{len(ds_ban)+1:02d}"

    ds_ban.append({
        "so_ban": so_ban,
        "ten_ban": ten_ban,
        "vi_tri": vi_tri,
        "trang_thai": trang_thai
    })

    ghi_ban(ds_ban)
    return redirect(url_for("danh_muc_ban"))


@app.route("/xoa/<so_ban>")
def xoa_ban(so_ban):
    ds_ban = doc_ban()
    ds_ban = [b for b in ds_ban if b["so_ban"] != so_ban]
    ghi_ban(ds_ban)
    return redirect(url_for("danh_muc_ban"))


@app.route("/sua/<so_ban>")
def sua_ban(so_ban):
    ds_ban = doc_ban()
    ban_sua = next((b for b in ds_ban if b["so_ban"] == so_ban), None)
    return render_template("ban.html", ds_ban=ds_ban, ban_sua=ban_sua)


@app.route("/cap_nhat", methods=["POST"])
def cap_nhat_ban():
    ds_ban = doc_ban()
    so_ban_cu = request.form["so_ban_cu"]

    for b in ds_ban:
        if b["so_ban"] == so_ban_cu:
            b["ten_ban"] = request.form["ten_ban"]
            b["vi_tri"] = request.form["vi_tri"]
            b["trang_thai"] = request.form["trang_thai"] == "1"

    ghi_ban(ds_ban)
    return redirect(url_for("danh_muc_ban"))


if __name__ == "__main__":
    app.run(debug=True)
