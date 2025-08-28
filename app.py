
from flask import Flask, request
import pyodbc

app = Flask(__name__)

@app.route('/test-db')
def test_db():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=192.168.188.112,1433;'
            'DATABASE=Pupuk;'
            'UID=user_pkt_bb;'
            'PWD=Initial2022!!;'
            'TrustServerCertificate=yes;'
        )
        cursor = conn.cursor()
        cursor.execute('SELECT 1')
        result = cursor.fetchone()
        conn.close()
        return f"Koneksi berhasil! Hasil query: {result}"
    except Exception as e:
        return f"Koneksi gagal: {e}"


@app.route('/get-data-stock-opname-penerimaan-bahan-baku', methods=['GET'])
def get_data_stock_opname_penerimaan_bahan_baku():
    try:
        from_date = request.args.get('from')
        to_date = request.args.get('to')
        if not from_date or not to_date:
            return {"error": "Parameter 'from' dan 'to' wajib diisi, format: YYYYMMDD"}
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=192.168.188.112,1433;'
            'DATABASE=Pupuk;'
            'UID=user_pkt_bb;'
            'PWD=Initial2022!!;'
            'TrustServerCertificate=yes;'
        )
        cursor = conn.cursor()
        query = f'''
            SELECT *
            FROM [Pupuk].[dbo].[v_daan_d000_mseg_mkpf]
            WHERE (
                MATNR like '%1000030' or MATNR like '%3000499' or MATNR like '%3000018' or MATNR like '%3000004' or 
                MATNR like '%4002084' or MATNR like '%1000051' or MATNR like '%1000054' or MATNR like '%3000019' or 
                MATNR like '%3000007' or MATNR like '%3000298' or MATNR like '%4002360' or MATNR like '%4002362' or 
                MATNR like '%1002654' or MATNR like '%3000036'
            )
            and BWART = '301'
            and CAST(BUDAT AS VARCHAR) >= '{from_date}'
            and CAST(BUDAT AS VARCHAR) <= '{to_date}'
            and (LGORT like '%1L02%' or LGORT like '%1L01%')
        '''
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        # Ambil data terakhir untuk kombinasi MATNR, LGORT, BUDAT
        latest_data = {}
        for row in rows:
            row_dict = dict(zip(columns, row))
            key = (row_dict['MATNR'], row_dict['LGORT'], row_dict['BUDAT'])
            # Jika ada data dengan key yang sama, simpan yang terakhir (override)
            latest_data[key] = row_dict
        data = list(latest_data.values())
        conn.close()
        return {"data": data}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True)
