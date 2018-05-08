class RigidBody
{
    constructor()
    {
        this.velocity = glm.vec3(0, 0, 0);
        this.linearDrag = glm.vec3(1, 1, 1)['*'](0.3);

        this.angularVel = glm.vec3(0, 0, 0);
        this.angularDrag = glm.vec3(1, 1, 1)['*'](0.3);
        
        this.mass = 0;
    }

    Update()
    {
        this.transform.Translate(this.velocity['*'](Time.deltaTime));
        this.transform.Rotate(this.angularVel['*'](Time.deltaTime));
        
        for (var i = 0; i < 3; i++)
        {
            this.velocity[i] = (1.0 - this.linearDrag[i] * Time.deltaTime) * this.velocity[i];
            this.angularVel[i] = (1.0 - this.angularDrag[i] * Time.deltaTime) * this.angularVel[i];
        }
    }
}