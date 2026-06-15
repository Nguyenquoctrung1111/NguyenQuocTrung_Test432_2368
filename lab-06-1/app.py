import tkinter as tk
from tkinter import messagebox
from cipher.playfair import PlayFairCipher

class PlayfairApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phần mềm Mã hóa Playfair")
        self.root.geometry("620x380")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Khởi tạo thuật toán Playfair từ file của bạn
        self.playfair_cipher = PlayFairCipher()

        # Vẽ giao diện
        self.create_widgets()
        
        # Tự động hiển thị ma trận mặc định ban đầu
        self.get_matrix()

    def create_widgets(self):
        # --- KHUNG BÊN TRÁI: MA TRẬN 5x5 ---
        frame_left = tk.LabelFrame(self.root, text=" Ma Trận Playfair 5x5 ", bg="#f0f0f0", font=("Arial", 10, "bold"), padx=10, pady=10)
        frame_left.place(x=15, y=15, width=250, height=340)

        # Tạo mảng lưới 5x5 ô Label hiển thị ký tự
        self.matrix_labels = []
        for i in range(5):
            row_labels = []
            for j in range(5):
                lbl = tk.Label(frame_left, text="-", font=("Arial", 12, "bold"), width=3, height=1, 
                               relief="solid", bd=1, bg="white", fg="#333")
                lbl.grid(row=i, column=j, padx=4, pady=8)
                row_labels.append(lbl)
            self.matrix_labels.append(row_labels)

        # --- KHUNG BÊN PHẢI: NHẬP LIỆU & NÚT BẤM ---
        frame_right = tk.LabelFrame(self.root, text=" Xử Lý Thuật Toán ", bg="#f0f0f0", font=("Arial", 10, "bold"), padx=15, pady=10)
        frame_right.place(x=280, y=15, width=325, height=340)

        # Ô nhập Từ khóa (Key)
        tk.Label(frame_right, text="Nhập từ khóa (Key):", bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w", pady=(5,2))
        self.entry_key = tk.Entry(frame_right, font=("Arial", 11), width=32)
        self.entry_key.pack(ipady=3)
        self.entry_key.insert(0, "MONARCHY") 

        # Nút cập nhật ma trận
        btn_matrix = tk.Button(frame_right, text="Tạo / Xem Ma Trận", font=("Arial", 9, "bold"), bg="#6c757d", fg="white", command=self.get_matrix)
        btn_matrix.pack(fill="x", pady=(5, 15))

        # Ô nhập Văn bản (Input)
        tk.Label(frame_right, text="Nhập văn bản (Plain/Cipher):", bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w", pady=(0,2))
        self.entry_input = tk.Entry(frame_right, font=("Arial", 11), width=32)
        self.entry_input.pack(ipady=3)

        # Khung chứa 2 nút Mã hóa và Giải mã nằm ngang
        frame_btns = tk.Frame(frame_right, bg="#f0f0f0")
        frame_btns.pack(fill="x", pady=15)

        btn_encrypt = tk.Button(frame_btns, text="🔒 Mã Hóa", font=("Arial", 10, "bold"), bg="#0d6efd", fg="white", width=12, command=self.handle_encrypt)
        btn_encrypt.pack(side="left", padx=5)

        btn_decrypt = tk.Button(frame_btns, text="🔓 Giải Mã", font=("Arial", 10, "bold"), bg="#198754", fg="white", width=12, command=self.handle_decrypt)
        btn_decrypt.pack(side="right", padx=5)

        # Khung hiển thị kết quả cuối cùng
        tk.Label(frame_right, text="KẾT QUẢ:", bg="#f0f0f0", font=("Arial", 10, "bold"), fg="#333").pack(anchor="w")
        self.lbl_result_val = tk.Label(frame_right, text="...", font=("Arial", 14, "bold"), bg="#e9ecef", fg="#dc3545", height=2, width=25, relief="groove")
        self