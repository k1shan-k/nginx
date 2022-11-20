def generate_nginx_config(server_name,host,port,path):
    config = 'server {\n' \
             '    listen 80;\n' \
             '    listen [::]:80;\n' \
             '        root ' + path + ';\n' \
             '        index index.html;\n' \
             '    server_name ' + server_name + ';\n' \
             '\n' \
             '    location / {\n' \
             '        try_files $uri $uri/ =404; ' ';\n' \
             '    }\n' \
             '    location /api {\n' \
             '        proxy_pass ' + host +':' + port + ';\n' \
             '    }\n' \
             '}'
    config1 = 'server {\n' \
             '    listen 80;\n' \
             '    listen [::]:80;\n' \
             '    server_name ' + server_name + ';\n' \
             '\n' \
             '    location / {\n' \
             '        proxy_pass ' + host +':' + port + ';\n' \
             '    }\n' \
             '}'
    if path=='null':
        return config1
    else:
        return config
print(generate_nginx_config('test.com','127.0.0.1','80','/var/www/'))
