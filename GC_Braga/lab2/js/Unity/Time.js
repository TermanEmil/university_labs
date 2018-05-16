class Time
{
	constructor()
	{
		this.Update();
		Time.start = new Date().getTime() / 1000;

		// Time.TotalTime = this.TotalTime;
	}

	Update()
	{
		Time.deltaTime = (new Date().getTime() - Time.lastUpdateTime) / 1000;
		Time.lastUpdateTime = new Date().getTime();
	}

	static TotalTime()
	{
		return new Date().getTime() / 1000 - Time.start;
	}
}