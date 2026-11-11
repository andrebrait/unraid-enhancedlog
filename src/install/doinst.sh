if [ ! -f /boot/config/plugins/enhanced.log3/enhanced.log3.cfg ]; then
  cp -a /usr/local/emhttp/plugins/enhanced.log3/default/enhanced.log3.cfg /boot/config/plugins/enhanced.log3/enhanced.log3.cfg
fi

if [ ! -f /boot/config/plugins/enhanced.log3/custom_syslog.conf ]; then
  cp -a /usr/local/emhttp/plugins/enhanced.log3/default/custom_syslog.conf /boot/config/plugins/enhanced.log3/custom_syslog.conf
fi

if [ ! -f /boot/config/plugins/enhanced.log3/syslog_filter.conf ]; then
  cp -a /usr/local/emhttp/plugins/enhanced.log3/default/syslog_filter.conf /boot/config/plugins/enhanced.log3/syslog_filter.conf
fi

/usr/local/emhttp/plugins/enhanced.log3/scripts/rc.enhanced.log3