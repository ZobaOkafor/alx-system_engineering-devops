# Install Nginx package

package { 'nginx':
  ensure => installed,
}

# Define custom HTTP header value
$hostname = $facts['hostname']

# Configure Nginx to add custom header
file { '/etc/nginx/conf.d/custom_response_header.conf':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        proxy_pass http://localhost:8080;
        add_header X-Served-By ${hostname};
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}",
  notify  => Service['nginx'],
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/conf.d/custom_response_header.conf'],
}
