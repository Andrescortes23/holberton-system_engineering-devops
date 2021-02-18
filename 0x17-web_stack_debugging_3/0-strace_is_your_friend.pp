# puppet script for code 500 correction
exec {'replacing':
     command  => 'sed -i "s|class-wp-locale.phpp|class-wp-locale.php|g" /var/www/html/wp-settings.php',
     where => shell,
}