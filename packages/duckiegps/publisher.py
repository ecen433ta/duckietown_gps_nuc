from dt_communication_utils import DTCommunicationGroup
from std_msgs.msg import Float32MultiArray, MultiArrayLayout, MultiArrayDimension
from triangulate import triangulate
from cap_objects import Caps

group = DTCommunicationGroup('nuc_group',Float32MultiArray)

publisher = group.Publisher()
message = Float32MultiArray()
caps = Caps()

# set up the layout for the multi-dimensional array

while(True):
    twod_array=triangulate(caps) # get the list of things from the triangulate function

    # flatten the array
    # flat_message = [item for sublist in twod_array for item in sublist]
    message.data = twod_array

    layout_msg = MultiArrayLayout()
    layout_msg.dim.append(MultiArrayDimension())
    layout_msg.dim[0].label = "row"
    layout_msg.dim[0].size = len(twod_array)
    layout_msg.dim[0].stride = len(twod_array)
    layout_msg.dim.append(MultiArrayDimension())
    layout_msg.dim[1].label = "column"
    layout_msg.dim[1].size = len(twod_array)
    layout_msg.dim[1].stride = 1
    
    message.layout = layout_msg
    # publish the message
    publisher.publish(message)
    print(message.data)

