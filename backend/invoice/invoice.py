# =========================
# FORM HOA DON - QUAN LY TRA SUA
# Phu trach: Thanh vien (Form Hoa Don)
# =========================

current_invoice = []
invoice_history = []

def create_invoice():
    global current_invoice
    current_invoice = []
    print("🧾 Đã tạo hóa đơn mới.")

def add_item():
    name = input("Tên món: ")
    price = float(input("Giá món: "))
    quantity = int(input("Số lượng: "))

    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    current_invoice.append(item)
    print("✅ Đã thêm món vào hóa đơn.")

def show_invoice():
    if not current_invoice:
        print("⚠️ Hóa đơn hiện tại trống.")
        return

    print("\n--- HÓA ĐƠN HIỆN TẠI ---")
    for i, item in enumerate(current_invoice, start=1):
        total = item["price"] * item["quantity"]
        print(f"{i}. {item['name']} | {item['quantity']} x {item['price']} = {total}")

def calculate_total():
    total = 0
    for item in current_invoice:
        total += item["price"] * item["quantity"]
    print(f"💰 Tổng tiền: {total} VND")
    return total

def save_invoice():
    if not current_invoice:
        print("⚠️ Không có hóa đơn để lưu.")
        return

    total = calculate_total()
    invoice_history.append({
        "items": current_invoice.copy(),
        "total": total
    })
    print("📦 Đã lưu hóa đơn vào lịch sử.")

def show_invoice_history():
    if not invoice_history:
        print("⚠️ Chưa có hóa đơn nào trong lịch sử.")
        return

    print("\n=== LỊCH SỬ HÓA ĐƠN ===")
    for i, inv in enumerate(invoice_history, start=1):
        print(f"\nHóa đơn #{i} - Tổng tiền: {inv['total']}")
        for item in inv["items"]:
            print(f"- {item['name']} ({item['quantity']} x {item['price']})")

def invoice_menu():
    while True:
        print("\n--- FORM HÓA ĐƠN ---")
        print("1. Tạo hóa đơn mới")
        print("2. Thêm món")
        print("3. Hiển thị hóa đơn")
        print("4. Tính tổng tiền")
        print("5. Lưu hóa đơn")
        print("6. Lịch sử hóa đơn")
        print("7. Thoát")

        choice = input("Chọn chức năng (1-7): ")

        if choice == '1':
            create_invoice()
        elif choice == '2':
            add_item()
        elif choice == '3':
            show_invoice()
        elif choice == '4':
            calculate_total()
        elif choice == '5':
            save_invoice()
        elif choice == '6':
            show_invoice_history()
        elif choice == '7':
            break
        else:
            print("❌ Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    invoice_menu()

