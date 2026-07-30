# sing-box CNIP Rule-Set

这是一个自动构建并维护的 sing-box 规则集项目。项目通过 GitHub Actions 定时合并指定来源的中国大陆 IPv4 与 IPv6 CIDR 地址段，并编译生成二进制 `.srs` 规则文件及 JSON 源码文件。

---

## 数据来源

- **IPv4**: `https://github.com/Hackl0us/GeoIP2-CN/raw/release/CN-ip-cidr.txt`
- **IPv6**: `https://ispip.clang.cn/all_cn_ipv6.txt`

---

## 自动构建说明

- **更新频率**: 每日自动拉取数据源、合并去重并编译更新。
- **输出路径**: 生成的文件存放在仓库的 `output/` 目录下：
  - `output/cnip.srs`: sing-box 二进制规则集 (推荐)
  - `output/cnip.json`: sing-box JSON 源码规则集

---
