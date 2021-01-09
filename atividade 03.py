class Ponto:
    def init(self, x ,y):
        self.x = x
        self.y = y

    # @property
    def getX(self):
            return self.x

    def getY(self):
            return self.y

    # @x.setter
    def setX(self, x):
            return self.x
    # @y.setter
    def setY(self, y):
            return self.x

    def qualQuadrante(self, x, y):
            if(x > 0 and y > 0 ):
                return 1
            if(x < 0 and y > 0 ):
                return 2
            if(y < 0 and y < 0 ):
                return 3
            if(y < 0 and y > 0 ):
                return 4
            if(y == 0 and x == 0 ):
                return Origem

    # Quadrilátero = Retangulo
    class Quadrilatero():
        def init(self, P1, P2):
            self.P1 = P1
            self.P2 = P2

        def contidoEmQ(a):
            if(a.getX( ) <= P2.getX( ) and a.getX( ) >= P1.getX( ) and a.getY( ) <= P1.getY() and     a.getT() >= P2.getY()):
                return True
            else:
                return False