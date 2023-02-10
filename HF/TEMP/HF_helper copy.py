import numpy as np
import math

class HF_tools():
    
    def __init__(self):
        self.K = 4 #NUMBER OF BASIS FUNCTIONS
        self.N = 2 #NUMBER OF ELECTRONS
        self.E = np.zeros(self.K)
        self.r_bas = [0.0,0.0,0.0,0.0] # CENTERS OF BASIS SETS
        self.a     = [13.00773 ,1.962079, 0.444529, 0.1219492]
        self.r_nuc = [0.0] # CENTER OF NUCLEOUS
        self.Z     = [1.0] # CHARGE OF NUCLEOUS
        self.F     = np.zeros([self.K,self.K])
        self.set_S_ij()
        self.set_T_ij()
        self.set_A_ij()
        self.set_G_ijkl()
        self.set_S_inv_sqrt()
        self.C=np.zeros([self.K,self.K])
        # for i in range(int(self.N/2)):
        #     self.C[:,i]=1.0
        self.set_P_ij()

    def add_nuclues(self):
        pass

    def add_basis_functions(self):
        pass

    def set_S_inv_sqrt(self):
        V=np.zeros([self.K,self.K])
        D,U =np.linalg.eig(self.S)
        D=1/D**0.5
        D=np.diag(D)
        UD=np.matmul(U,D)
        self.S_inv_sqrt=np.matmul(UD,U.T)


    def get_total_E(self):
        total_E=0.0
        for i in range(int(self.N/2.)):
            total_E += 2*self.E[i]

        for i in range(self.K):
            for j in range(self.K):
                    self.P[i,j]

        JK=0 
        for i in range(self.K):
            for j in range(self.K):    
                for k in range(self.K):
                    for l in range(self.K):
                        JK += self.P[k,l]*(self.G[i,j,k,l]-0.5*self.G[i,k,j,l]); 

        return total_E-JK
       

    def set_P_ij(self):
        P=np.zeros([self.K,self.K])
        for i in range(self.K):
            for j in range(self.K):
                for k in range(int(self.N/2)):
                    P[i,j] += 2*self.C[i,k]*self.C[j,k]
        self.P=P

    def set_S_ij(self):
        S=np.zeros([self.K,self.K])
        for i in range(self.K):
            for j in range(self.K):
                asum = self.a[i]+self.a[j]
                ap = self.a[i]*self.a[j]
                rat=ap/asum
                S[i,j]=(np.pi/asum)**(1.5)*math.exp(-rat*(self.r_bas[i]-self.r_bas[j])**2)

        self.S = S

    def set_T_ij(self):
        T=np.zeros([self.K,self.K])
        for i in range(self.K):
            for j in range(self.K):
                asum = self.a[i]+self.a[j]
                ap = self.a[i]*self.a[j]
                rat=ap/asum
                T[i,j]=0.5*rat*(6-4*rat*(self.r_bas[i]-self.r_bas[j])**2)*self.S[i,j]
        self.T = T        

    def set_A_ij(self):
        A=np.zeros([self.K,self.K])
        for i in range(self.K):
            for j in range(self.K):
                asum = self.a[i]+self.a[j]
                ap = self.a[i]*self.a[j]
                rat=ap/asum
                rp=(self.a[i]*self.r_bas[i]+self.a[j]*self.r_bas[j])/asum
                F0=0
                for r,Z in zip(self.r_nuc,self.Z):
                    if rp == r:
                        F0+=1
                    else:
                        F0+=(np.pi**0.5)/2*(math.erf(np.abs(asum*(rp-r)))/np.abs(asum*(rp-r)))
                    
                    A[i,j] += -2*np.pi*Z/asum*math.exp(-rat*(self.r_bas[i]-self.r_bas[j])**2)*F0
               
        self.A = A

    def set_G_ijkl(self):
        G=np.zeros([self.K,self.K,self.K,self.K])

        for i in range(self.K):
            for j in range(i): 
                as1=self.a[i]+self.a[j]
                ap1=self.a[i]*self.a[j]
                rp=(self.a[i]*self.r_bas[i]+self.a[j]*self.r_bas[j])/as1
                for k in range(i-1):
                    for l in range(k): 
                        as2=self.a[k]+self.a[l];
                        ap2=self.a[k]*self.a[l];
                        rq=(self.a[k]*self.r_bas[k]+self.a[l]*self.r_bas[l])/as2;
                        if ((rp-rq)==0):
                            F0=1;
                        else:
                            F0=(np.pi**0.5)/2*math.erf((as1*as2*(rp-rq)**2/(as1+as2))**0.5)/(as1*as2*(rp-rq)**2/(as1+as2))**0.5;

                        G[i,j,k,l]=( 2*np.pi**2.5/(as1*as2*(as1+as2)**0.5) )  *math.exp(-ap1*(self.r_bas[i]-self.r_bas[j])**2/as1-ap2*(self.r_bas[k]-self.r_bas[l])**2/as2)*F0;
                        G[k,l,i,j]=G[i,j,k,l]
                        G[j,i,k,l]=G[i,j,k,l]
                        G[i,j,l,k]=G[i,j,k,l]
                        G[j,i,l,k]=G[i,j,k,l]
                        G[k,l,j,i]=G[i,j,k,l]
                        G[l,k,i,j]=G[i,j,k,l]
                        G[l,k,j,i]=G[i,j,k,l]
                    
                    k=i
                    for l in range(j):
                        as2=self.a[k]+self.a[l]
                        ap2=self.a[k]*self.a[l]
                        rq=(self.a[k]*self.r_bas[k]+self.a[l]*self.r_bas[l])/as2;
                        if ((rp-rq)==0):
                            F0=1
                        else:
                            F0=(np.pi**0.5)/2*math.erf((as1*as2*(rp-rq)**2/(as1+as2))**0.5)/(as1*as2*(rp-rq)**2/(as1+as2))**0.5
                        
                        G[i,j,k,l]=( 2*np.pi**2.5/(as1*as2*(as1+as2)**0.5))*math.exp(-ap1*(self.r_bas[i]-self.r_bas[j])**2/as1-ap2*(self.r_bas[k]-self.r_bas[l])**2/as2)*F0;
                        G[k,l,i,j]=G[i,j,k,l]
                        G[j,i,k,l]=G[i,j,k,l]
                        G[i,j,l,k]=G[i,j,k,l]
                        G[j,i,l,k]=G[i,j,k,l]
                        G[k,l,j,i]=G[i,j,k,l]
                        G[l,k,i,j]=G[i,j,k,l]
                        G[l,k,j,i]=G[i,j,k,l] 
                    
        self.G=G
