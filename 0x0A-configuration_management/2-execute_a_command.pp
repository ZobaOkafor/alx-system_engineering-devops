# Manifest that kills a process called 'killmenow'.

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
}
