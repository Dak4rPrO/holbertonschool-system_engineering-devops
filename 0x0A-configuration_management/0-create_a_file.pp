# Using Puppet, create a file in /tmp.
file { '/tmp/school':
  owner   => www-date,
  group   => www-date,
  mode    => '0744',
  content => 'I love Puppet'
  }