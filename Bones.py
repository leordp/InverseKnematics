from matplotlib import pyplot as plt
import numpy as np
import random as rd


class Bones:
    def __init__(self,module = 1,origin_point = np.zeros(2),theta = 0):
        self.origin_ = origin_point
        self.module_ = module
        self.theta_ = theta

    def calculate_end(self):
        end_point = self.origin_ + np.array([self.module_,0])
        vector = end_point - self.origin_
        vector = np.matmul(self.rotation_matrix,vector)
        return vector+self.origin_
    
    def rotate(self,theta):
        self.theta_ += theta
        return self.vector
    
    @property
    def end_point(self):
        return self.calculate_end()
    
    @property
    def rotation_matrix(self):
        return np.array([[np.cos(self.theta_),-np.sin(self.theta_)],
                         [np.sin(self.theta_),np.cos(self.theta_)]])
    @property
    def vector(self):
        return(self.end_point - self.origin_)


class BoneStructure:
    def __init__(self,n_dof = 0,origin_=np.zeros(2)):
        self.strcuture_ = []
        self.strcuture_.append(Bones(origin_point=origin_,))
        for i in range(1,n_dof):
            theta = rd.uniform(-np.pi/2,np.pi/2)
            self.strcuture_.append(Bones(origin_point=self.strcuture_[i-1].end_point,theta=theta))
        self.calculate_end_point()

    def __len__(self):
        return len(self.strcuture_)
    
    def __getitem__(self,key):
        if key < len(self.strcuture_):
            return self.strcuture_[key]
        else:
            return -1


    def append_node(self,module_ = 1):
        new_bone = Bones(module_=module_,origin_point=self.end_point)
        self.strcuture_.append(new_bone)

    def calculate_end_point(self,i = 0):
        self.strcuture_[i].end_point
        if i < len(self.strcuture_) - 1:
            self.strcuture_[i+1].origin_ = self.strcuture_[i].end_point
            self.calculate_end_point(i+1)
        return self.strcuture_[i].end_point

    @property
    def end_point(self):
        self.calculate_end_point()
        return self.strcuture_[-1].end_point
    
    @property
    def reach(self):
        return sum([self.strcuture_[i].module_ for i in range(0,len(self.strcuture_))])
    
    def show(self):
        x = [self.strcuture_[i].origin_[0] for i in range(0,len(self.strcuture_))]
        y = [self.strcuture_[i].origin_[1] for i in range(0,len(self.strcuture_))]
        u = [self.strcuture_[i].vector[0] for i in range(0,len(self.strcuture_))]
        v = [self.strcuture_[i].vector[1] for i in range(0,len(self.strcuture_))]
        plt.quiver(x,y,u,v, scale_units='xy', scale=1)
        plt.xlim([-5,5])
        plt.ylim([-5,5])
        plt.show()
    
