import re


p = re.compile(ur'(?!10\.)(?!172\.(?:1[6-9]|2\d|3[01]))(?!192\.168\.)(?<!\d)\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?!\d)\b', re.MULTILINE | re.VERBOSE)

test_str = "Mar  8 00:41:29 snort snort: [1:40000002:100] ScanMe {ICMP} 10.0.0.1 -> 192.168.1.1"

re.findall(p, test_str)


