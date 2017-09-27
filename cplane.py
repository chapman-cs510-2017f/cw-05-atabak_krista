
class ListComplexPlane(AbsComplexPlane):

    plane = []
    for i in range(xlen):
        for k in range(ylen):
            self.plane.append([xmin+i*dx ,(ymin+k*dy)*1j])



    def __init__(self):
        xmin  = 0.0
        xmax  = 100.0
        xlen  = 100
        ymin  = 0.0
        ymax  = 100.0
        ylen  = 100
        plane = []
        for i in range(xlen):
            for k in range(ylen):
                self.plane.append([xmin+i*dx ,(ymin+k*dy)*1j])
        fs    = []

    def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):

        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        self.fs = []
        for i in range(xlen):
            for k in range(ylen):
                self.plane.append([xmin+i*dx ,(ymin+k*dy)*1j])


    def refresh():

        for i in range(self.xlen):
            for k in range(self.ylen):
                plane.append([self.xmin+i*dx ,(self.ymin+k*dy)*1j])

        fs = []

    def apply(self, f):

        for p in self.plane:
            f(p)

        self.fs.append(f)

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):

        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        for i in range(xlen):
            for k in range(ylen):
                self.plane.append([xmin+i*dx ,(ymin+k*dy)*1j])

        for f in self.fs:
            for p in self.plane:
                f(p)
            
            
            
            

            
            
            
            
            
            