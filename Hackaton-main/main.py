import socket 
from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
@app.route('/admin/dashboard')
def adminDashboard():
     hostname = socket.gethostname()
     ip_address = socket.gethostbyname(hostname)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
malicious_ips = {'192.168.56.1', '5.6.7.8'}
def check_ip():
    if ip_address in malicious_ips:
       
         print({'message': f'The IP {ip_address} is malicious.'})
    else:
         print({'message': f'The IP {ip_address} is safe.'})
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
check_ip()
