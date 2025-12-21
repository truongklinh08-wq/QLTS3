// MENU nhiều loại nước
const MENU = [
  { name: "Trà sữa trân châu", price: 30000 },
  { name: "Hồng trà", price: 25000 },
  { name: "Matcha latte", price: 35000 },
  { name: "Trà đào cam sả", price: 32000 },
  { name: "Trà vải", price: 28000 },
  { name: "Trà sữa socola", price: 33000 },
  { name: "Trà sữa khoai môn", price: 34000 }
  

  
];

// Danh sách món đã gọi
let orderItems = [];

// Load menu ra select
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

// Thêm món
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

  const menuItem = MENU.find(m => m.name === product);
  if (!menuItem) return;

  const existingItem = orderItems.find(i => i.product === product);

  if (existingItem) {
    existingItem.quantity += quantity;
  } else {
    orderItems.push({
      product: product,
      quantity: quantity,
      price: menuItem.price
    });
  }

  renderOrder();
}

// Xóa món
function removeItem(product) {
  orderItems = orderItems.filter(i => i.product !== product);
  renderOrder();
}

// Hiển thị danh sách món
function renderOrder() {
  const list = document.getElementById("order-list");
  list.innerHTML = "";

  let total = 0;

  orderItems.forEach(item => {
    const itemTotal = item.quantity * item.price;
    total += itemTotal;

    const li = document.createElement("li");
    li.innerHTML = `
      <span>${item.product} x${item.quantity}</span>
      <span>
        ${itemTotal.toLocaleString()}đ
        <button onclick="removeItem('${item.product}')">✕</button>
      </span>
    `;
    list.appendChild(li);
  });

  document.getElementById("total").innerText =
    `💰 Tổng tiền: ${total.toLocaleString()}đ`;
}

// Đổi bàn → reset order
function resetOrder() {
  orderItems = [];
  renderOrder();
}

// Khi mở trang
window.onload = loadMenu;
