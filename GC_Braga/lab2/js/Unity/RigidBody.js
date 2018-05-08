class RigidBody
{
    constructor()
    {
        this.velocity = glm.vec3(0, 0, 0);
        this.maxVel = glm.vec3(5, 5, 5);
        this.minVel = this.maxVel['*'](-1);
        this.linearDrag = glm.vec3(0, 0, 0);
        this.mass = 0;
    }

    Update()
    {
        if (this.velocity.x == 0 && this.velocity.y == 0 && this.velocity.z == 0)
            return;

        for (var i = 0; i < 3; i++)
        {
            
            if (this.velocity[i] > this.maxVel[i])
                this.velocity[i] = this.maxVel[i];
            else if (this.velocity[i] < this.minVel[i])
                this.velocity[i] = this.minVel[i];
        }
        this.transform.Translate(this.velocity['*'](Time.deltaTime));
    }
}