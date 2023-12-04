# Notes on DNS and SSL

## nslookup

Use it via interactive method

```
$ nslookup
```


## specify server to use 

By default, it will use your specified dns server based upon network settings.  
Most likely you have this set via DHCP.  In this case, it might even be a
non routable IP such as 192.168.0.1 which in turn gets info via another
DNS server.  To be sure which one you are using, you can specify it with
the server command in interactive mode.

Well known public DNS servers

#### ipv4

* google `8.8.8.8`
* openDNS  `208.67.222.222`
* register.com 
#### ipv6

* google `2606:4700:4700::1111`
* openDNS `2620:0:ccc::2`

## Specify result type

These are commands issued while in the interactive mode of nslookup.

#### ipv4 results

```
> set q=A
```
#### ipv6 results

```
> set q=AAAA
```

#### CNAME results

```
> set q=CNAME
```

## Usage of whois

Another tool to use is `whois`

```
$ whois balsa.rtp-gcp.org
```

#### Notes on non interactive mode

If you wish to use in non-interactive mode, you can use the query option like so:

```
$ nslookup -type=CNAME rtp-gcp.org
```
If you wish to get all info 

```
$ nslookup -type=any rtp-gcp.org
```

If you wish to use a specific dns server

```
$ nslookup -type=any rtp.gcp.org 8.8.8.8
```

## dig

Get CNAME records for domain from using google DNS server

```
$ dig -t CNAME rtp-gcp.org @8.8.8.8.8
```
