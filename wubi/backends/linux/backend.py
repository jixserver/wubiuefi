import commands
from backends.shared_backend import Backend, Progress

class LinuxBackend(Backend):
    '''
    Linux-specific backend
    '''
    
    def get_stuff(self):
        self.info.timezone = commands.getoutput('date +%Z')
        self.info.arch = commands.getoutput('uname -m')
        self.info.username = commands.getoutput('whoami')