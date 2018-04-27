class Input
{
  constructor()
  {
    Input.instance = this;

    this.onKeyDown = {};
    document.addEventListener('keydown', function(event){
      if (Input.instance.onKeyDown[event.key] != undefined)
        Input.instance.onKeyDown[event.key](event);
    });
  }
}
