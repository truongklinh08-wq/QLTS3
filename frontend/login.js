async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch("http://localhost:3000/api/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (res.ok) {
        alert("Đăng nhập thành công!");

        // 👉 CHUYỂN THẲNG SANG MÀN HÌNH CHÍNH (FLASK)
        window.location.href = "http://127.0.0.1:5000/main";
    } else {
        alert(data.message || "Sai tài khoản hoặc mật khẩu");
    }
}
