app.post("/api/auth/login", async (req, res) => {
  const { username, password } = req.body;

  // 1. Validate
  if (!username || !password) {
    return res.status(400).json({
      message: "Thiếu username hoặc password"
    });
  }

  // 2. Kiểm tra tài khoản
  const [rows] = await db.execute(
    "SELECT * FROM users WHERE username = ? AND password = ?",
    [username, password]
  );

  if (rows.length === 0) {
    return res.status(401).json({
      message: "Sai tài khoản hoặc mật khẩu"
    });
  }

  // 3. Thành công
  res.json({
    message: "Đăng nhập thành công",
    role: rows[0].role
  });
});
