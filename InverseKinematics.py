import numpy as np
import random as rd
from matplotlib import pyplot as plt
from Bones import BoneStructure
from HelperFunctions import *
PRECISION = 0.01
ITERATIONLIMIT = 10


class InverseKinematics:
    def __init__(self,n_dof=0,origin=np.zeros(2)):
        self.structure_ = BoneStructure(n_dof,origin)
        self.origin_ = origin

    def CCD(self,i=0,target_point = [0,0]):

        if i < len(self.structure_) - 1:  
            self.CCD(i+1,target_point)  
        current_point = self.structure_[i].origin_
        angle = angle_between(self.structure_.end_point - current_point,target_point-current_point)
        self.structure_[i].theta_ += angle

        return self.structure_[i].end_point
    
    def set_method(self,method='CCD'):
        if method == 'CCD':
            return self.CCD
        return self.CCD

    def IK(self,target,method='CCD'):
        if euclidean_distance(self.origin_,target) > self.structure_.reach:
            raise TypeError("Point out of reach")
        ik = self.set_method(method)
        iteration = 0
        while iteration < ITERATIONLIMIT and euclidean_distance(self.structure_.end_point,target) > PRECISION:
            ik(target_point=target)
            iteration += 1

