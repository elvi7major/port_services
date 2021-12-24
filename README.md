# port_services
simple ports services name finder from IANA
[link to database](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv)

# USAGE
```bash
python3 ports_services.py port_number
Ex: python3 ports_services.py 80
```
Result
```bash
root@kali:$ python3 ports_services.py 445
Port Number Service Name Transport Protocol Description
445         microsoft-ds         tcp       Microsoft-DS
445         microsoft-ds         udp       Microsoft-DS
```
