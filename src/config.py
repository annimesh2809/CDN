import socket

HOSTNAME_MAX_LEN = 249
CONTENT_ID_MAX_LEN = 256
LOCATION_ID_MAX_LEN = 256

DNS_IP = socket.gethostname()
DNS_PORT = 1234
DNS_MAX_LISTEN = 100

LB_CLIENT_MAX_LISTEN = 10
LB_CLIENT_LISTEN_PORT = 10000
LB_CLIENT_LISTEN_PORT_BACKUP = 10010
LB_HEARTBEAT_PORT = 10002
LB_HEARTBEAT_TIME = 1	# seconds
MAX_CLIENT_REQUESTS = 10
LOAD_BALANCER_PRIMARY_IP = "127.0.0.1"
LOAD_BALANCER_SECONDARY_IP = "127.0.0.1"
EDGE_SERVER_PORT = 30005
LB1_HEARTBEAT_LISTENER_PORT = 20002
LB2_HEARTBEAT_LISTENER_PORT = 20003
EDGE_HEARTBEAT_TIME = 1
MAX_EDGE_SERVERS = 5
EDGE_CONTENT_DICT_FILENAME = 'content_dic'

MSG_DELAY = 5

ORIGIN_SERVER_PORT_1 = 40000
ORIGIN_SERVER_PORT_2 = 40001
ORIGIN_HEARTBEAT_TIME = 1
ORIGIN_SYNCHRONIZER_PORT_1 = 40002
ORIGIN_SYNCHRONIZER_PORT_2 = 40003
ORIGIN_CONTENT_PROVIDER_PORT_1 = 40004
ORIGIN_CONTENT_PROVIDER_PORT_2 = 40005
ORIGIN_METADATA_FILENAME = 'meta.pic'

# Location_id to position map
LOCATION = {}
LOCATION[0] = (0.,0.)
LOCATION[1] = (0.,1.)
LOCATION[2] = (1.,0.)
LOCATION[3] = (1.,1.)

WEIGHT_DISTANCE = 0.8
WEIGHT_LOAD = 0.2