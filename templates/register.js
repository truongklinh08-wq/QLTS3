async function register() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const role = document.getElementById("role").value;

  const res = await fetch("http://localhost:3000/api/auth/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ username, password, role })
  });

  const data = await res.json();

  if (res.ok) {
    document.getElementById("result").innerText = "Đăng ký thành công";

    // 👉 CHỜ 1 GIÂY RỒI CHUYỂN SANG FORM ĐĂNG NHẬP
    setTimeout(() => {
      window.location.href = "login.html";
    }, 1000);

  } else {
    document.getElementById("result").innerText = data.message;
  }
}
