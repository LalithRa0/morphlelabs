from flask import Flask, render_template_string
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    name = "Lalith Rao"
    username = os.getenv('USER', os.getenv('USERNAME', 'unknown'))
    
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], 
                                          stderr=subprocess.STDOUT, 
                                          text=True)
    except Exception as e:
        top_output = f"Error getting top output: {str(e)}"
    
    
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head><title>System Monitor</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                pre { background: #f5f5f5; padding: 15px; border-radius: 5px; }
                .info { margin-bottom: 20px; }
            </style>
        </head>
        <body>
            <h1>System Information</h1>
            <div class="info">
                <p><strong>Name:</strong> {{ name }}</p>
                <p><strong>User:</strong> {{ username }}</p>
                <p><strong>Server Time (IST):</strong> {{ server_time }}</p>
            </div>
            <h2>TOP Output:</h2>
            <pre>{{ top_output }}</pre>
        </body>
        </html>
    ''', name=name, username=username, server_time=server_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)