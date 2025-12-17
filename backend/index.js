const express = require("express");
const cors = require("cors");

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

// TEST SERVER
app.get("/", (req, res) => {
  res.send("Backend is running 🚀");
});

// API đăng ký
app.post("/api/auth/register", (req, res) => {
  const { username, password, role } = req.body;

  if (!username || !password) {
    return res.status(400).json({
      message: "Thiếu username hoặc password"
    });
  }

  return res.json({
    message: "Đăng ký thành công",
    role
  });
});

// API đăng nhập
app.post("/api/auth/login", (req, res) => {
  const { username, password } = req.body;

  if (username === "admin" && password === "123") {
    return res.json({ role: "ADMIN" });
  }

  return res.json({ role: "STAFF" });
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
