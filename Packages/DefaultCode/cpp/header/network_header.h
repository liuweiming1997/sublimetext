#define ETH_LENGTH 6
#define PROTO_IP 0x0800
#define PROTO_UDP 0x8000

#pragma pack(2)

// 14
struct ethhdr {
  unsigned char s_dest[ETH_LENGTH];
  unsigned char d_dest[ETH_LENGTH];
  unsigned short h_proto;
};

// 20
struct iphdr {
  unsigned char version:4,
                hdrlen:4; // 虽然是4bit，可以表示15，但是单位要*4
  unsigned char tos; // 流媒体那些
  unsigned char totlen;
  unsigned short id;
  unsigned short flag:3,
                 offset:13;
  unsigned char ttl; // 网络经过一层就会减1，默认64
  unsigned char proto; // tcp/udp
  unsigned short check_sum;

  unsigned int s_ip;
  unsigned int d_ip;
};

// 8
struct udphdr {
  unsigned short s_port;
  unsigned short d_port;
  unsigned short length;
  unsigned short check_sum;
};

// udp packet
struct udppack {
  struct ethhdr eth_1; // 14
  struct iphdr ip_1; // 20
  struct udphdr upd_1; //8
  unsigned char body[0]; // sizeof(body) = 0，这个长度可以根据udp里面的长度规定
};
