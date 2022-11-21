def generatePreviewNginxConf(domain , host ,port,path):
    from nginx.config.api import Config, Section, Location
    pp=Section(
            'server',
        Location(
                  '/',
                  proxy_pass= f'{host}:{port}',
              ),
              Location(
                  '/api',
                  try_files="$uri $uri/ =404",
              ),
            listen='80',
            server_name=domain,
            root=path,
            index= 'index.html',
        )
    nginx = Config(
        worker_processes='auto',
        daemon='on',
        error_log='var/error.log',
    )
    return pp
print(generatePreviewNginxConf('test.com','127.0.0.1','89','/var/www/html'))
