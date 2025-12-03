# Lead Dashboard - View and Export Leads
# Run this with: python lead_dashboard.py

import lead_database as db
from datetime import datetime
import os

def print_header(title):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def display_ai_readiness_leads(limit=10):
    """Display AI Readiness leads"""
    leads = db.get_all_leads('ai_readiness_leads', limit)
    
    print_header(f"AI READINESS ASSESSMENT LEADS (Latest {limit})")
    
    if not leads:
        print("No leads found.")
        return
    
    for i, lead in enumerate(leads, 1):
        print(f"\n{i}. {lead['name']} - {lead['company']}")
        print(f"   Email: {lead['email']}")
        print(f"   Phone: {lead['phone'] or 'N/A'}")
        print(f"   Score: {lead['score']}/30 - {lead['readiness_level']}")
        print(f"   Date: {lead['created_at']}")

def display_roi_calculator_leads(limit=10):
    """Display ROI Calculator leads"""
    leads = db.get_all_leads('roi_calculator_leads', limit)
    
    print_header(f"ROI CALCULATOR LEADS (Latest {limit})")
    
    if not leads:
        print("No leads found.")
        return
    
    for i, lead in enumerate(leads, 1):
        name = lead['name'] or 'Anonymous'
        company = lead['company'] or 'N/A'
        print(f"\n{i}. {name} - {company}")
        if lead['email']:
            print(f"   Email: {lead['email']}")
        print(f"   Employees: {lead['employees']}")
        print(f"   Annual Savings: AED {lead['annual_savings']:,.0f}")
        print(f"   Payback: {lead['payback_months']} months")
        print(f"   Date: {lead['created_at']}")

def display_stats():
    """Display lead statistics"""
    stats = db.get_stats()
    
    print_header("LEAD STATISTICS")
    print(f"\nTotal Leads:")
    print(f"  AI Readiness Assessments: {stats['ai_readiness_count']}")
    print(f"  ROI Calculator: {stats['roi_calculator_count']}")
    print(f"  Contact Submissions: {stats['contact_count']}")
    print(f"\nToday's Leads:")
    print(f"  AI Readiness: {stats['today_ai_readiness']}")
    print(f"  ROI Calculator: {stats['today_roi_calculator']}")

def export_menu():
    """Export leads to CSV"""
    print_header("EXPORT LEADS TO CSV")
    print("\n1. AI Readiness Leads")
    print("2. ROI Calculator Leads")
    print("3. Contact Submissions")
    print("4. All Tables")
    print("0. Back to Main Menu")
    
    choice = input("\nSelect option: ").strip()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if choice == '1':
        filename = f'ai_readiness_leads_{timestamp}.csv'
        db.export_to_csv('ai_readiness_leads', filename)
    elif choice == '2':
        filename = f'roi_calculator_leads_{timestamp}.csv'
        db.export_to_csv('roi_calculator_leads', filename)
    elif choice == '3':
        filename = f'contact_submissions_{timestamp}.csv'
        db.export_to_csv('contact_submissions', filename)
    elif choice == '4':
        db.export_to_csv('ai_readiness_leads', f'ai_readiness_leads_{timestamp}.csv')
        db.export_to_csv('roi_calculator_leads', f'roi_calculator_leads_{timestamp}.csv')
        db.export_to_csv('contact_submissions', f'contact_submissions_{timestamp}.csv')
        print("✅ All tables exported!")

def main_menu():
    """Main menu"""
    while True:
        print_header("LEAD MANAGEMENT DASHBOARD")
        print("\n1. View AI Readiness Leads")
        print("2. View ROI Calculator Leads")
        print("3. View Statistics")
        print("4. Export to CSV")
        print("5. Refresh Database Stats")
        print("0. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            limit = input("How many leads to display? (default 10): ").strip() or "10"
            display_ai_readiness_leads(int(limit))
        elif choice == '2':
            limit = input("How many leads to display? (default 10): ").strip() or "10"
            display_roi_calculator_leads(int(limit))
        elif choice == '3':
            display_stats()
        elif choice == '4':
            export_menu()
        elif choice == '5':
            display_stats()
        elif choice == '0':
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    print("\n🚀 iMPLEMENTAi.ae - Lead Management Dashboard")
    print(f"💾 Database: {os.path.abspath(db.DB_PATH)}")
    
    # Initialize database if needed
    if not os.path.exists(db.DB_PATH):
        print("\n⚠️  Database not found. Initializing...")
        db.init_database()
    
    main_menu()
