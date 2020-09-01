public class Vector
{
    private String formatString = "(%.2f, %.2f, %.2f)";
    public double x, y, z = 0;

    // constructors
    Vector(){}
    Vector(double x, double y, double z)
    {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    Vector(int x, int y, int z)
    {
        this.x = (double)x;
        this.y = (double)y;
        this.z = (double)z;
    }
    Vector(Vector other)
    {
        this.x = other.x;
        this.y = other.y;
        this.z = other.z;
    }
    void init(Vector other)
    {
        this.x = other.x;
        this.y = other.y;
        this.z = other.z;
    }
    void init(double x, double y, double z)
    {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    void init(int x, int y, int z)
    {
        this.x = (double)x;
        this.y = (double)y;
        this.z = (double)z;
    }

    // magnitudes
    double length()
    {
        return Math.sqrt(x*x + y*y + z*z);
    }

    double lengthSquared()
    {
        return x*x + y*y + z*z;
    }

    double length2d()
    {
        return Math.sqrt(x*x + y*y);
    }

    double lengthSquared2d()
    {
        return x*x + y*y;
    }

    // operators
    double dot(Vector other)
    {
        return x * other.x + y * other.y + z * other.z;
    }
    Vector add(Vector other)
    {
        return new Vector(x + other.x, y + other.y, z + other.z);
    }
    Vector add(double x, double y, double z)
    {
        return new Vector(this.x + x, this.y + y, this.z + z);
    }
    Vector add(int x, int y, int z)
    {
        return new Vector(this.x + (double)x, this.y + (double)y, this.z + (double)z);
    }
    void iadd(Vector other)
    {
        x += other.x;
        y += other.y;
        z += other.z;
    }
    void iadd(double x, double y, double z)
    {
        this.x += x;
        this.y += y;
        this.z += z;
    }
    void iadd(int x, int y, int z)
    {
        this.x += (double)x;
        this.y += (double)y;
        this.z += (double)z;
    }
    Vector sub(Vector other)
    {
        return new Vector(x - other.x, y - other.y, z - other.z);
    }
    Vector sub(double x, double y, double z)
    {
        return new Vector(this.x - x, this.y - y, this.z - z);
    }
    Vector sub(int x, int y, int z)
    {
        return new Vector(this.x - (double)x, this.y - (double)y, this.z - (double)z);
    }
    void isub(Vector other)
    {
        x -= other.x;
        y -= other.y;
        z -= other.z;
    }
    void isub(double x, double y, double z)
    {
        this.x -= x;
        this.y -= y;
        this.z -= z;
    }
    void isub(int x, int y, int z)
    {
        this.x -= (double)x;
        this.y -= (double)y;
        this.z -= (double)z;
    }
    Vector scale(double f)
    {
        return new Vector(x * f, y * f, z * f);
    }
    Vector scale(int f)
    {
        return new Vector(x * (double)f, y * (double)f, z * (double)f);
    }
    void iscale(double f)
    {
        x *= f;
        y *= f;
        z *= f;
    }
    void iscale(int f)
    {
        x *= (double)f;
        y *= (double)f;
        z *= (double)f;
    }

    // util
    void setOutputPercision(int decimalPlaces)
    {
        if (decimalPlaces < 0 || decimalPlaces > 16)
            decimalPlaces = 16;
        this.formatString = String.format("(%%.%df, %%.%df, %%.%df)", decimalPlaces, decimalPlaces, decimalPlaces);
    }
    @Override
    public String toString()
    {
        return String.format(this.formatString, x, y, z);
    }
    Vector unit()
    {
        double length = this.length();
        // tfw you can't switch on a double
        return length == 0.f ? new Vector(0.5773502691896258, 0.5773502691896258, 0.5773502691896258) : length == 1.f ? new Vector(this) : this.scale(1 / length);
    }
}
