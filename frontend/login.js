async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const res = await fetch("http://localhost:3000/api/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const data = await res.json();

  if (res.ok) {
    if (data.role === "ADMIN") {
      window.location.href = "admin.html";
    } else {
      window.location.href = "staff.html";
    }
  } else {
    document.getElementById("result").innerText = data.message;
  }
}
