from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return 'Admin Portal is working!'

@app.route('/create')
def create():
    loft_domain = os.getenv('LOFT_DOMAIN')
    access_key = os.getenv('ACCESS_KEY')
    command = f'curl -s -X POST --insecure "https://{loft_domain}/kubernetes/management/apis/management.loft.sh/v1/namespaces/loft-p-saas-tutorial/virtualclusterinstances" --data-binary "$(cat vcluster-template.yaml)" -H "Content-Type: application/yaml" -H "Authorization: Bearer {access_key}"'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return f'Error: {error}'
    else:
        return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)