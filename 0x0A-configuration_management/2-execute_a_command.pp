# Manifest that kills a process called 'killmenow'.

exec { 'killmenow':
  command     => 'pkill killmenow',
  refreshonly => true,
}
