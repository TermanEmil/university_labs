class ArrayBuffer
{
	constructor(array, itemSize, numItems, drawType = gl.STATIC_DRAW)
	{
		this.array = array;
		this.itemSize = itemSize;
		this.numItems = numItems;
		this.drawType = drawType;
	}
}
