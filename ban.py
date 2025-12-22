from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)
DATA_FILE = "data/ban.json"


def doc_ban():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def ghi_ban(ds):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=2)


@app.route("/")
def home():
    return redirect("/ban")


@app.route("/ban")
def danh_muc_ban():
    ds = doc_ban()
    return render_template("ban.html", ds_ban=ds)


@app.route("/luu", methods=["POST"])
def luu_ban():
    ds = doc_ban()

    action = request.form.get("action")
    so_ban = request.form.get("so_ban")
    suc_raw = request.form.get("suc_chua")
    trang_thai = request.form.get("trang_thai") == "1"

    # VALIDATE
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
        ghi_ban(ds)
        return redirect("/ban?msg=them_ok")

    if action == "sua":
        for b in ds:
            if b["so_ban"] == so_ban:
                b["suc_chua"] = suc_chua
                b["trang_thai"] = trang_thai
        ghi_ban(ds)
        return redirect(f"/ban?msg=sua_ok&ban={so_ban}")

    return redirect("/ban")


@app.route("/xoa/<so_ban>")
def xoa_ban(so_ban):
    ds = [b for b in doc_ban() if b["so_ban"] != so_ban]
    ghi_ban(ds)
    return redirect(f"/ban?msg=xoa_ok&ban={so_ban}")


if __name__ == "__main__":
    app.run(debug=True)
