# Flask API Server for Lead Capture
# Run this with: python api_server.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import lead_database as db
import json
import os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)  # Enable CORS for local development

# Initialize database on startup
db.init_database()

@app.route('/api/ai-readiness', methods=['POST'])
def submit_ai_readiness():
    """Handle AI Readiness Assessment submissions"""
    try:
        data = request.get_json()
        
        # Calculate readiness level
        score = data.get('score', 0)
        if score >= 25:
            readiness_level = "AI Ready"
        elif score >= 18:
            readiness_level = "AI Capable"
        elif score >= 12:
            readiness_level = "AI Emerging"
        else:
            readiness_level = "AI Exploring"
        
        data['readiness_level'] = readiness_level
        
        # Save to database
        lead_id = db.save_ai_readiness_lead(data)
        
        return jsonify({
            'success': True,
            'lead_id': lead_id,
            'readiness_level': readiness_level,
            'message': 'Assessment submitted successfully'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/roi-calculator', methods=['POST'])
def submit_roi_calculator():
    """Handle ROI Calculator submissions"""
    try:
        data = request.get_json()
        
        # Save to database
        lead_id = db.save_roi_calculator_lead(data)
        
        return jsonify({
            'success': True,
            'lead_id': lead_id,
            'message': 'ROI calculation saved successfully'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Save to database
        submission_id = db.save_contact_submission(data)
        
        return jsonify({
            'success': True,
            'submission_id': submission_id,
            'message': 'Contact form submitted successfully'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/ai-experts/apply', methods=['POST'])
def submit_ai_expert_application():
    """Handle AI Expert Hub applications"""
    try:
        form = request.form
        files = request.files

        cv_filename = None
        cv_file = files.get('cv')
        if cv_file and cv_file.filename:
            upload_dir = os.path.join('uploads', 'cv')
            os.makedirs(upload_dir, exist_ok=True)
            safe_name = secure_filename(cv_file.filename)
            unique_name = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}_{safe_name}"
            cv_path = os.path.join(upload_dir, unique_name)
            cv_file.save(cv_path)
            cv_filename = unique_name

        application_data = {
            'linkedin': form.get('linkedin', '').strip(),
            'email': form.get('email'),
            'phone': form.get('phone'),
            'availability': form.get('availability'),
            'currency': form.get('currency'),
            'rate': form.get('rate'),
            'rate_unit': form.get('rateUnit'),
            'expertise': form.get('expertise'),
            'engagement': form.get('engagement'),
            'tools': form.get('tools'),
            'note': form.get('note'),
            'other_expertise': form.get('otherExpertise'),
            'cv_filename': cv_filename,
            'raw_form': json.dumps(form.to_dict(flat=True))
        }

        if not application_data['linkedin']:
            return jsonify({
                'success': False,
                'error': 'LinkedIn profile is required.'
            }), 400

        application_id = db.save_ai_expert_application(application_data)

        return jsonify({
            'success': True,
            'application_id': application_id,
            'message': 'AI Expert application submitted successfully'
        }), 200

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/leads/ai-readiness', methods=['GET'])
def get_ai_readiness_leads():
    """Get all AI Readiness leads"""
    try:
        limit = request.args.get('limit', 100, type=int)
        leads = db.get_all_leads('ai_readiness_leads', limit)
        return jsonify({
            'success': True,
            'count': len(leads),
            'leads': leads
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/leads/roi-calculator', methods=['GET'])
def get_roi_calculator_leads():
    """Get all ROI Calculator leads"""
    try:
        limit = request.args.get('limit', 100, type=int)
        leads = db.get_all_leads('roi_calculator_leads', limit)
        return jsonify({
            'success': True,
            'count': len(leads),
            'leads': leads
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get lead statistics"""
    try:
        stats = db.get_stats()
        return jsonify({
            'success': True,
            'stats': stats
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/export/<table_name>', methods=['GET'])
def export_leads(table_name):
    """Export leads to CSV"""
    try:
        filename = f'{table_name}_{db.datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        db.export_to_csv(table_name, filename)
        return jsonify({
            'success': True,
            'filename': filename,
            'message': f'Exported to {filename}'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Lead capture API is running'
    }), 200

if __name__ == '__main__':
    print("Starting Lead Capture API Server...")
    print("API Endpoints:")
    print("   POST /api/ai-readiness - Submit AI Readiness assessment")
    print("   POST /api/roi-calculator - Submit ROI calculator data")
    print("   POST /api/contact - Submit contact form")
    print("   POST /api/ai-experts/apply - Submit AI Expert application")
    print("   GET  /api/leads/ai-readiness - Get AI Readiness leads")
    print("   GET  /api/leads/roi-calculator - Get ROI Calculator leads")
    print("   GET  /api/stats - Get lead statistics")
    print("   GET  /api/export/<table_name> - Export leads to CSV")
    print("\nServer running on http://localhost:5000")
    print("Database: leads.db")
    print("\nPress Ctrl+C to stop the server\n")

    app.run(debug=True, port=5000, host='0.0.0.0')
