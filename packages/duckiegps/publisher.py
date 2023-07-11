from dt_communication_utils import DTCommunicationGroup
from std_msgs.msg import Float32MultiArray
from triangulate import triangulate

group = DTCommunicationGroup('nuc_group',Float32MultiArray)

publisher = group.Publisher()
message = Float32MultiArray()
message.data=[[1,1,1],[2,2,2],[3,3,3]]
#message = triangulate()
publisher.publish(message)