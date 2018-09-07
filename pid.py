import subprocess

ros_nodes = []
p = subprocess.run(
    './extra/pid.sh',
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True,
    check=True
)

stdout = p.stdout.decode('utf-8')
for o in stdout.splitlines():
    pid = o.split()[1]
    p = subprocess.run(
        'ps -T -p ' + pid,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        check=True
    )

    _stdout = p.stdout.decode('utf-8')
    for _o in _stdout.splitlines()[1:]:
        ros_nodes.append(_o.split()[1])

print(ros_nodes)
