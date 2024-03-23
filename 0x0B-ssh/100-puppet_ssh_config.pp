# Configure client's SSH file to connect to a server without typing password.

include stdlib
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#?IdentityFile',
}
