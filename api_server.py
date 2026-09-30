import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from mcp.server.fastmcp import FastMCP
from seirama_mcp.integrations.bkn import call, pagination

mcp = FastMCP("seirama-api", host="0.0.0.0", port=8003)

def listing(path, page, size):
    return call(path, pagination(page, size))

@mcp.tool()
def get_bkn_asn(page=0, size=20):
    """Mengambil statistik ASN dari API publik BKN."""
    return listing("/api/public/asn", page, size)

@mcp.tool()
def get_bkn_asn_by_id(id):
    """Mengambil statistik ASN berdasarkan ID."""
    return call(f"/api/public/asn/{id}")

@mcp.tool()
def get_bkn_asn_total(idbkn):
    """Mengambil total ASN berdasarkan ID BKN instansi."""
    return call(f"/api/public/asn/total/{idbkn}")

@mcp.tool()
def get_bkn_asn_by_idbkn(idbkn):
    """Mengambil statistik ASN berdasarkan ID BKN instansi."""
    return call(f"/api/public/asn/idbkn/{idbkn}")

@mcp.tool()
def get_bkn_asn_count():
    """Mengambil jumlah record statistik ASN."""
    return call("/api/public/asn/count")

@mcp.tool()
def get_bkn_demografi(page=0, size=20):
    """Mengambil statistik demografi dari API publik BKN."""
    return listing("/api/public/demografi", page, size)

@mcp.tool()
def get_bkn_demografi_by_id(id):
    """Mengambil statistik demografi berdasarkan ID."""
    return call(f"/api/public/demografi/{id}")

@mcp.tool()
def get_bkn_demografi_by_idbkn(idbkn):
    """Mengambil statistik demografi berdasarkan ID BKN instansi."""
    return call(f"/api/public/demografi/idbkn/{idbkn}")

@mcp.tool()
def get_bkn_demografi_count():
    """Mengambil jumlah record statistik demografi."""
    return call("/api/public/demografi/count")

@mcp.tool()
def get_bkn_inovasi(page=0, size=20):
    """Mengambil statistik inovasi dari API publik BKN."""
    return listing("/api/public/inovasi", page, size)

@mcp.tool()
def get_bkn_inovasi_by_id(id):
    """Mengambil statistik inovasi berdasarkan ID."""
    return call(f"/api/public/inovasi/{id}")

@mcp.tool()
def get_bkn_inovasi_by_idbkn(idbkn):
    """Mengambil statistik inovasi berdasarkan ID BKN instansi."""
    return call(f"/api/public/inovasi/idbkn/{idbkn}")

@mcp.tool()
def get_bkn_inovasi_count():
    """Mengambil jumlah record statistik inovasi."""
    return call("/api/public/inovasi/count")

@mcp.tool()
def get_bkn_master_instansi(page=0, size=20):
    """Mengambil master instansi dari API publik BKN."""
    return listing("/api/public/master-instansi", page, size)

@mcp.tool()
def get_bkn_instansi_by_id(id):
    """Mengambil instansi berdasarkan ID."""
    return call(f"/api/public/master-instansi/{id}")

@mcp.tool()
def search_bkn_instansi(nama, page=0, size=20):
    """Mencari instansi berdasarkan nama."""
    if not nama.strip():
        raise ValueError("nama tidak boleh kosong")
    return call("/api/public/master-instansi/search", {"nama": nama, **pagination(page, size)})

@mcp.tool()
def get_bkn_instansi_by_provinsi(kd_prov, page=0, size=20):
    """Mengambil instansi berdasarkan kode provinsi."""
    return call(f"/api/public/master-instansi/provinsi/{kd_prov}", pagination(page, size))

@mcp.tool()
def get_bkn_instansi_by_kode(cepat_kode):
    """Mengambil instansi berdasarkan kode cepat."""
    return call(f"/api/public/master-instansi/kode/{cepat_kode}")

@mcp.tool()
def get_bkn_instansi_by_jenis(jenis, page=0, size=20):
    """Mengambil instansi berdasarkan jenis."""
    return call(f"/api/public/master-instansi/jenis/{jenis}", pagination(page, size))

@mcp.tool()
def get_bkn_instansi_count():
    """Mengambil jumlah instansi."""
    return call("/api/public/master-instansi/count")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")