# Let’s practice using Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d like you to set
# up your client SSH configuration file so that you can connect to a
# server without typing a password.
file { '~/ssh/school':
  ensure                 => create
  host                   => *
  line                   => IdentityFile ~/.ssh/school,
  PasswordAuthentication => 'no'
  }
