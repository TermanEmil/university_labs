class GameObject
{
	constructor()
	{
		this.transform = new Transform();
		this.components = [];
		this.AddComponent(this.transform);

		GameController.instance.objs.push(this);
	}

	Update()
	{
		this.components.forEach(function(component)
		{
			if (typeof component.Update === 'function')
				component.Update();
		});
	}

	AddComponent(newComponent)
	{
		newComponent.gameObject = this;
		newComponent.transform = this.transform;
		this.components.push(newComponent);
	}
}
