import subprocess
subprocess.Popen('/bin/ls -l %s' % ('something else',), shell=True)
