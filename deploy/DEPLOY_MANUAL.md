# SỔ TAY HƯỚNG DẪN TRIỂN KHAI PRODUCTION (DEPLOYMENT RUNBOOK)
**Hệ thống:** HAIChain Autonomous Agent Gateway & Economic Relayer  
**Mục tiêu:** Đưa hệ thống lên máy chủ VPS độc lập (Ubuntu 22.04 LTS / 24.04 LTS) với tên miền riêng và chứng chỉ SSL HTTPS.

---

## I. YÊU CẦU MÁY CHỦ TỐI THIỂU
* **Hệ điều hành:** Ubuntu 22.04 / 24.04 LTS hoặc Debian 12
* **Cấu hình phần cứng:** 1 vCPU, 1 GB RAM, 15 GB SSD (Gói \$4 - \$6/tháng trên DigitalOcean / Hetzner / Vultr)
* **Phần mềm:** Node.js v20.x LTS, NPM v10.x, Git

---

## II. QUY TRÌNH TRIỂN KHAI NHANH TRONG 4 BƯỚC

### Bước 1: Kết nối VPS & Cài đặt môi trường
```bash
# Cập nhật hệ thống
sudo apt update && sudo apt upgrade -y

# Cài đặt Node.js 20 LTS & Git
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs git build-essential

# Cài đặt PM2 để duy trì tiến trình chạy 24/7
sudo npm install -g pm2
```

### Bước 2: Tải kho mã nguồn HAIChain & Biên dịch
```bash
# Clone kho mã nguồn
git clone https://github.com/haichainsi/haichain.git
cd haichain

# Cài đặt dependencies và build package
npm install --prefix packages/agent-pay
npm run build --prefix packages/agent-pay
npm install --prefix mcp-server
npm run build --prefix mcp-server
```

### Bước 3: Khởi chạy Gateway với PM2
```bash
# Cấp quyền chạy script
chmod +x deploy/start-production.sh

# Khởi chạy ứng dụng
./deploy/start-production.sh

# Cấu hình tự động khởi động lại khi reboot VPS
pm2 save
sudo env PATH=$PATH:/usr/bin pm2 startup systemd -u $USER --hp $HOME
```

### Bước 4: Cấu hình Nginx & Chứng chỉ SSL Miễn phí (Let's Encrypt)
```bash
# Cài đặt Nginx và Certbot
sudo apt install -y nginx certbot python3-certbot-nginx

# Sao chép file cấu hình
sudo cp deploy/nginx-haichain.conf /etc/nginx/sites-available/haichain
sudo ln -s /etc/nginx/sites-available/haichain /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

# Thay đổi tên miền của bạn (ví dụ app.haichain.io)
sudo nano /etc/nginx/sites-available/haichain

# Cấp chứng chỉ SSL tự động
sudo certbot --nginx -d app.haichain.io

# Khởi động lại Nginx
sudo nginx -t && sudo systemctl reload nginx
```

---

## III. KIỂM THỬ XÁC NHẬN SAU KHI TRIỂN KHAI

Kiểm tra trạng thái máy chủ:
```bash
curl https://app.haichain.io/status
```
Kết quả mong đợi:
```json
{
  "status": "ONLINE",
  "service": "HAICHAIN Production Agent Relayer & Unified Gateway (Real On-Chain)",
  "protocols": ["HTTP 402", "MCP JSON-RPC", "Solana Devnet Micro-Escrow"],
  "payerWallet": "HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW",
  "oracleRate": "1 SOL = 200 USDT"
}
```
Mở trình duyệt truy cập `https://app.haichain.io`, mở tab **Developer Docs** hoặc tab **AI Agent Swarm** để bắt đầu trải nghiệm!
