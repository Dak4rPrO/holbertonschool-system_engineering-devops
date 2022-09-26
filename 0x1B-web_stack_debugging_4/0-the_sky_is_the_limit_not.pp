#Using puppet, find out why requests are failing and fix them.

exec {
  'sed -i s/15/1000/ /etc/default/nginx':
}

exec {
  'service nginx restart':
}
