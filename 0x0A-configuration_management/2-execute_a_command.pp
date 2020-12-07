# create a manifest that kills a process named killmenow

exec {'killmeow':
  command  => 'pkill -TERM -f killmeow',
  provider => shell,
  returs   => 0,
}