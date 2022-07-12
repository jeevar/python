import nmap

np = nmap.PortScanner()

target = '192.168.1.0/24'

# Scan the subnet 
results = np.scan(hosts=target, arguments='-sn -Pn')

# Clean the data nmap returns
results = results['scan']
output = {}
for result in results:
    output[result] = {}
    try:
        output[result]['openshares'] = np.scan(hosts=resultss, arguments='--script smb-enum-shares.nse -p445')['smb']
        results = resultss['scan']
        output ={}
        for results in resultss:
            output[resultss]={}
    except:
        output[result]['smb'] = 'No Share found'
print(output,output)
