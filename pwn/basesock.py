import pwn, socket, time, sys, re, errno
from basechatter import basechatter
from pwn import log, text

class basesock(basechatter):
    def __init__(self, timeout = 'default'):
        basechatter.__init__(self, timeout)
        self.current_timeout = None

    def connected(self):
        return self.sock != None

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None
            log.info('Closed connection to %s on port %d' % self.target)

    def _send(self, dat):
        l = len(dat)
        i = 0
        while l > i:
            i += self.sock.send(dat[i:])

    def _recv(self, numb):
        if self.current_timeout != self.timeout:
            self.current_timeout = self.timeout
            if self.timeout == 0:
                self.sock.setblocking(0)
            else:
                self.sock.setblocking(1)
                self.sock.settimeout(self.timeout)

        return self.sock.recv(numb)

    def fileno(self):
        return self.sock.fileno()
