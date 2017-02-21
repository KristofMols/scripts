import log
import subprocess

from log import Colors
from sys import stdout

def test_ports(services):
    stdout.write('{0:55}'.format(""))
    stdout.write(log.colorText(Colors.BUTTON_GREY, '    Host   '))
    stdout.write(' ')
    stdout.write(log.colorText(Colors.BUTTON_GREY, '    Port   '))
    stdout.write('\n')

    for service, values in sorted(services.iteritems()):
        host = values['host']
        port = values['port']

        stdout.write(log.colorText(Colors.RESET, '{0:25}'.format(service)))
        stdout.write(log.colorText(Colors.RESET, '{0:20}'.format(host)))
        stdout.write(log.colorText(Colors.RESET, '{0:10}'.format(port)))

        out, err = subprocess.Popen(['nc', '-zv', '-w', '3', host, port], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

        if out:
            value = out
        if err:
            value = err

        if value[len(value)-11:len(value)-1] == 'succeeded!':
            log.printStatusText(True)
            stdout.write(" ")
            log.printStatusText(True)
        elif value[len(value)-9:len(value)-1] == 'progress':
            log.printStatusText(False)
            stdout.write(" ")
            log.printStatusText(False)
        elif value[len(value)-8:len(value)-1] == 'refused':
            log.printStatusText(True)
            stdout.write(" ")
            log.printStatusText(False)

        stdout.write('\n')
