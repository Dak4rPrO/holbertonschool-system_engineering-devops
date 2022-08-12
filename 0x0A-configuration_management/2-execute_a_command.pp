# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'killmenow':
  path    => '/user/bin/',
  command => '[pkill -f killmenow]'
}