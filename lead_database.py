# Lead Capture System for iMPLEMENTAi.ae

import sqlite3
from datetime import datetime
import json
import os

# Database file path
DB_PATH = 'leads.db'

def init_database():
    """Initialize the SQLite database with tables for leads"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # AI Readiness Assessment Leads
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ai_readiness_leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            company TEXT NOT NULL,
            phone TEXT,
            score INTEGER NOT NULL,
            readiness_level TEXT,
            answers TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # ROI Calculator Leads
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS roi_calculator_leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            company TEXT,
            phone TEXT,
            employees INTEGER,
            hourly_rate REAL,
            manual_hours REAL,
            automation_rate REAL,
            implementation_cost REAL,
            monthly_cost REAL,
            annual_savings REAL,
            monthly_savings REAL,
            hours_saved REAL,
            payback_months INTEGER,
            three_year_roi REAL,
            five_year_benefit REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Contact Form Submissions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact_submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            company TEXT,
            phone TEXT,
            message TEXT,
            source TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # AI Expert Applications
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ai_expert_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            linkedin TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            availability TEXT,
            currency TEXT,
            rate REAL,
            rate_unit TEXT,
            expertise TEXT,
            engagement TEXT,
            tools TEXT,
            note TEXT,
            other_expertise TEXT,
            cv_filename TEXT,
            raw_form TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

def save_ai_readiness_lead(data):
    """Save AI Readiness Assessment lead"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO ai_readiness_leads 
        (name, email, company, phone, score, readiness_level, answers)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('name'),
        data.get('email'),
        data.get('company'),
        data.get('phone'),
        data.get('score'),
        data.get('readiness_level'),
        json.dumps(data.get('answers', {}))
    ))
    
    conn.commit()
    lead_id = cursor.lastrowid
    conn.close()
    
    return lead_id

def save_roi_calculator_lead(data):
    """Save ROI Calculator lead"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO roi_calculator_leads 
        (name, email, company, phone, employees, hourly_rate, manual_hours, 
         automation_rate, implementation_cost, monthly_cost, annual_savings, 
         monthly_savings, hours_saved, payback_months, three_year_roi, five_year_benefit)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('name'),
        data.get('email'),
        data.get('company'),
        data.get('phone'),
        data.get('employees'),
        data.get('hourly_rate'),
        data.get('manual_hours'),
        data.get('automation_rate'),
        data.get('implementation_cost'),
        data.get('monthly_cost'),
        data.get('annual_savings'),
        data.get('monthly_savings'),
        data.get('hours_saved'),
        data.get('payback_months'),
        data.get('three_year_roi'),
        data.get('five_year_benefit')
    ))
    
    conn.commit()
    lead_id = cursor.lastrowid
    conn.close()
    
    return lead_id

def save_contact_submission(data):
    """Save contact form submission"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO contact_submissions 
        (name, email, company, phone, message, source)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data.get('name'),
        data.get('email'),
        data.get('company'),
        data.get('phone'),
        data.get('message'),
        data.get('source', 'website')
    ))
    
    conn.commit()
    submission_id = cursor.lastrowid
    conn.close()
    
    return submission_id

def save_ai_expert_application(data):
    """Save AI Expert application"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO ai_expert_applications 
        (linkedin, email, phone, availability, currency, rate, rate_unit, expertise, engagement, tools, note, other_expertise, cv_filename, raw_form)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('linkedin'),
        data.get('email'),
        data.get('phone'),
        data.get('availability'),
        data.get('currency'),
        data.get('rate'),
        data.get('rate_unit'),
        data.get('expertise'),
        data.get('engagement'),
        data.get('tools'),
        data.get('note'),
        data.get('other_expertise'),
        data.get('cv_filename'),
        data.get('raw_form')
    ))

    conn.commit()
    application_id = cursor.lastrowid
    conn.close()

    return application_id

def get_all_leads(table_name='ai_readiness_leads', limit=100):
    """Retrieve leads from specified table"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute(f'SELECT * FROM {table_name} ORDER BY created_at DESC LIMIT ?', (limit,))
    rows = cursor.fetchall()
    
    leads = [dict(row) for row in rows]
    conn.close()
    
    return leads

def export_to_csv(table_name, filename):
    """Export leads to CSV file"""
    import csv
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute(f'SELECT * FROM {table_name} ORDER BY created_at DESC')
    rows = cursor.fetchall()
    
    if rows:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
            writer.writeheader()
            for row in rows:
                writer.writerow(dict(row))
        print(f"✅ Exported {len(rows)} records to {filename}")
    else:
        print("⚠️ No records to export")
    
    conn.close()

def get_stats():
    """Get statistics about leads"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    stats = {}
    
    # AI Readiness leads count
    cursor.execute('SELECT COUNT(*) FROM ai_readiness_leads')
    stats['ai_readiness_count'] = cursor.fetchone()[0]
    
    # ROI Calculator leads count
    cursor.execute('SELECT COUNT(*) FROM roi_calculator_leads')
    stats['roi_calculator_count'] = cursor.fetchone()[0]
    
    # Contact submissions count
    cursor.execute('SELECT COUNT(*) FROM contact_submissions')
    stats['contact_count'] = cursor.fetchone()[0]
    
    # Today's leads
    cursor.execute("SELECT COUNT(*) FROM ai_readiness_leads WHERE DATE(created_at) = DATE('now')")
    stats['today_ai_readiness'] = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM roi_calculator_leads WHERE DATE(created_at) = DATE('now')")
    stats['today_roi_calculator'] = cursor.fetchone()[0]
    
    conn.close()
    
    return stats

if __name__ == '__main__':
    # Initialize database
    init_database()
    
    # Show stats
    stats = get_stats()
    print("\n📊 Lead Statistics:")
    print(f"   AI Readiness Leads: {stats['ai_readiness_count']} (Today: {stats['today_ai_readiness']})")
    print(f"   ROI Calculator Leads: {stats['roi_calculator_count']} (Today: {stats['today_roi_calculator']})")
    print(f"   Contact Submissions: {stats['contact_count']}")
    print(f"\n💾 Database: {os.path.abspath(DB_PATH)}")
