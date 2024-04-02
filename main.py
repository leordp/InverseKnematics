from matplotlib import pyplot as plt
import numpy as np
import random as rd
from InverseKinematics import InverseKinematics
ITERATION_LIMIT = 15

# def get_magnitude(vector):
#     sum_squares = sum([np.power(vector[x],2) for x in range(0,len(vector))])
#     return np.sqrt(sum_squares)

# def get_angle_between(vector1,vector2):
#     dot_product = np.dot(vector1,vector2)
#     return np.arccos(dot_product/(get_magnitude(vector1)*get_magnitude(vector2)))


# class Robot:
    
#     def __init__(self,origin_point = np.zeros(2),n_dof = 3):
#         self.origin_point = origin_point
#         self.arm = []
#         self.arm.append(ArmSegment(origin_point=origin_point))
#         for i in range(1,n_dof):
#             theta = rd.uniform(-np.pi/2,np.pi/2)
#             self.arm.append(ArmSegment(origin_point=self.arm[i-1].end_point,theta=theta))

#     def calculate_end_point(self,i = 0):
#         self.arm[i].calculate_end_point()
#         if i < len(self.arm) - 1:
#             self.arm[i+1].origin_point = self.arm[i].end_point
#             self.calculate_end_point(i+1)
#         return self.arm[i].end_point

#     def show_robot(self):
#         self.calculate_end_point()
#         x = [self.arm[i].origin_point[0] for i in range(0,len(self.arm))]
#         y = [self.arm[i].origin_point[1] for i in range(0,len(self.arm))]
#         u = [self.arm[i].get_vector()[0] for i in range(0,len(self.arm))]
#         v = [self.arm[i].get_vector()[1] for i in range(0,len(self.arm))]
#         plt.quiver(x,y,u,v, scale_units='xy', scale=1)
#         plt.xlim([-5,5])
#         plt.ylim([-5,5])
#         plt.show()

#     def CCD(self,i,target_point):
#         if i < len(self.arm) - 1:  
#             self.CCD(i+1,target_point)  
#         current_point = self.arm[i].origin_point
#         angle = get_angle_between(self.arm[-1].end_point - current_point,target_point-current_point)
#         self.arm[i].theta += angle


#         self.calculate_end_point()

#         return self.arm[i].end_point
    
#     def IK_CCD(self,target_point,precision):
#         if get_magnitude(target_point - self.arm[0].origin_point) > self.reach:
#             raise TypeError("Point out of reach") 
#         iteration = 0
#         while get_magnitude(self.arm[-1].end_point - target_point) > precision or iteration < ITERATION_LIMIT:
#             self.CCD(0,target_point=target_point)
#             iteration += 1




# class ArmSegment:

#     def __init__(self,module = 1,origin_point = np.zeros(2),theta = 0):
#         self.origin_point = origin_point
#         self.module = module
#         self.theta = theta
#         self.end_point = self.calculate_end_point()
    
#     def rotation_matrix(self):
#         return np.array([[np.cos(self.theta),-np.sin(self.theta)],
#                          [np.sin(self.theta),np.cos(self.theta)]])

#     def calculate_end_point(self):
#         end_point = self.origin_point + np.array([self.module,0])
#         vector = end_point - self.origin_point
#         vector = np.matmul(self.rotation_matrix(),vector)
#         self.end_point = vector+self.origin_point
#         return self.end_point

#     def get_vector(self):
#         return self.end_point - self.origin_point


if __name__ == "__main__":
    ik = InverseKinematics(n_dof=3)
    ik.structure_.show()
    target = np.array([-1,1])
    ik.IK(target)
    ik.structure_.show()
    

    