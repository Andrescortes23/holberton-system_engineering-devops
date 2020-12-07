# create a manifest that kills a process named killmenow

exec {'killmenow':
  command  => 'pkill -TERM -f killmenow',
  provider => shell,
  returs   => 0,
}