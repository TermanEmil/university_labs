class Time
{
	constructor()
	{
		this.Update();
	}

	Update()
	{
		Time.deltaTime = (new Date().getTime() - Time.lastUpdateTime) / 1000;
		Time.lastUpdateTime = new Date().getTime();
	}
}