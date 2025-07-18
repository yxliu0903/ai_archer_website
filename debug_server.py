#!/usr/bin/env python3
"""
Debug version of the HTTP server with detailed logging
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from threading import Timer
import logging

PORT = 8000

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DebugHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        """Override to use our logger"""
        logger.info(f"Request: {format % args}")
    
    def end_headers(self):
        # Add CORS headers to allow cross-origin requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def guess_type(self, path):
        """Override to handle specific file types"""
        mimetype = super().guess_type(path)
        if path.endswith('.json'):
            return 'application/json'
        logger.info(f"File: {path}, MIME type: {mimetype}")
        return mimetype
    
    def do_GET(self):
        """Override GET to add logging"""
        logger.info(f"GET request for: {self.path}")
        
        # Check if requested file exists
        if self.path == '/':
            file_path = './index.html'
        else:
            file_path = '.' + self.path.split('?')[0]
        
        if os.path.exists(file_path):
            logger.info(f"File exists: {file_path}")
        else:
            logger.warning(f"File NOT found: {file_path}")
        
        return super().do_GET()

def open_browser():
    """Open browser after a short delay"""
    webbrowser.open(f'http://localhost:{PORT}')

def main():
    # Change to the directory containing the website files
    website_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(website_dir)
    
    logger.info(f"Working directory: {website_dir}")
    logger.info(f"Files in directory: {os.listdir('.')}")
    
    # Check if required files exist
    required_files = ['index.html', 'models_output_processed.json', 'cache_simplified.json']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        logger.error(f"Missing required files: {', '.join(missing_files)}")
        sys.exit(1)
    else:
        logger.info("All required files found")
    
    # Start the server
    with socketserver.TCPServer(("", PORT), DebugHTTPRequestHandler) as httpd:
        logger.info(f"神经网络研究数据展示网站正在运行...")
        logger.info(f"本地地址: http://localhost:{PORT}")
        logger.info(f"服务器目录: {website_dir}")
        logger.info(f"按 Ctrl+C 停止服务器")
        
        # Open browser after 2 seconds
        timer = Timer(2.0, open_browser)
        timer.start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("\n正在停止服务器...")
            httpd.shutdown()

if __name__ == "__main__":
    main() 