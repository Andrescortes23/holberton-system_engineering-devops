# puppet script for code 500 correction
exec { 'replacing':
     command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
     path    => [ '/usr/bin', '/bin', '/usr/sbin', '/sbin' ],
}