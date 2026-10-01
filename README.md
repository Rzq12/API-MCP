# SEIRAMA API MCP

MCP server terpisah untuk integrasi API publik BKN.

## Menjalankan

```powershell
pip install -e .
python api_server.py
```

Endpoint: `http://127.0.0.1:8003/mcp`

Menyediakan tool statistik ASN, demografi, inovasi, dan master instansi BKN.

## Menjalankan di VPS dengan Podman Compose

Pastikan Podman dan Podman Compose tersedia di VPS, lalu siapkan konfigurasi:

```bash
cp .env.example .env
```

Sesuaikan `BKN_API_BASE_URL` di `.env`, kemudian jalankan service:

```bash
podman compose down --remove-orphans
podman compose build --no-cache
podman compose up -d
podman compose ps
podman compose logs -f seirama-api-mcp
```

MCP endpoint dapat diakses melalui `http://IP_VPS:8003/mcp`. Untuk menghentikan
service:

```bash
podman compose down
```

Port `8003` sebaiknya dibatasi melalui firewall VPS atau reverse proxy HTTPS
apabila endpoint akan diakses dari internet.
