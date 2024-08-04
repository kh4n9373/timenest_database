1.
check:
- python --version
- conda --version
- pip --version

thiếu gì tải nấy, đến khi nào chạy được lệnh check version

2. Tạo môi trường anaconda 
```
conda create --name timenest 
conda activate timenest
```

3. Clone repo này về  rồi cài đặt file thư viện

```
git clone https://github.com/kh4n9373/SwinDatabase.git
cd SwinDatabase/
```

cài đặt
```
pip install -r requirements.txt
```
xong thì mở VSCode lên 
```
code . 
```

4. Copy key ở file .env, paste vào new connection trong mongodb rồi connect 


Xong setup, 

## Nhap du lieu vao database

5. file test.py là example khi thêm 1 record mới vào bảng:
```
data = {
  "UserID": 1223456789,
  "UserName": "sucvatanhtuananmandaikhai",
  "Password": "anhnhoem",
  "Calendar": {
    "$oid": "123456"
  }
}

mongo_client.insert_one(
    collection_name='user',
    data=data
)
```
với data truyền vào là một dictionary trong python (json)

đọc mongodb.py để sử dụng các hàm khi muốn thao tác vào database, ngoài insert_one còn có insert_many, 
upsert_one, upsert_many, ... (từng hàm dùng thế nào t sẽ nói lúc họp)

6. Insert xong có thể vào mongodb để check thay đổi 