class Animation
{
	Update()
	{
	}
}

class Animator
{
	constructor()
	{
		this.animations = {};
		this.currentAnim = "idle";
	}

	Update()
	{
		if (this.animations[this.currentAnim] == undefined)
			throw this.currentAnim + ": No such animation.";
		else
			this.animations[this.currentAnim].Update();
	}
}
