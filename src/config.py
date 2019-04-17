import socket

HOSTNAME_MAX_LEN = 249
CONTENT_ID_MAX_LEN = 256
LOCATION_ID_MAX_LEN = 256



DNS_IP = socket.gethostname()
DNS_PORT = 1234
DNS_MAX_LISTEN = 100

LB_CLIENT_MAX_LISTEN = 10
LB_CLIENT_LISTEN_PORT = 10000
LB_HEARTBEAT_PORT = 10002
LB_HEARTBEAT_TIME = 1	# seconds
MAX_CLIENT_REQUESTS = 10
LOAD_BALANCER_PRIMARY_IP = "127.0.0.1"
LOAD_BALANCER_SECONDARY_IP = "127.0.0.1"

EDGE_SERVER_PORT = 30005
EDGE_HEARTBEAT_LISTENER_PORT = 20000
EDGE_HEARTBEAT_LISTENER_PORT_SECONDARY = 25000
EDGE_HEARTBEAT_TIME = 1
MAX_EDGE_SERVERS = 5

MSG_DELAY = 5

ORIGIN_SERVER_PORT = 40000
ORIGIN_HEARTBEAT_TIME = 1
ORIGIN_HEARTBEAT_PORT = 40001
ORIGIN_CONTENT_PROVIDER_PORT = 40002
ORIGIN_METADATA_FILENAME = 'meta.pic'

# Location_id to position map
LOCATION = {}
LOCATION[0] = (0.,0.)
LOCATION[1] = (0.,1.)
LOCATION[2] = (1.,0.)
LOCATION[3] = (1.,1.)