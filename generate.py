import urllib.request
import json
import sys

# 1. 目标规则源
IPV4_URL = "https://github.com/Hackl0us/GeoIP2-CN/raw/release/CN-ip-cidr.txt"
IPV6_URL = "https://ispip.clang.cn/all_cn_ipv6.txt"

def fetch_ip_list(url):
    ip_list = []
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            lines = response.read().decode('utf-8').splitlines()
            for line in lines:
                line = line.strip()
                # 过滤注释与空行
                if line and not line.startswith('#') and not line.startswith('//'):
                    ip_list.append(line)
    except Exception as e:
        print(f"Error fetching from {url}: {e}")
        sys.exit(1)
    return ip_list

def main():
    print("Downloading IPv4 rules...")
    ipv4_list = fetch_ip_list(IPV4_URL)
    
    print("Downloading IPv6 rules...")
    ipv6_list = fetch_ip_list(IPV6_URL)
    
    all_ips = ipv4_list + ipv6_list
    print(f"Total IP CIDRs loaded: {len(all_ips)} (IPv4: {len(ipv4_list)}, IPv6: {len(ipv6_list)})")

    # 2. 构造成 sing-box 1.8+ 标准的 rule-set JSON 结构
    rule_set_data = {
        "version": 1,
        "rules": [
            {
                "ip_cidr": all_ips
            }
        ]
    }

    # 3. 输出为 cnip.json
    with open("cnip.json", "w", encoding="utf-8") as f:
        json.dump(rule_set_data, f, indent=2, ensure_ascii=False)
    
    print("Successfully generated cnip.json!")

if __name__ == "__main__":
    main()
