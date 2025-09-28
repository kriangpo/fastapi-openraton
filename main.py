from fastapi import FastAPI, Request
import smtplib
import mysql.connector

app = FastAPI()

@app.post("/api/v1/send-email")
async def send_email_api(request: Request):
    data = await request.json()
    employee = data.get("employeeName")
    approved = data.get("approved")
    send_email(employee, approved)
    return {"status": "email sent"}

@app.post("/api/v1/save-db")
async def save_db_api(request: Request):
    data = await request.json()
    employee = data.get("employeeName")
    days = data.get("leaveDays")
    reason = data.get("reason")
    approved = data.get("approved")
    save_to_db(employee, days, reason, approved)
    return {"status": "db saved"}

def send_email(employee, approved):
    status = "approved" if approved else "rejected"
    msg = f"Hello {employee}, your leave request has been {status}."
    print("ส่ง email แล้ว")
    '''
    with smtplib.SMTP("smtp.yourdomain.com", 587) as server:
        server.login("noreply@yourdomain.com", "password")
        server.sendmail("noreply@yourdomain.com", f"{employee}@yourdomain.com", msg)
    '''

def save_to_db(employee, days, reason, approved):
    conn = mysql.connector.connect(
        host="172.26.8.178",
        user="root",
        password="your_password",
        database="operaton"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO leave_request (employee, days, reason, approved) VALUES (%s, %s, %s, %s)",
        (employee, days, reason, approved)
    )
    conn.commit()
    cursor.close()
    conn.close()
