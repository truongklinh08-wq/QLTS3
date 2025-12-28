// ================= MENU (GIỮ NGUYÊN, KHÔNG ĐỤNG) =================
const MENU = [
  { name: "Trà sữa trân châu", price: 30000 },
  { name: "Hồng trà", price: 25000 },
  { name: "Matcha latte", price: 35000 },
  { name: "Trà đào cam sả", price: 32000 },
  { name: "Trà vải", price: 28000 },
  { name: "Trà sữa socola", price: 33000 },
  { name: "Trà sữa khoai môn", price: 34000 }
];

// ================= BIẾN =================
let orderItems = [];
let currentTable = "";

// ================= LOAD MENU =================
function loadMenu() {
  const select = document.getElementById("product");
  select.innerHTML = "";

  MENU.forEach(item => {
    const option = document.createElement("option");
    option.value = item.name;
    option.textContent = `${item.name} (${item.price.toLocaleString()}đ)`;
    select.appendChild(option);
  });
}

// ================= THÊM MÓN =================
function addItem() {
  const table = document.getElementById("table").value;
  const product = document.getElementById("product").value;
  const quantity = parseInt(document.getElementById("quantity").value);

  if (!table) {
    alert("Vui lòng chọn bàn trước khi gọi món");
    return;
  }

  if (quantity <= 0) {
    alert("Số lượng phải lớn hơn 0");
    return;
  }

  currentTable = table;

  const menuItem = MENU.find(m => m.name === product);
  if (!menuItem) return;

  const exist = orderItems.find(i => i.product === product);

  if (exist) {
    exist.quantity += quantity;
  } else {
    orderItems.push({
      product: product,
      quantity: quantity,
      price: menuItem.price
    });
  }

  renderOrder();
}

// ================= XÓA MÓN =================
function removeItem(product) {
  orderItems = orderItems.filter(i => i.product !== product);
  renderOrder();
}

// ================= HIỂN THỊ HÓA ĐƠN =================
function renderOrder() {
  const list = document.getElementById("order-list");
  list.innerHTML = "";

  let total = 0;

  orderItems.forEach(item => {
    const itemTotal = item.quantity * item.price;
    total += itemTotal;

    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${item.product}</td>
      <td>${item.price.toLocaleString()}đ</td>
      <td>${item.quantity}</td>
      <td>${itemTotal.toLocaleString()}đ</td>
      <td>
        <button onclick="removeItem('${item.product}')">❌</button>
      </td>
    `;
    list.appendChild(tr);
  });

  document.getElementById("total").innerText =
    `💰 Tổng tiền: ${total.toLocaleString()}đ`;
}

// ================= ĐỔI BÀN =================
function resetOrder() {
  orderItems = [];
  currentTable = "";
  renderOrder();
}

// ================= LƯU HÓA ĐƠN =================
function saveInvoice() {
  if (orderItems.length === 0) {
    alert("Chưa có món để lưu hóa đơn");
    return;
  }

  const invoice = {
    table: currentTable,
    items: orderItems,
    total: orderItems.reduce((s, i) => s + i.price * i.quantity, 0),
    time: new Date().toLocaleString()
  };

  const history = JSON.parse(localStorage.getItem("invoice_history") || "[]");
  history.push(invoice);
  localStorage.setItem("invoice_history", JSON.stringify(history));

  alert("✅ Đã lưu hóa đơn");
  resetOrder();
  loadInvoiceHistory();
}

// ================= LỊCH SỬ HÓA ĐƠN =================
function loadInvoiceHistory() {
  const list = document.getElementById("invoice-history");
  if (!list) return;

  list.innerHTML = "";
  const history = JSON.parse(localStorage.getItem("invoice_history") || "[]");

  history.forEach(inv => {
    const li = document.createElement("li");
    li.innerText = `🧾 Bàn ${inv.table} - ${inv.total.toLocaleString()}đ (${inv.time})`;
    list.appendChild(li);
  });
}

// ================= KHI MỞ TRANG =================
window.onload = () => {
  loadMenu();
  loadInvoiceHistory();
};
