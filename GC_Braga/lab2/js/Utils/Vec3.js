class Vec3
{
    constructor(x, y, z)
    {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    static FromVals(values)
    {
        return new Vec3(values[0], values[1], values[2]);
    }

    Mult(other)
    {
        return new Vec3(this.x * other.x, this.y * other.y, this.z * other.z);
    }

    MultScalar(scalar)
    {
        return new Vec3(this.x * scalar, this.y * scalar, this.z * scalar);
    }

    Add(vec3)
    {
        return new Vec3(this.x + vec3.x, this.y + vec3.y, this.z + vec3.z);
    }

    ToVals()
    {
        return [this.x, this.y, this.z];
    }
}