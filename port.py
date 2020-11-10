
ip = sys.argv[1]

for port in range(1000):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((ip, port))
        print '%d:Open' % (port)
        s.close()
    except:
       continue
