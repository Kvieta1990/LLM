Agentic AI with `n8n`
===

We will be using the `n8n` workflow orchestration framework to set up the Agentic AI for neutron powder diffraction. Current file contains technical notes about the setup.

## nginx

We will be using the `nginx` reverse proxy for hosting the interface between the internet and the `n8n` service (with `Docker`) running locally. On MacOS, when installing `nginx` with `homebrew`, the `nginx` configuration file is located at `/opt/homebrew/etc/nginx`. Here below is a working version of the `nginx` configuration file,

```
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    access_log  logs/access.log;
    error_log  logs/error.log;

    client_max_body_size 200M;
    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;
    add_header X-Frame-Options DENY;

    ssl_protocols TLSv1.3 TLSv1.2;
    ssl_prefer_server_ciphers on;

    include servers/*;

    server {
            listen 80;
            server_name n8n.ornl.gov;
            add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains; preload;' always;
            add_header X-Frame-Options DENY;
            add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains; preload;' always;
            add_header X-Frame-Options "SAMEORIGIN";
            return 301 https://n8n.ornl.gov$request_uri;
    }

    map $http_upgrade $connection_upgrade {
            default upgrade;
            '' close;
    }

    server {
        listen       443 ssl;
        server_name  n8n.ornl.gov;
        root         /usr/share/nginx/html;

        add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains; preload;' always;
        add_header X-Frame-Options "DENY";

        ssl_certificate "/Users/y8z/Dev/certificates/n8n.pem";
        ssl_certificate_key "/Users/y8z/Dev/certificates/n8n.key";

        location / {
            proxy_pass http://localhost:5678;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_pass_request_headers on;
            add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains; preload;' always;
            add_header Cache-Control "no-store, no-cache, must-revalidate, proxy-revalidate" always;
            add_header Pragma "no-cache" always;
            add_header Expires "0" always;
            add_header X-Frame-Options "SAMEORIGIN";
            add_header X-Frame-Options "DENY" always;
            proxy_set_header X-Frame-Options "SAMEORIGIN";
        }

        error_page 404 /404.html;
            location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
}
```