# Giới thiệu
Đây là github repo chứa mã nguồn cho lộ trình học python backend 
Lộ trình này có thể tìm thấy trên trang web https://vimentor.com ở đường dẫn sau: https://vimentor.com/vi/learning-path/lo-trinh-hoc-python-cho-ky-su-backend?type=lesson
Group facebôk để thảo luận các vấn đề liên quan tới lộ trình học: https://www.facebook.com/groups/711152479268593/

# Cách chạy ứng dụng trên host 
### Yêu cầu 
- Ứng dụng này được viết theo python3. Nên để chạy được ứng dụng cần phải cài đặt python3 và pip3 và một số gói khác

        sudo unlink /etc/localtime 
        sudo ln -s /usr/share/zoneinfo/Etc/GMT+7 /etc/localtime
        sudo apt update 
        sudo apt install -y git python3 python3-pip libsm6 libxext6 libfontconfig1 libxrender1 python3-tk
        
- Chú ý: Trong bước "sudo unlink /etc/localtime" có thể báo lỗi nếu file /etc/localtime không tồn tại. Lệnh "sudo ln -s /usr/share/zoneinfo/Etc/GMT+7 /etc/localtime" cũng có thể báo lỗi nếu file /etc/localtime đã tồn tại. Nếu xảy ra hai lỗi này, hãy bỏ qua nó và chạy tiếp những lệnh sau. Chương trình vẫn có thể hoạt động bình thường.
### Cài các gói phụ trợ 
- Chạy lệnh sau trong thư mục pythonbackenddemo để cài các gói phụ trợ 

        pip3 install -r requirements.txt
        
### Chạy ứng dụng
- Sau khi cài đặt cái gói phụ trợ bạn có thể chạy ứng dụng bằng lênh sau, chú ý là cần đứng trong thư mục chứa mã nguồn pythonbackenddemo khi chạy lệnh này

        python3 house3d_worker_demo.py

# Chạy ứng dụng trong docker container 
### B1. Clone mã nguồn và chuyển về nhánh 6-gunicorn-flask

        git clone https://github.com/vimentor-com/pythonbackenddemo.git
        cd pythonbackenddemo
        git checkout 6-gunicorn-flask

### B2. Build docker image với lệnh

        sudo docker build . -t demoimg:v0.2

### B2. Khởi chạy docker container 

        sudo docker run -it --name='pythonbackenddemo' -p 8000:8000 demoimg:v0.2 bash

Log xuất hiện trên màn hình sau khi chạy docker container

        [2019-02-28 01:44:38 -0700] [6] [INFO] Starting gunicorn 19.9.0
        [2019-02-28 01:44:38 -0700] [6] [INFO] Listening at: http://127.0.0.1:8000 (6)
        [2019-02-28 01:44:38 -0700] [6] [INFO] Using worker: threads
        [2019-02-28 01:44:38 -0700] [9] [INFO] Booting worker with pid: 9
        [2019-02-28 01:44:38 -0700] [17] [INFO] Booting worker with pid: 17
        [2019-02-28 01:44:38 -0700] [26] [INFO] Booting worker with pid: 26
