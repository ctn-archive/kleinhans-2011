import nef
import math

segments=100
feedback_pstc=0.1
period=1
omega=(math.pi*2)/period # omega =10 worked well for the starting paramaters


#specify vector that defines position of neuron on the cartisian plane
encoders=[]
for i in range(segments): 
	#colon for anytime indent
	theta1 = i*math.pi/segments
	theta2 = theta1+math.pi
	encoders.append([math.sin(theta1),math.cos(theta1)])
	encoders.append([math.sin(theta2),math.cos(theta2)])
	
	

net = nef.Network('Lamprey') #capitals when referring to a class
motor = net.make('motor',neurons=2*segments,dimensions=2,tau_rc=0.02,tau_ref=0.002,radius=1, 
	encoders=encoders, intercept=[0.7,0.8],max_rate=[200,200]) # (tau_ref/rc = mseconds) 2 neurons per segment - coupled neurons doing opposite opperations intercepts to be played with later.. close to theta origin
# python has a set list of places to look for in directories and therefore subdirectories (nesting)
# perfered direction vectors of neurons manage how they fire (representing a circle)
input=net.make_input('Input',[0,0])
net.connect(input,motor,pstc=0.01)
net.connect(motor,motor,pstc=feedback_pstc,transform=[[1,feedback_pstc*omega],[-feedback_pstc*omega,1]])

net.add_to(world)

