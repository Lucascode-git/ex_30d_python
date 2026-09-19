
from statistics import mean
import statistics

print()

raw_servers = [
    ('web-01', '10.0.0.1', 'running', 512),
    ('db-01', '10.0.0.2', 'stopped', 2048),
    ('cache-01', '10.0.0.3', 'running', 256),
    ('worker-01', '10.0.0.4', 'maintenance', 1024),
]

extra_tags = ['prod', 'prod', 'staging', 'prod']
extra_zones = ['eu-west', 'eu-west', 'us-east', 'eu-west']

def build_servers(raw, tags, zones):
    id_info =[]
    for index, (r, t, z) in enumerate(zip(raw, tags, zones), start=1):
        id_info.append({'id':index, 'name': r[0], 'ip':r[1], 'status':r[2], 'memory':r[3], 'tag':t, 'zone':z})
    return id_info
#print(build_servers(raw_servers, extra_tags, extra_zones))

def listinfo(listi):
    name, ip, status, memory = listi
    return f'{name} {ip} - {status}, {memory}MB'

list_userinfo = list(raw_servers[0])
#print(listinfo(list_userinfo))

def memory_report(*sizes):
    '''Retourne des statistiques sur des tailles mémoire'''
    return {'total': sum(sizes), 'mean': mean(sizes), 'min': min(sizes), 'max': max(sizes)}

listmemo = []
for info in raw_servers:
    listmemo.append(info[-1])

print(memory_report(*listmemo))
print()


def safe_lookup(servers, name):
    pair = {}
    for log in servers:
        pair[log[0]] = log[1:]
    try:
        test = pair[name]
        print(test)
    except:
        return None
    else:
        print('Name in server logs')
    finally:
        print('function end')

verification = safe_lookup(raw_servers, 'web-01')
print()

base = {'region': 'eu-west', 'replicas': 1, 'ssl': False}
override = {'replicas': 3, 'ssl': True}

def merge_config(base, override):
    return {**base, **override}

print(merge_config(base, override))


test1 = ['je']
test2 = ['ke']
too = [*test1 , *test2]
print(too)



print()