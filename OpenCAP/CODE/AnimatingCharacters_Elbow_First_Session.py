import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

def readMarkerData(file_path):
    data = ""
    pathFile = ""
    ex_title_list = []
    ex_data_list = []
    titles = []

    data = []
    with open(file_path) as file:
        count = 0
        for line in file:
            if(count==0):
                l = line.split(" ")
#                 print(l)
                pathFile = l[3]
            elif(count == 1):
                l = line.split("\t")
                ex_title_list = l
            elif(count == 2):
                l = line.split("\t")
                ex_data_list = l
            elif(count == 3):
                l = line.split("\t")
                # Remove spaces from each element using list comprehension
                l = [item for item in l if item != ""]
                titles = l
                # Print the result
#                 print(l)

            elif (count == 4 or count == 5):
                pass

            else:
                l = line.split("\t")
                data.append(l)


            count+=1
#     print(data)
    
    
    last_string = ex_title_list[-1].rstrip('\n')
    ex_title_list[-1] = last_string

    last_string = ex_data_list[-1].rstrip('\n')
    ex_data_list[-1] = last_string
    
    dataDict = {}
    
    dataDict['PathFileType'] = pathFile
    
    
    # dataDict

    # For Data rate, Camera Rate etc
    for i in range(len(ex_title_list)):
        dataDict[ex_title_list[i]] = ex_data_list[i]

    datas = {}

    a = 2
    for i in range(len(data)):
        for j in range(len(data[i])):
            try:
                datas[str(j)].append(data[i][j])
            except:
                datas[str(j)] = [data[i][j]]

#     print(datas)
    # datas['3']
    # For the Titles
    count = 0
    for i in range(len(titles)):
        if(i < 2):
            dataDict[titles[i]] = datas[str(count)]
            count=count+1
        else:
            try:
                dataDict[titles[i]] = {}
                dataDict[titles[i]]['X'] = datas[str(count)]
                dataDict[titles[i]]['Y'] = datas[str(count+1)]
                dataDict[titles[i]]['Z'] = datas[str(count+2)]
                count=count+3
            except:
                pass
    return dataDict


markerData = readMarkerData("C:/Users/Jatin/Desktop/Engineering/ROBOTICS PROGRAM NUS/PROJECT/OpenCAP/DATA/NUS_PROJECT_DATA/MarkerData/Elbow_Start1.trc")
n = markerData['NumFrames']

def getCoordinates(i):
    X = []
    Y = []
    Z = []
    Labels = []

    flag = 0
    for key, value in markerData.items():
        if(key == "Time"):
            flag = 1
            continue
        if(flag == 1):
            try:
                if(key == "Neck" or key == "RShoulder" or key == "RElbow" or key == "RWrist" or key == "LShoulder" or key == "LElbow" or key == "LWrist" or key == "midHip" or key == "RHip" or key == "RKnee" or key == "RAnkle" or key == "LHip" or key == "LKnee" or key == "LAnkle" or key == "LBigToe" or key == "LSmallToe" or key == "LHeel" or key == "RBigToe" or key == "RSmallToe" or key == "RHeel"):
                    x = value['X'][i]
                    y = value['Y'][i]
                    z = value['Z'][i]
                    labels = key


                    X.append(float(x))
                    Y.append(float(y))
                    Z.append(float(z))
                    Labels.append(labels)
            except:
                pass
    return [X,Y,Z,Labels]



# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set labels for each axis
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')


# Set X-axis range to 0-2
ax.set_xlim(0, 2)

plt.ion()  # Turn on interactive mode

# Plot the points as dots
sc = ax.scatter([], [], [], c='r', marker='o')

# Real-time updating loop
for i in range(int(n)):
    # Clear the previous data
    ax.clear()
    # Set X-axis range to 0-2
    ax.set_xlim(0, 2)
    # print(i)
    # time.sleep(0.1)  # Simulate some data generation delay
    X,Y,Z,Labels = getCoordinates(i)        
    # Define pairs for lines
    line_segments = [((Labels.index("Neck"), Labels.index("RShoulder"))), ((Labels.index("Neck"), Labels.index("LShoulder"))),((Labels.index("RShoulder"), Labels.index("RElbow"))),
                    ((Labels.index("RElbow"), Labels.index("RWrist"))), ((Labels.index("LElbow"), Labels.index("LShoulder"))),((Labels.index("LElbow"), Labels.index("LWrist"))),
                    ((Labels.index("Neck"), Labels.index("midHip"))), ((Labels.index("midHip"), Labels.index("RHip"))), ((Labels.index("midHip"), Labels.index("LHip"))), 
                    ((Labels.index("LHip"), Labels.index("LKnee"))), ((Labels.index("LKnee"), Labels.index("LAnkle"))), ((Labels.index("LAnkle"), Labels.index("LHeel"))),
                    ((Labels.index("LAnkle"), Labels.index("LSmallToe"))), ((Labels.index("LAnkle"), Labels.index("LBigToe"))), ((Labels.index("RHip"), Labels.index("RKnee"))),
                    ((Labels.index("RKnee"), Labels.index("RAnkle"))),((Labels.index("RAnkle"), Labels.index("RHeel"))), ((Labels.index("RAnkle"), Labels.index("RBigToe"))),
                    ((Labels.index("RAnkle"), Labels.index("RSmallToe")))]


    # Replace these with your actual XYZ coordinates and point labels
    x_points = X
    y_points = Y
    z_points = Z
    point_labels = Labels  # Add labels for each point


    # # Plot the points as dots
    # sc = ax.scatter(x_points, y_points, z_points, c='r', marker='o')


    # Scatter3d trace for lines
    for segment in line_segments:
        x_conn = [x_points[j] for j in segment]
        y_conn = [y_points[j] for j in segment]
        z_conn = [z_points[j] for j in segment]
        ax.plot(x_conn, y_conn, z_conn, c='b', linestyle='-', linewidth=2)


    # Update the scatter plot
    sc._offsets3d = (X, Y, Z)

    # Draw the updated plot
    plt.draw()
    plt.pause(0.1)

# plt.ioff()  # Turn off interactive mode (optional)
plt.show()