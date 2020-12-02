import socket
from concurrent.futures import ThreadPoolExecutor, wait
from tools.time_counter import calc_time_interval
from logger import get_logger

log = get_logger("hunyuan")
alive_port = []


def sock_connect(ip_port):
    ip, port = ip_port.split(':')
    timeout = 2
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_sock.settimeout(timeout)
    log.info("ip and port: %s" % ip_port)
    res = -1
    try:
        res = tcp_sock.connect_ex((ip, int(port)))
        if res == 0:
            log.info("the open port is: %s" % port)
            global alive_port
            alive_port.append((ip, port))
    except socket.error as e:
        log.error('socket error: %s' % e)
    finally:
        tcp_sock.close()
        return res


@calc_time_interval
def scan_port():
    executor = ThreadPoolExecutor(max_workers=30)
    ip_list = ['139.9.126.27']
    port_list = [x for x in range(3305, 65535)]
    all_task = []
    for ip in ip_list:
        for port in port_list:
            print("the ip and port: ", ip, port)
            res = executor.submit(sock_connect, (ip + ":" + str(port)))
            all_task.append(res)
    log.info("all task length: %s" % len(all_task))
    # for task in all_task:
    #     print(task.result())
    wait(all_task)
    log.info("all finished!")


if __name__ == '__main__':
    scan_port()
    # sock_connect("139.9.126.27", 3306)
    # [('139.9.126.27', '3306'), ('139.9.126.27', '5433'), ('139.9.126.27', '7011'),
    #  ('139.9.126.27', '8080'), ('139.9.126.27', '8090'), ('139.9.126.27', '9500')]
    print("open ports: ", alive_port)
