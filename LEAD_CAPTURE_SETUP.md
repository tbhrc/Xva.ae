# LEAD CAPTURE SYSTEM - SETUP GUIDE

## 🎯 Overview
Complete lead capture system for iMPLEMENTAi.ae with SQLite database and Flask API.

## 📦 Components

1. **lead_database.py** - Database management (SQLite)
2. **api_server.py** - Flask API server
3. **lead_dashboard.py** - Command-line dashboard
4. **requirements.txt** - Python dependencies

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Initialize Database
```bash
python lead_database.py
```

### Step 3: Start API Server
```bash
python api_server.py
```
Server will run on http://localhost:5000

### Step 4: Keep Website Server Running
Your website should already be running on http://localhost:8080

## 📊 Database Tables

### 1. ai_readiness_leads
- Captures AI Readiness Assessment submissions
- Fields: name, email, company, phone, score, readiness_level, answers, created_at

### 2. roi_calculator_leads
- Captures ROI Calculator data
- Fields: name, email, company, phone, employees, hourly_rate, manual_hours, automation_rate, implementation_cost, monthly_cost, annual_savings, monthly_savings, hours_saved, payback_months, three_year_roi, five_year_benefit, created_at

### 3. contact_submissions
- Captures contact form submissions
- Fields: name, email, company, phone, message, source, created_at

## 🔌 API Endpoints

### Submit Data
- `POST /api/ai-readiness` - Submit AI Readiness assessment
- `POST /api/roi-calculator` - Submit ROI calculator data
- `POST /api/contact` - Submit contact form

### Retrieve Data
- `GET /api/leads/ai-readiness?limit=100` - Get AI Readiness leads
- `GET /api/leads/roi-calculator?limit=100` - Get ROI Calculator leads
- `GET /api/stats` - Get lead statistics

### Export
- `GET /api/export/ai_readiness_leads` - Export to CSV
- `GET /api/export/roi_calculator_leads` - Export to CSV
- `GET /api/export/contact_submissions` - Export to CSV

## 💻 Using the Dashboard

Run the command-line dashboard:
```bash
python lead_dashboard.py
```

Features:
- View latest leads
- Export to CSV
- View statistics
- Filter by date

## 📁 Files Location

- Database: `leads.db` (created automatically)
- CSV Exports: `*_YYYYMMDD_HHMMSS.csv`

## 🔧 Configuration

### Change API Port
Edit `api_server.py`, line: `app.run(debug=True, port=5000)`

### Change Database Location
Edit `lead_database.py`, line: `DB_PATH = 'leads.db'`

## 🌐 Frontend Integration

Forms automatically send data to API:
- AI Readiness form → http://localhost:5000/api/ai-readiness
- ROI Calculator → http://localhost:5000/api/roi-calculator

If API is offline, forms still work (data stored in localStorage).

## 📈 Monitoring

Check API health:
```bash
curl http://localhost:5000/api/health
```

View stats:
```bash
curl http://localhost:5000/api/stats
```

## 🔒 Security Notes

**For Production:**
1. Add authentication to API endpoints
2. Use HTTPS
3. Add rate limiting
4. Validate all inputs
5. Use environment variables for sensitive data
6. Deploy API to secure server (not localhost)

## 📧 Email Notifications (Optional)

To add email notifications when new leads arrive, edit `api_server.py` and add:
```python
import smtplib
from email.mime.text import MIMEText

def send_notification(lead_data):
    # Configure your email settings
    pass
```

## 🎯 Next Steps

1. ✅ Database created
2. ✅ API server ready
3. ✅ Forms updated
4. ⏳ Start API server: `python api_server.py`
5. ⏳ Test form submissions
6. ⏳ View leads in dashboard

## 💡 Tips

- Keep API server running alongside website server
- Use dashboard to monitor leads in real-time
- Export to CSV regularly for backup
- Check `leads.db` file for all data

## 🆘 Troubleshooting

**API not connecting?**
- Check if API server is running on port 5000
- Check browser console for CORS errors
- Verify localhost:5000 is accessible

**Database errors?**
- Delete `leads.db` and run `python lead_database.py` again
- Check file permissions

**Forms not submitting?**
- Forms will still work even if API is offline
- Data is stored in localStorage
- Check browser console for errors
