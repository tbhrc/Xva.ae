# Quick Start Script for Lead Capture System
# This script will help you get the lead capture system running

import subprocess
import sys
import os
import time

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def check_dependencies():
    """Check if required packages are installed"""
    print_header("CHECKING DEPENDENCIES")
    
    try:
        import flask
        import flask_cors
        print("✅ Flask and Flask-CORS are installed")
        return True
    except ImportError:
        print("❌ Missing dependencies")
        print("\nInstalling required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True

def initialize_database():
    """Initialize the database"""
    print_header("INITIALIZING DATABASE")
    
    import lead_database as db
    db.init_database()
    
    stats = db.get_stats()
    print(f"\n📊 Database Statistics:")
    print(f"   AI Readiness Leads: {stats['ai_readiness_count']}")
    print(f"   ROI Calculator Leads: {stats['roi_calculator_count']}")
    print(f"   Contact Submissions: {stats['contact_count']}")
    print(f"\n💾 Database file: {os.path.abspath(db.DB_PATH)}")

def main():
    print("\n🚀 iMPLEMENTAi.ae - Lead Capture System Setup")
    print("="*60)
    
    # Step 1: Check dependencies
    if not check_dependencies():
        print("\n❌ Failed to install dependencies")
        return
    
    # Step 2: Initialize database
    initialize_database()
    
    # Step 3: Instructions
    print_header("SETUP COMPLETE!")
    
    print("📋 Next Steps:\n")
    print("1. Start the API server:")
    print("   python api_server.py")
    print("\n2. Keep your website server running on port 8080")
    print("\n3. Test the forms:")
    print("   - AI Readiness: http://localhost:8080/ai-readiness.html")
    print("   - ROI Calculator: http://localhost:8080/roi-calculator.html")
    print("\n4. View leads using the dashboard:")
    print("   python lead_dashboard.py")
    print("\n5. Export leads to CSV from the dashboard")
    
    print("\n" + "="*60)
    print("💡 TIP: Keep both servers running:")
    print("   - Website: python -m http.server 8080")
    print("   - API: python api_server.py")
    print("="*60 + "\n")
    
    # Ask if user wants to start API server now
    response = input("Would you like to start the API server now? (y/n): ").strip().lower()
    
    if response == 'y':
        print("\n🚀 Starting API server...")
        print("Press Ctrl+C to stop the server\n")
        time.sleep(2)
        subprocess.call([sys.executable, "api_server.py"])

if __name__ == '__main__':
    main()
