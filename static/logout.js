function logout() {
  // Xóa thông tin đăng nhập
  localStorage.removeItem("role");
  localStorage.removeItem("username");

  // Quay về trang login
  window.location.href = "login.html";
}
