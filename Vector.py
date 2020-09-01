class Vector:
    x, y, z = 0, 0, 0;
    formatString = "(%.2f, %.2f, %.2f)"

    # constructors
    def __init__(self, x = 0, y = 0, z = 0):
        self.init(x, y, z)
        
    def init(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    # magnitudes
    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def lengthSquared(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def length2d(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def lengthSquared2d(self):
        return self.x ** 2 + self.y ** 2;

    # operators
    def dot(self, other):
        assert isinstance(other, Vector), "may only dot with another Vector"
        return self.x * other.x + self.y * other.y + self.z * other.z
        
    def add(self, *args):
        if len(args) == 1 and isinstance(args[0], Vector):
            other = args[0]
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif len(args) == 3 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)) and isinstance(args[2], (int, float)):
            return Vector(self.x + args[0], self.y + args[1], self.z + args[2])
        else:
            raise TypeError("unknown add arguments, expected [Vector other] or [number x, number y, number z]")
            
    def iadd(self, *args):
        if len(args) == 1 and isinstance(args[0], Vector):
            other = args[0]
            self.x += other.x
            self.y += other.y
            self.z += other.z
        elif len(args) == 3 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)) and isinstance(args[2], (int, float)):
            self.x += args[0]
            self.y += args[1]
            self.z += args[2]
        else:
            raise TypeError("unknown iadd arguments, expected [Vector other] or [number x, number y, number z]")
    
    def sub(self, *args):
        if len(args) == 1 and isinstance(args[0], Vector):
            other = args[0]
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif len(args) == 3 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)) and isinstance(args[2], (int, float)):
            return Vector(self.x - args[0], self.y - args[1], self.z - args[2])
        else:
            raise TypeError("unknown sub arguments, expected [Vector other] or [number x, number y, number z]")
            
    def isub(self, *args):
        if len(args) == 1 and isinstance(args[0], Vector):
            other = args[0]
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        elif len(args) == 3 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)) and isinstance(args[2], (int, float)):
            self.x -= args[0]
            self.y -= args[1]
            self.z -= args[2]
        else:
            raise TypeError("unknown isub arguments, expected [Vector other] or [number x, number y, number z]")
    
    def scale(self, f):
        assert isinstance(f, (int, float)), "must scale by a number"
        return Vector(self.x * f, self.y * f, self.z * f)
        
    def iscale(self, f):
        assert isinstance(f, (int, float)), "must iscale by a number"
        self.x *= f
        self.y *= f
        self.z *= f

    # util
    def setOutputPercision(self, decimalPlaces):
        assert isinstance(decimalPlaces, int), "setOutputPercision takes an integer, the number of decimals to display when converting to string. -1 = all decimals"
        if decimalPlaces < 0 or decimalPlaces > 16:
            decimalPlaces = 16
        self.formatString = "(%%.%df, %%.%df, %%.%df)" % (decimalPlaces, decimalPlaces, decimalPlaces)
    
    def __str__(self):
        return self.formatString % (self.x, self.y, self.z)
    
    def unit(self):
        length = self.length()
        return Vector(0.5773502691896258, 0.5773502691896258, 0.5773502691896258) if length == 0 else (Vector(self) if length == 1 else self.scale(1/length))
    
