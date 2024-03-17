import ipinfo
import json
import ipaddress
print('Which website would you like to locate?')
user_input = input()
handler = ipinfo.getHandler()
def get_ips_by_dns_lookup(target, port=None):
    '''
        this function takes the passed target and optional port and does a dns
        lookup. it returns the ips that it finds to the caller.

        :param target:  the URI that you'd like to get the ip address(es) for
        :type target:   string
        :param port:    which port do you want to do the lookup against?
        :type port:     integer
        :returns ips:   all of the discovered ips for the target
        :rtype ips:     list of strings

    '''
    import socket

    if not port:
        port = 443
    try:
        ip_obj = ipaddress.ip_address(target)
        print(f"{target} is a valid IP address")
        print('IP is', target)
        details = handler.getDetails(target)
        print('IP is located at:', details.city)
        print('The ISP for this IP is', details.org)
    except ValueError:
        ips = list(map(lambda x: x[4][0], socket.getaddrinfo('{}.'.format(target),port,type=socket.SOCK_STREAM)))
        print('IP is', ips[0])
        details = handler.getDetails(ips[0])
        print('IP is located at:', details.city)
        print('The ISP for this IP is', details.org)
get_ips_by_dns_lookup(user_input)