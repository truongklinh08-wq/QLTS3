const express = require("express");
const fs = require("fs");
const router = express.Router();

const FILE_PATH = "./data/invoices.json";

// Đọc danh sách hóa đơn
function readInvoices() {
  if (!fs.existsSync(FILE_PATH)) return [];
  return JSON.parse(fs.readFileSync(FILE_PATH, "utf-8"));
}

// Ghi danh sách hóa đơn
function saveInvoices(data) {
  fs.writeFileSync(FILE_PATH, JSON.stringify(data, null, 2), "utf-8");
}

// ================= API =================

// POST /api/invoices  -> lưu hóa đơn mới
router.post("/", (req, res) => {
  const invoices = readInvoices();

  const newInvoice = {
    id: Date.now(),
    time: new Date().toLocaleString(),
    items: req.body.items,
    total: req.body.total
  };

  invoices.push(newInvoice);
  saveInvoices(invoices);

  res.json({
    message: "Lưu hóa đơn thành công",
    invoice: newInvoice
  });
});

// GET /api/invoices -> lấy lịch sử hóa đơn
router.get("/", (req, res) => {
  res.json(readInvoices());
});

module.exports = router;
