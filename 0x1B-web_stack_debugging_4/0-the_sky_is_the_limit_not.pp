# debbug to set number of request to unlimit
exec { 'find and correct':
    command => "sed -i 's/ULIMIT=/# ULIMIT=/g' /etc/default/nginx",
    path    => [ '/usr/bin' , '/bin', '/usr/sbin', '/sbin' ],
}
exec { 'restart nginx':
    command => 'sudo service nginx restart',
    path    => '/usr/bin',
} ~>
service { 'nginx':
    ensure    => running,
}
