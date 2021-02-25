# debbug to set number of request to unlimit
exec { 'upperlimit' :
     command => 'sed -i "s/15/15000/g" /etc/default/nginx',
     path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
     onlyif  => 'test -e /etc/default/nginx,
}