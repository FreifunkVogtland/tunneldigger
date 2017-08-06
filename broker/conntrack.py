import sys
import subprocess
import os
from socket import AF_INET, AF_INET6, IPPROTO_TCP, IPPROTO_UDP

class ConnectionManager(object):

    def __init__(self):
        '''
        Create new ConnectionManager object
        '''

    def kill(self, proto, src, dst, sport, dport, silent_query = True):
        '''
        Delete specified connection.
        '''
	# we only use UDP
	proto = "UDP"
	
	args = ['-p', proto, '-s', src, '-d', dst, '--sport', str(sport), '--dport', str(dport)]
	self.__run_conntrack(args)

    def killall(self, proto = None, src = None, dst = None, sport = None, dport = None):

        #we only use UDP
        proto = "UDP"

        args = ['-p', proto]

	if src:
	  args.extend(['-s', src])
	if dst:
	  args.extend(['-d', dst])
	if sport:
	  args.extend(['--sport', str(sport)])
	if dport:
	  args.extend(['--dport', str(dport)])
        self.__run_conntrack(args)


    def __run_conntrack(self, args):
        cmd = ['/usr/sbin/conntrack', '-D'] + args
        self.__run(cmd)


    def __run(self, cmd):
        p = subprocess.Popen(cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=True)
        out, err = p.communicate()
        status = p.wait()
        # check exit status

        if not os.WIFEXITED(status) or os.WEXITSTATUS(status):
#	     print("conntrack error:", cmd, err)
	    pass
        return out






